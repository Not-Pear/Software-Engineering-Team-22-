import tkinter as tk
from PIL import Image, ImageTk
from tkinter import scrolledtext
from socketComms import SocketComms
 

class ActionScreen: 
    def __init__(self, initial_time, comms):
        self.parent = tk.Tk()
        self.parent.title("Action Screen")
        self.parent.attributes('-fullscreen', True)
        
        self.comms = comms

        self.action_text_box = tk.Text(self.parent)
        self.action_text_box = scrolledtext.ScrolledText(self.parent, height = 5, width = 50, wrap = "word")
        self.action_text_box.pack(side = tk.BOTTOM,padx = 20, pady = 20)

        # Create frames for Green Team (Right) and Red Team (Left)
        self.red_team_frame = tk.Frame(self.parent)
        self.red_team_frame.pack(side=tk.LEFT, padx=20, pady=20)
        self.red_team_score_frame = tk.Frame(self.parent)
        self.red_team_score_frame.pack(side=tk.LEFT, padx=20, pady=20)


        self.green_team_score_frame = tk.Frame(self.parent)
        self.green_team_score_frame.pack(side=tk.RIGHT, padx=20, pady=20)
        self.green_team_frame = tk.Frame(self.parent)
        self.green_team_frame.pack(side=tk.RIGHT, padx=20, pady=20)


        self.green_text_boxes = {}
        self.test_teams = ["Bob", "Jimbob", "Jimmybimbob"]

        for i in range(15):
            self.green_player_score_label = tk.Label(self.green_team_score_frame, text=f"Score:", fg = "green")
            self.green_player_score_label.grid(row=i, column=0, padx=5, pady=2, sticky="w")  # Align left
            self.green_textbox_scores = tk.Entry(self.green_team_score_frame, width = 15)
            self.green_textbox_scores.grid(row = i, column = 1)
            self.green_textbox_scores.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

            self.green_player_label = tk.Label(self.green_team_frame, text=f"Player {i+1}:", fg = "green")
            self.green_player_label.grid(row=i, column=0, padx=5, pady=2, sticky="w")  # Align left
            self.green_textbox_codename = tk.Entry(self.green_team_frame, width = 15)
            self.green_textbox_codename.grid(row = i, column = 1)
            self.green_textbox_codename.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

            self.green_text_boxes[i] = (self.green_textbox_codename, self.green_textbox_scores)   #Codename, score
            


        self.red_text_boxes = {}
        for j in range(15):
            self.red_player_label = tk.Label(self.red_team_frame, text=f"Player {j+1}:", fg = "red")
            self.red_player_label.grid(row=j, column=0, padx=5, pady=2, sticky="w")  # Align left


            self.red_textbox_codename = tk.Entry(self.red_team_frame, width = 15)
            self.red_textbox_codename.grid(row = j, column = 1)
            self.red_textbox_codename.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")


            self.red_player_score_label = tk.Label(self.red_team_score_frame, text=f"Score:", fg = "red")
            self.red_player_score_label.grid(row=j, column=0, padx=5, pady=2, sticky="w")  # Align left
            self.red_textbox_scores = tk.Entry(self.red_team_score_frame, width = 15)   #Scores box
            self.red_textbox_scores.grid(row = j, column = 1)
            self.red_textbox_scores.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

            self.red_text_boxes[j] = (self.red_textbox_codename, self.red_textbox_scores) #Codename, Score

    


        self.initial_time = initial_time
        self.remaining_time = initial_time
        self.is_running = True
        self.time_label = tk.Label(self.parent, text="00:00", font=("Helvetica", 15))
        self.time_label.pack(side = tk.BOTTOM, pady=20)

        self.count = 0

    def testAutoScrollTxtBox(self):
        global count
        self.count = self.count + 1
        self.action_text_box.insert(tk.END, f'Testing Autoscroll Text Box, Value = {self.count}\n')
        self.action_text_box.see(tk.END) #What scrolls to the end
        self.parent.after(1000, self.testAutoScrollTxtBox)

    def countdown(self):
        if self.is_running and self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.time_label.config(text=f"Time Remaining: {minutes:02}:{seconds:02}")
            self.remaining_time -= 1
            self.parent.after(1000, self.countdown)  # Use self.parent.after
        elif self.remaining_time == 0:
            self.time_label.config(text="Game Start!", fg="green")
            self.comms.sendStart()
            self.is_running = False

    def update_entries(self, team, player_num, new_name=None, new_score=None):
        if team == "green" and player_num in self.green_text_boxes:
            # self.green_textbox_scores.config(state = NORMAL)
            codename, score = self.green_text_boxes[player_num]   #codename is codename entry, score is score entry
            if new_name is not None:
                codename.config(state="normal")  # Enable editing
                codename.delete(0, tk.END)
                codename.insert(0, new_name)
                codename.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")  # Enable editing
            if new_score is not None:
                score.config(state="normal")
                score.delete(0, tk.END)
                score.insert(0, new_score)
                score.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
        if team == "red" and player_num in self.red_text_boxes:
            codename, score = self.red_text_boxes[player_num]   #codename is codename entry, score is score entry
            if new_name is not None:
                codename.config(state="normal")
                codename.delete(0, tk.END)
                codename.insert(0, new_name)
                codename.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
            if new_score is not None:
                score.config(state="normal")
                score.delete(0, tk.END)
                score.insert(0, new_score)
                score.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

    def run(self):
        self.testAutoScrollTxtBox()
        self.countdown()
        self.update_entries("green", 0, self.test_teams[0], 0)  #testing
        self.update_entries("red", 0, self.test_teams[1], 50)
        
        self.parent.mainloop()
