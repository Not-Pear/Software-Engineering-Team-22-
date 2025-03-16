from tkinter import *
# from photonDB import query_username  # Assuming you have a function to query usernames
from player import Player
import photonDB

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
canvas = Canvas(s, width=500, height=450, bg="grey")
canvas.pack()

# Make the red side
canvas.create_rectangle(0, 0, 250, 500, fill="dark red", outline="grey")
canvas.create_text(125, 15, text="Red Team", font=("Terminal", 15, "bold"), fill="#ff746c")

# Make the green side
canvas.create_rectangle(250, 0, 500, 450, fill="dark green", outline="grey")
canvas.create_text(375, 15, text="Green Team", font=("Terminal", 15, "bold"), fill="#CFFDBC")

def start(comms):
    # Store entries and username fields
    red_entries = []
    red_usernames = []
    green_entries = []
    green_usernames = []
    new_players = []
    new_player_count = 0
    equipment_id = []
    
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

            username = query_username(player_id)  
            username_entry.delete(0, END)
            username_entry.insert(0, username)

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
                newer.destroy()
            done = Button(newer, text="Submit", command=addedepuipmentid)
            newercanvas.create_window(150,200, window=done)
            newer.wait_window()
            comms.send(player_id, equipment_id[-1])
            
    
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
            def added():
                new_players.append(new_name.get())
                photonDB.addPlayer(player_id, new_players[-1])
                new.destroy()
            
            done = Button(new, text="Submit", command=added)
            newcanvas.create_window(150,200, window=done)
            new.wait_window()
            print(f"New players: {new_players}")
            if new_players:
                return new_players[-1]
            else:
                return ""
        else:
            return player.codename if player.codename else ""
    
    for i in range(20):
        aentry = Entry(s, width=10)
        canvas.create_window(50, 40 + (i * 20), window=aentry)
        red_entries.append(aentry)

        username_entry = Entry(s, width=15)
        canvas.create_window(150, 40 + (i * 20), window=username_entry)
        red_usernames.append(username_entry)

        save_red = buttonID(s, i, "red", text="Save", command=None)
        canvas.create_window(230, 40 + (i * 20), window=save_red)
    
    for i in range(20):
        entry = Entry(s, width=10)
        canvas.create_window(300, 40 + (i * 20), window=entry)
        green_entries.append(entry)

        username_entry = Entry(s, width=15)
        canvas.create_window(400, 40 + (i * 20), window=username_entry)
        green_usernames.append(username_entry)

        save_green = buttonID(s, i, "green", text="Save", command=None)
        canvas.create_window(475, 40 + (i * 20), window=save_green)
    
    def do_nothing():
        print("Button Clicked")
    def clear(): 
        print("Clearing screen")

    button_config = [
        ("F1\nEdit\nGame", 0,do_nothing, "<F1>"), ("F2\nGame\nParameters", 70,do_nothing, "<F2>"), ("F3\nStart\nGame", 140,do_nothing, "<F3>"),
        ("F5\nPreEntered\nGames", 280,do_nothing, "<F5>"), ("F7\n", 420,do_nothing, "<F7>"), ("F8\nView\nGame", 490,do_nothing, "<F8>"),
        ("F10\nFlick\nSync", 630,do_nothing, "<F10>"), ("F12\nClear\nGame", 730,clear, "<F12>")
    ]

    for text, x_pos, func, key in button_config:
        btn = Button(s, text=text, bg="black", fg="green", command=func) #make button
        btn.place(x=x_pos, y=520, width=70, height=80) #in this specific spot
        s.bind(key, lambda event, f=func: f()) # bound to these keys
        

    s.mainloop()

