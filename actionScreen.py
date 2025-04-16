import tkinter as tk
from PIL import Image, ImageTk
from tkinter import scrolledtext
import time
from audio import *

#from socketComms import SocketComms


class ActionScreen: 
    def __init__(self, initial_time, game_time, comms, players):
        self.parent = tk.Tk()
        self.parent.title("Action Screen")
        #getting screen width and height of display
        self.width= self.parent.winfo_screenwidth() 
        self.height= self.parent.winfo_screenheight()
        #setting tkinter window size
        self.parent.geometry("%dx%d" % (1000, 800))  
        self.parent.config(bg = 'black')

        self.comms = comms
        comms.setActionScreen(self)

        self.action_text_box = tk.Text(self.parent)
        self.action_text_box = scrolledtext.ScrolledText(self.parent, height = 5, width = 50, wrap = "word")
        self.action_text_box.pack(side = tk.BOTTOM,padx = 20, pady = 20)

        self.red_team_container = tk.Frame(self.parent, highlightbackground="red", highlightthickness=2, bg = 'black') # main container that is being moved and all textboxes are beint stored
        self.red_team_container.pack(side=tk.LEFT, padx=20, pady=20)

        self.red_team_label = tk.Label(self.red_team_container, text="Red Team", font=("Helvetica", 16, "bold"), fg="red", bg = 'black')
        self.red_team_label.pack()

        self.red_team_total_score_label = tk.Label(self.red_team_container, text="Total Score: ", font=("Helvetica", 8, "normal"), fg="red", bg = 'black')
        self.red_team_total_score_label.pack()
        self.red_team_total_score = tk.Entry(self.red_team_container, width = 15)
        self.red_team_total_score.insert(0, "0")
        self.red_team_total_score.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

        self.red_team_total_score.pack(pady = 10)

        
        #self.red_team_score = tk.Label(self.red_team_container, text="Red Team Score: ", font=("Helvetica", 16, "bold"), fg="red", bg = 'black')

        self.red_team_frame = tk.Frame(self.red_team_container, bg = 'black') # make it so that each box and frame are contained in another frame
        self.red_team_frame.pack(side=tk.LEFT, padx=(0, 10)) # slight gap between columns
        self.red_team_score_frame = tk.Frame(self.red_team_container, bg = 'black') 
        self.red_team_score_frame.pack(side=tk.LEFT)




        self.green_team_container = tk.Frame(self.parent, highlightbackground="green", highlightthickness=2, bg = 'black')
        self.green_team_container.pack(side=tk.RIGHT, padx=20, pady=20)

        self.green_team_label = tk.Label(self.green_team_container, text="Green Team", font=("Helvetica", 16, "bold"), fg="green", bg = 'black')
        self.green_team_label.pack()

        self.green_team_total_score_label = tk.Label(self.green_team_container, text="Total Score: ", font=("Helvetica", 8, "normal"), fg="green", bg = 'black')
        self.green_team_total_score_label.pack()
        self.green_team_total_score = tk.Entry(self.green_team_container, width = 15)
        self.green_team_total_score.insert(0, "0")
        self.green_team_total_score.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
        self.green_team_total_score.pack(pady = 10)

        self.green_team_frame = tk.Frame(self.green_team_container, bg = 'black') # make it so that each box and frame are contained in another frame
        self.green_team_frame.pack(side=tk.LEFT, padx=(10, 0)) # slight gap between columns
        self.green_team_score_frame = tk.Frame(self.green_team_container, bg = 'black') 
        self.green_team_score_frame.pack(side=tk.LEFT)



        self.green_text_boxes = {}
        self.test_teams = ["Bob", "Jimbob", "Jimmybimbob"]

        for i in range(15):
            self.green_player_score_label = tk.Label(self.green_team_score_frame, text=f"Score:", fg = "green", bg = 'black')
            self.green_player_score_label.grid(row=i, column=0, padx=5, pady=2, sticky="w")  # Align left
            self.green_textbox_scores = tk.Entry(self.green_team_score_frame, width = 15)
            self.green_textbox_scores.grid(row = i, column = 1, padx = 20, pady= 5)
            self.green_textbox_scores.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

            self.green_player_label = tk.Label(self.green_team_frame, text=f"Player {i+1}:", fg = "green", bg = 'black')
            self.green_player_label.grid(row=i, column=0, padx=5, pady=2, sticky="w")  # Align left
            self.green_textbox_codename = tk.Entry(self.green_team_frame, width = 15)
            self.green_textbox_codename.grid(row = i, column = 1, pady= 5)
            self.green_textbox_codename.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

            self.green_text_boxes[i] = (self.green_textbox_codename, self.green_textbox_scores)   #Codename, score
        

        # self.red_team_label = tk.Label(self.red_team_frame, text=f"Red Team:", fg = "red")
        # self.red_team_label.pack(padx=20, pady=20)
        self.red_text_boxes = {}
        for j in range(15):
            self.red_player_label = tk.Label(self.red_team_frame, text=f"Player {j+1}:", fg = "red", bg = 'black')
            self.red_player_label.grid(row=j, column=0, padx=5, pady=2, sticky="w")  # Align left


            self.red_textbox_codename = tk.Entry(self.red_team_frame, width = 15, bg = 'black')
            self.red_textbox_codename.grid(row = j, column = 1, pady= 5)
            self.red_textbox_codename.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")


            self.red_player_score_label = tk.Label(self.red_team_score_frame, text=f"Score:", fg = "red", bg = 'black')
            self.red_player_score_label.grid(row=j, column=0, padx=5, pady=2, sticky="w")  # Align left
            self.red_textbox_scores = tk.Entry(self.red_team_score_frame, width = 15)   #Scores box
            self.red_textbox_scores.grid(row = j, column = 1, padx = 20, pady= 5)
            self.red_textbox_scores.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

            self.red_text_boxes[j] = (self.red_textbox_codename, self.red_textbox_scores) #Codename, Score


        self.initial_time = initial_time
        self.remaining_time = initial_time
        self.game_time = game_time
        self.remaining_game_time = game_time
        self.is_running = True
        #make end button
        self.endgame = tk.Button(self.parent, text="END GAME", command=self.destroy)  
        self.endgame.pack(side = tk.BOTTOM, pady=(10,0))
        self.time_label = tk.Label(self.parent, text="00:00", font=("Helvetica", 15), fg = 'white', bg = 'black')
        self.time_label.pack(side = tk.BOTTOM, pady=5)

        self.count = 0
        self.players = players
        
        self.red_total_score = 0
        self.green_total_score = 0

      

    def testAutoScrollTxtBox(self):
        global count
        self.count = self.count + 1
        #self.action_text_box.insert(tk.END, f'Testing Autoscroll Text Box, Value = {self.count}\n')
        self.action_text_box.see(tk.END) #What scrolls to the end
        self.parent.after(1000, self.testAutoScrollTxtBox)
        
    def getPlayerByID(self, searchEqID):
        for p in self.players:
            if (p.getequipmentid() == searchEqID):
                return p

    def countdown(self):
        if self.is_running and self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.time_label.config(text=f"Time Remaining: {minutes:02}:{seconds:02}")
            self.remaining_time -= 1
            self.parent.after(1000, self.countdown)  # Use self.parent.after
        elif self.remaining_time == 0:
            self.time_label.config(text="Game Start!", fg="green")
            self.parent.after(2000, lambda: print("Starting game_Timer now..."))
            self.parent.after(2000, self.game_Timer)
            self.parent.after(2000, self.comms.sendStart)
            self.parent.after(2000, playAudio)

            

    def game_Timer(self):
        if self.remaining_game_time > 0 and self.remaining_time == 0:
            minutes, seconds = divmod(self.remaining_game_time, 60)

            self.time_label.config(text=f"Game Time: {minutes:02}:{seconds:02}", fg="white")
            self.remaining_game_time -= 1
            self.parent.after(1000, self.game_Timer)  # Use self.parent.after
        elif self.remaining_game_time == 0:
            self.time_label.config(text="Game Over!", fg="red")
            self.comms.sendEnd()
            stopAudio()
            self.is_running = False

    def update_entries(self, team, player_num, new_name=None, new_score=None, baseHit = False):
        if team == "green" and player_num in self.green_text_boxes:
            # self.green_textbox_scores.config(state = NORMAL)
            codename, score = self.green_text_boxes[player_num]   #codename is codename entry, score is score entry
            if baseHit:
                print("In green base")
                temp_name = "B " + codename.get()
                codename.config(state = "normal")
                codename.delete(0, tk.END)
                codename.insert(0, temp_name)
                codename.config(bg = "green")
                codename.config(state = "disabled", disabledbackground = "green", disabledforeground = "black")
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
            if baseHit:
                print("In red base")
                temp_name = "B " + codename.get()
                codename.config(state = "normal")
                codename.delete(0, tk.END)
                codename.insert(0, temp_name)
                codename.config(bg = "red")
                codename.config(state = "disabled", disabledbackground = "red", disabledforeground = "black")
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

# takes global variable of total scores and adds new score to it
    def update_scores(self, team, new_score):
        if team == "red":
            self.red_total_score = self.red_total_score + new_score
            self.red_team_total_score.config(state = "normal")
            self.red_team_total_score.delete(0, tk.END)
            self.red_team_total_score.insert(0, self.red_total_score)
            self.red_team_total_score.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")
        elif team == "green":
            self.green_total_score = self.green_total_score + new_score

            self.green_team_total_score.config(state = "normal")
            self.green_team_total_score.delete(0, tk.END)
            self.green_team_total_score.insert(0, self.green_total_score)
            self.green_team_total_score.config(state = "disabled", disabledbackground = "white", disabledforeground = "black")

    def run(self):
        self.testAutoScrollTxtBox()
        self.countdown()
        self.parent.mainloop()

    def destroy(self):
        self.parent.destroy()  

