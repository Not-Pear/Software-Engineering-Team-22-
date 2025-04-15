from tkinter import *
# from photonDB import query_username  # Assuming you have a function to query usernames
from player import Player
import photonDB
import audio
from actionScreen import ActionScreen
s = Tk()

# Button class ----------------------------------------------------------------------------

# Sets up ---------------------------------------------------------------------------------
s.geometry('800x600')
s.configure(bg="#000000")
s.title("Entry Terminal")

# Title -------------------------------------------------------------------------------------
main_title = Label(s, text="Edit Current Game", font=("Terminal", 20, "bold"), bg="black", fg="indigo")
main_title.pack(side="top", pady=10)

# Create a canvas for the general layout ------------------------------------------------
canvas = Canvas(s, width=600, height=450, bg="grey")
canvas.pack()

# Make the red side
canvas.create_rectangle(0, 0, 300, 450, fill="dark red", outline="grey")
canvas.create_text(65, 15, text="Red Team", font=("Terminal", 15, "bold"), fill="#ff746c")

# Make the green side
canvas.create_rectangle(300, 0, 600, 450, fill="dark green", outline="grey")
canvas.create_text(375, 15, text="Green Team", font=("Terminal", 15, "bold"), fill="#CFFDBC")
# start function for the entry screen --------------------------------------------------------
def start(comms):
    # Store entries and username fields
    red_entries = []
    red_usernames = []
    green_entries = []
    green_usernames = []
    new_players = []
    new_player_count = 0
    equipment_id = []
    players = []
    class buttonID(Button):
        def __init__(self, root, id, col, text, command):
            super().__init__(root, text=text, command=self.on_button_click)
            self.id = id
            self.col = col
            self.command = command  
        
        def getID(self):
            return self.id  
        
        def on_button_click(self):
            if self.col == "red":
                entry = red_entries[self.id]  
                username_entry = red_usernames[self.id]  
            else:
                entry = green_entries[self.id]  
                username_entry = green_usernames[self.id]  
            
            player_id = entry.get()
            print(f"Button {self.getID()} clicked. Player ID: {player_id}")

            player = query_username(player_id)  
            print(f"Player codename: {player.getCodeName()}")
            username_entry.delete(0, END)
            username_entry.insert(0, player.getCodeName())
            player.setTeam(self.col)
            
            # make new window 
            newer = Toplevel(s)
            newer.geometry('300x300')
            newer.configure(bg="#FFFFFF")
            newer.title("Equipment ID")

            #create canvas 
            newercanvas = Canvas(newer, width=300, height=300, bg="white")
            newercanvas.pack()
            #text box to tell user what to do
            equpipmentprompt = Label(newer,text="Please Enter the Equipment ID")
            newercanvas.create_window(150,100,window=equpipmentprompt)
            #spot for new username 
            equipmentid = Entry(newer, width=10)
            newercanvas.create_window(150,150, window=equipmentid)
            def addedepuipmentid():
                equipment_id.append(equipmentid.get())
                player.setEquipmentId(equipment_id[-1])
                players.append(player)
                comms.sendEqpID(equipment_id[-1])
                newer.destroy()
            done = Button(newer, text="Submit", command=addedepuipmentid)
            newercanvas.create_window(150,200, window=done)
            newer.wait_window()
            
    # check entered id for username ----------------------------------------------------------
    def query_username(player_id):
        player = photonDB.queryId(player_id)
        if player.id == -1: #if player does not exist 
            new = Toplevel(s) # make pop up window
            new.geometry('300x300')
            new.configure(bg="#FFFFFF")
            new.title("Create New Player")

            # make a canvas 
            newcanvas = Canvas(new, width=300, height=300, bg="white")
            newcanvas.pack()
            
            #insert text to tell user to enter new username
            newcanvas.create_text(150,100,text="Please Enter New Username", fill="black")

            new_name = Entry(new, width=10)
            newcanvas.create_window(150,150, window=new_name)
            #function to add username 
            def added():
                new_players.append(new_name.get())
                player.setCodeName(new_players[-1])
                photonDB.addPlayer(player_id, new_players[-1])
                new.destroy()
            
            done = Button(new, text="Submit", command=added)
            newcanvas.create_window(150,200, window=done)
            new.wait_window()
            print(f"New players: {new_players}")
            if new_players:
                return player
            else:
                return ""
        else:
            return player
    
    #displaying the name and id boxes  ---------------------------------------------------------------------------------
    for i in range(15): #red user entry boxes 
        aentry = Entry(s, width=10)
        canvas.create_window(50, 40 + (i * 25), window=aentry)
        red_entries.append(aentry)

        username_entry = Entry(s, width=15)
        canvas.create_window(150, 40 + (i * 25), window=username_entry)
        red_usernames.append(username_entry)

        save_red = buttonID(s, i, "red", text="Save", command=None)
        canvas.create_window(260, 40 + (i * 25), window=save_red)
    
    for i in range(15): #green user entry boxes 

        entry = Entry(s, width=10)
        canvas.create_window(350, 40 + (i * 25), window=entry)
        green_entries.append(entry)

        username_entry = Entry(s, width=15)
        canvas.create_window(450, 40 + (i * 25), window=username_entry)
        green_usernames.append(username_entry)

        save_green = buttonID(s, i, "green", text="Save", command=None)
        canvas.create_window(560, 40 + (i * 25), window=save_green)

    # Button functions ----------------------------------------------------------------------------------------------------
    #place holder function for button 
    def do_nothing():
        print("Button Clicked")
    #clear function 
    def clear(): 
        for i in range(15): 
            red_entries[i].delete(0, END)
            green_entries[i].delete(0, END)
            red_usernames[i].delete(0, END)
            green_usernames[i].delete(0, END)
        players.clear()
        print("Clearing screen")
    #starting action screen 
    def startActionScreen():
        actionScreen = ActionScreen(60, comms)
        redCounter = 0
        greenCounter = 0

        for player in players:
            if player.getTeam() == "red":
                actionScreen.update_entries(player.getTeam(), redCounter, player.getCodeName(), player.getPoints())
                redCounter+=1
            if player.getTeam() == "green":
                actionScreen.update_entries(player.getTeam(), greenCounter, player.getCodeName(), player.getPoints())
                greenCounter+=1
        actionScreen.run()
    #window for changing the ip address 
    def changeIP(): 
        #create new window 
        ipbox = Toplevel(s)
        ipbox.geometry('300x300')
        ipbox.configure(bg="#FFFFFF")
        ipbox.title("Change IP Address")

        #make canvas for the window 
        ipcanvas = Canvas(ipbox, width=300, height=300, bg="white")
        ipcanvas.pack()

        #insert text to tell user to enter new username
        ipcanvas.create_text(150,100,text="Please enter IP Adress: ", fill="black")

        #spot to input 
        ip_input = Entry(ipbox, width=10)
        ipcanvas.create_window(150,150, window=ip_input)

        def ip_entered():
            ipbox.destroy()
        #make submit button 
        submit = Button(ipbox, text='Submit', command=ip_entered)
        ipcanvas.create_window(150,200, window=submit)

    #canvas for the buttons 
    button_canvas = Canvas(s, width=800, height=100, bg='grey')
    button_canvas.pack(side='bottom')

    #button information 
    button_config = [
        ("F1\nStart\nGame", 160, startActionScreen, "<F1>"), ("F2\nChange\nIP Address", 410, changeIP, "<F2>"), ("F12\nClear\nGame",650 ,clear, "<F12>")
    ]

    #displaying buttons 
    for text, x_pos, func, key in button_config:
        btn = Button(s, text=text, command=func) #make button
        button_canvas.create_window(x_pos, 50, window=btn, width=100, height=80)
        s.bind(key, lambda event, f=func: f()) # bound to these keys
        

    s.mainloop()

