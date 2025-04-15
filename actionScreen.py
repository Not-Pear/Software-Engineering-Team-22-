import tkinter as tk
from PIL import Image, ImageTk
from tkinter import scrolledtext
import time

#from socketComms import SocketComms


class ActionScreen: 
    def __init__(self, initial_time, game_time):
        self.parent = tk.Tk()
        self.parent.title("Action Screen")
        #getting screen width and height of display
        self.width= self.parent.winfo_screenwidth() 
        self.height= self.parent.winfo_screenheight()
        #setting tkinter window size
        self.parent.geometry("%dx%d" % (self.width, self.height))  

        #self.comms = comms

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
        self.game_time = game_time
        self.remaining_game_time = game_time
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
            print("Before label update")
            self.time_label.config(text="Game Start!", fg="green")
            print("After label update")
            self.parent.after(30000, lambda: print("Starting game_Timer now..."))
            self.parent.after(30000, self.game_Timer)

            

    def game_Timer(self):
        if self.remaining_game_time > 0 and self.remaining_time == 0:
            print("Inside game Timer")
            minutes, seconds = divmod(self.remaining_game_time, 60)
            self.time_label.config(text=f"Time Remaining: {minutes:02}:{seconds:02}", fg="black")
            self.remaining_game_time -= 1
            self.parent.after(1000, self.game_Timer)  # Use self.parent.after
        elif self.remaining_game_time == 0:
            self.time_label.config(text="Game Over!", fg="red")
            #self.comms.sendStart()
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
        # self.update_entries("green", 0, self.test_teams[0], 0)  #testing
        # self.update_entries("red", 0, self.test_teams[1], 50)
        #self.update_entries("green", 0, "Tom", 0)

        self.parent.mainloop()
    def destroy(self):
        self.parent.destroy