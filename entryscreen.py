from tkinter import *
# from photonDB import query_username  # Assuming you have a function to query usernames
from Player import Player
import photonDB

s = Tk()

# Button class ----------------------------------------------------------------------------
class buttonID(Button):
    def __init__(self, root, id, col, text, command):
        super().__init__(root, text=text, command=self.on_button_click)  # Use self.on_button_click for the command
        self.id = id
        self.col = col
        self.command = command  # Optional: You can still pass the command if you want, otherwise handle internally
    
    def getID(self):
        return self.id  # Returns the button ID
    
    def on_button_click(self):
        # Retrieve the corresponding entry field and username field based on the button ID
        if self.col == "red":
            entry = red_entries[self.id]  # Access the correct entry field for red team
            username_entry = red_usernames[self.id]  # Access the correct username field for red team
        else:  # For green team
            entry = green_entries[self.id]  # Access the correct entry field for green team
            username_entry = green_usernames[self.id]  # Access the correct username field for green team
        
        player_id = entry.get()  # Get the player ID from the entry field
        print(f"Button {self.getID()} clicked. Player ID: {player_id}")

        # Query for the username (mock query function for example)
        username = query_username(player_id)  # Use your database query function
        
        # Insert the retrieved username into the correct column
        username_entry.delete(0, END)  # Clear previous text
        username_entry.insert(0, username)  # Insert new username

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

# Store entries and username fields
red_entries = []
red_usernames = []
green_entries = []
green_usernames = []
new_players = []


# Mock function for querying username (Replace this with real database query)
def query_username(player_id):
	player = photonDB.queryId(player_id)
	if player.id == -1:
		new = Tk()
		new.geometry('200x200')
		new.configure(bg = "#FFFFFF")
		new.title("Create New Player")
		
		new_name = Entry(new, width=10)
		new_name.pack()
		
		def added():
			new_players.append(new_name.get())
			new.destroy()
			
		done = Button(new, text = "Okay", command = added)
		done.pack()
		new.wait_window()
		print(f"printing", new_players[-1])
		photonDB.addPlayer(player_id, new_players[-1])
		if new_players:
			return new_players[-1]
		else:
			return ''
	else:
		return player.codename if player.codename else ''

# Create red team input fields and buttons
for i in range(20):
    entry = Entry(s, width=10)
    canvas.create_window(50, 40 + (i * 20), window=entry)
    red_entries.append(entry)

    username_entry = Entry(s, width=15)  # Username column
    canvas.create_window(150, 40 + (i * 20), window=username_entry)
    red_usernames.append(username_entry)

    save_red = buttonID(s, i, "red", text="Save", command=None)
    canvas.create_window(230, 40 + (i * 20), window=save_red)

# Create green team input fields and buttons
for i in range(20):
    entry = Entry(s, width=10)
    canvas.create_window(300, 40 + (i * 20), window=entry)
    green_entries.append(entry)

    username_entry = Entry(s, width=15)  # Username column
    canvas.create_window(400, 40 + (i * 20), window=username_entry)
    green_usernames.append(username_entry)

    save_green = buttonID(s, i, "green", text="Save", command=None)
    canvas.create_window(475, 40 + (i * 20), window=save_green)

# Bottom buttons -------------------------------------------------------------------------
def do_nothing():
    print("Button Clicked")

button_config = [
    ("F1\nEdit\nGame", 0), ("F2\nGame\nParameters", 70), ("F3\nStart\nGame", 140),
    ("F5\nPreEntered\nGames", 280), ("F7\n", 420), ("F8\nView\nGame", 490),
    ("F10\nFlick\nSync", 630), ("F12\nClear\nGame", 730)
]

for text, x_pos in button_config:
    btn = Button(s, text=text, bg="black", fg="green", command=do_nothing)
    btn.place(x=x_pos, y=520, width=70, height=80)

s.mainloop()
