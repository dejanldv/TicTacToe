# TIC-TAC-TOE, classic board game made with Tkinter, with the possibility to choose between one or two players
# with three levels of difficulty (Easy, Normal, Hard)


import tkinter as tk
import tkinter.font as font
from tkinter import messagebox
import random

# defining class TicTacToe as a Tkinter child class
class TicTacToe(tk.Tk):
    X, O, blank = 'X', 'O', ''              # field markings
    currentPlayer, nextPlayer = X, O    
    turn_counter = 0
    players = 1                             # number of players
    difficulty = 'normal'                   # level of difficulty
    fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]    # empty fields on board
    buttons = {}                            # dictionary with number 1-9 as keys and board fields (buttons) as values
    move = None                             # move made by computer
    p1_score, p2_score = 0, 0               # player's scores
    
    # player and button colors
    color_X = '#483D8B'
    color_O = '#8B3A62'
    sunken = '#668B8B'
    raised = '#AEEEEE'

    
    # initializing tkinter object
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # defining app window
        self.geometry('400x500')
        self.title('TicTacToe Game')
        self.resizable = (False, False)

        self.myFont = font.Font(family='Arial', size=30)    # font for board markings
        self.pixel = tk.PhotoImage(width=1, height=1)       # adding 1px image so that tkinter will calculate sizes in pixels

        # defining app frames (menu, game and score frames)
        self.menu_frame = tk.Frame(width=400, height=100, bg='#CAE1FF')
        self.menu_frame.pack()
        self.game_frame = tk.Frame(width=400, height=250, bg='#CAE1FF')
        self.game_frame.pack(pady=15)
        self.score_frame = tk.Frame(width=400, height=150, bg='#CAE1FF')
        self.score_frame.pack()
        # self.buttons = {}
        
        # menu buttons
        self.new_game = tk.Button(self.menu_frame, height=25, width=75, text='New Game', font='Arial 11', bg='#4682B4', fg='white', image=self.pixel, compound='center', command=self.newGame)
        self.new_game.grid(row=0, column=0, padx= 5, pady= 5)
        self.exit = tk.Button(self.menu_frame, height=25, width=75, text='Quit', font='Arial 11', bg='#4682B4', fg='white', image=self.pixel, compound='center', command=self.exit)
        self.exit.grid(row=0, column=2, padx=5, pady=5)

        # number of players buttons
        self.b_1player = tk.Button(self.menu_frame, height= 25, width= 75,text= '1 Player', font='Arial, 11', image=self.pixel, compound='center', bg=self.sunken, relief='sunken', command=self.players_1)
        self.b_1player.grid(row=1, column=0, padx=10, pady=10)
        self.b_2players = tk.Button(self.menu_frame, height= 25, width= 75, text= '2 Players', font='Arial, 11', image=self.pixel, compound='center', bg=self.raised, relief='raised', command=self.players_2)
        self.b_2players.grid(row=1, column=2, padx=10, pady=10)

        # level of difficulty buttons
        self.easy = tk.Button(self.menu_frame, height= 25, width= 60, text='Easy', font='Arial, 11', image=self.pixel, compound='center', bg=self.raised, relief='raised', command=self.easy_dif)
        self.easy.grid(row=2, column=0, padx=5, pady=10)
        self.normal = tk.Button(self.menu_frame, height= 25, width= 60, text='Normal', font='Arial, 11', image=self.pixel, compound='center', bg=self.sunken, relief='sunken', command=self.normal_dif)
        self.normal.grid(row=2, column=1, padx=5, pady=10)
        self.hard = tk.Button(self.menu_frame, height= 25, width= 60, text='Hard', font='Arial, 11', image=self.pixel, compound='center', bg=self.raised, relief='raised', command=self.hard_dif)
        self.hard.grid(row=2, column=2, padx=5, pady=10)

        # move number and scoreboard
        self.counter = tk.Label(self.score_frame, text='Move: ' + str(self.turn_counter), font='Arial 10 bold', bg='#CAE1FF')
        self.counter.grid(row=3, column=1)
        self.player1 = tk.Label(self.score_frame, text='Player1 (X): ' + str(self.p1_score), font='Arial 10 bold', bg='#CAE1FF')
        self.player1.grid(row=4, column=1)
        self.player2 = tk.Label(self.score_frame, text='Player2 (O): ' + str(self.p2_score), font='Arial 10 bold', bg='#CAE1FF')
        self.player2.grid(row=5, column=1)

        # defining 3x3 board, filled with buttons as board fields;
        # key is used to set dictionary keys to numbers 1-9 with appropriate buttons as values
        key = 1
        for row in range(3):
            self.game_frame.grid_rowconfigure(row, weight=1)
            for column in range(3):
                self.game_frame.grid_columnconfigure(column, weight=1)
                button_key = key + row + column
                self.buttons[button_key] = tk.Button(self.game_frame, text = "", font=self.myFont, image=self.pixel, compound='center', width=70, height=70, bg='#CDB7B5', command=lambda idx = button_key:self.play_field(idx))
                self.buttons[button_key].grid(row=row, column=column)
            key+=2
    
    # setting up number of players variable, and button appereance
    def players_1(self):
        self.b_1player.config(relief='sunken', bg=self.sunken)
        self.b_2players.config(relief='raised', bg=self.raised)
        self.players = 1

    
    
    def players_2(self):
        self.b_1player.config(relief='raised', bg=self.raised)
        self.b_2players.config(relief='sunken', bg=self.sunken)
        self.players = 2


    # setting up level of difficulty variable, and button appereance
    def easy_dif(self):
        self.easy.config(relief='sunken', bg=self.sunken)
        self.normal.config(relief='raised', bg=self.raised)
        self.hard.config(relief='raised', bg=self.raised)
        self.difficulty = 'easy'



    def normal_dif(self):
        self.easy.config(relief='raised', bg=self.raised)
        self.normal.config(relief='sunken', bg=self.sunken)
        self.hard.config(relief='raised', bg=self.raised)
        self.difficulty = 'normal'



    def hard_dif(self):
        self.easy.config(relief='raised', bg=self.raised)
        self.normal.config(relief='raised', bg=self.raised)
        self.hard.config(relief='sunken', bg=self.sunken)
        self.difficulty = 'hard'


    # checking if there is a winner (returning True if there is)
    def isWinner(self):
        return(self.buttons[1]['text'] == self.buttons[2]['text'] == self.buttons[3]['text'] == self.currentPlayer or
               self.buttons[4]['text'] == self.buttons[5]['text'] == self.buttons[6]['text'] == self.currentPlayer or
               self.buttons[7]['text'] == self.buttons[8]['text'] == self.buttons[9]['text'] == self.currentPlayer or
               self.buttons[1]['text'] == self.buttons[4]['text'] == self.buttons[7]['text'] == self.currentPlayer or
               self.buttons[2]['text'] == self.buttons[5]['text'] == self.buttons[8]['text'] == self.currentPlayer or
               self.buttons[3]['text'] == self.buttons[6]['text'] == self.buttons[9]['text'] == self.currentPlayer or
               self.buttons[1]['text'] == self.buttons[5]['text'] == self.buttons[9]['text'] == self.currentPlayer or
               self.buttons[3]['text'] == self.buttons[5]['text'] == self.buttons[7]['text'] == self.currentPlayer)


    # checking if boards is full and game is a tie (if turn is 9 and there is no winner)
    def boardFull(self):
        if self.turn_counter == 9 and not self.isWinner():
            return True


    # setting up a new game from scratch
    def newGame(self):
        self.p1_score, self.p1_score = 0, 0
        self.reset()


    # reseting game board and turn counter
    def reset(self):
        for button in self.buttons.values():
            button.config(text=self.blank)
            self.fields = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.turn_counter = 0
            self.counter.config(text='Move: ' + str(self.turn_counter))
            self.player1.config(text='Player1 (X): ' + str(self.p1_score))
            self.player2.config(text='Player2 (O): ' + str(self.p2_score))


    # exiting the app
    def exit(self):
        self.destroy()


    # defining logic for normal level of difficulty (if there are two player marks in one row, column or diagonaly,
    # choose a move that will block it, else choose random available field on board)
    def normal_c(self, player):
        if self.buttons[1]['text'] == self.buttons[2]['text'] == player and self.buttons[3]['text'] == self.blank: 
            return 3
        elif self.buttons[2]['text'] == self.buttons[3]['text'] == player and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[3]['text'] == player and self.buttons[2]['text'] == self.blank:
            return 2
        elif self.buttons[4]['text'] == self.buttons[5]['text'] == player and self.buttons[6]['text'] == self.blank:
            return 6
        elif self.buttons[5]['text'] == self.buttons[6]['text'] == player and self.buttons[4]['text'] == self.blank:
            return 4
        elif self.buttons[4]['text'] == self.buttons[6]['text'] == player and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[7]['text'] == self.buttons[8]['text'] == player and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[8]['text'] == self.buttons[9]['text'] == player and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[7]['text'] == self.buttons[9]['text'] == player and self.buttons[8]['text'] == self.blank:
            return 8
        elif self.buttons[1]['text'] == self.buttons[4]['text'] == player and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[4]['text'] == self.buttons[7]['text'] == player and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[7]['text'] == player and self.buttons[4]['text'] == self.blank:
            return 4
        elif self.buttons[2]['text'] == self.buttons[5]['text'] == player and self.buttons[8]['text'] == self.blank:
            return 8
        elif self.buttons[5]['text'] == self.buttons[8]['text'] == player and self.buttons[2]['text'] == self.blank:
            return 2
        elif self.buttons[2]['text'] == self.buttons[8]['text'] == player and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[3]['text'] == self.buttons[6]['text'] == player and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[6]['text'] == self.buttons[9]['text'] == player and self.buttons[3]['text'] == self.blank:
            return 3
        elif self.buttons[3]['text'] == self.buttons[9]['text'] == player and self.buttons[6]['text'] == self.blank:
            return 6
        elif self.buttons[1]['text'] == self.buttons[5]['text'] == player and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[5]['text'] == self.buttons[9]['text'] == player and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[9]['text'] == player and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[3]['text'] == self.buttons[5]['text'] == player and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[5]['text'] == self.buttons[7]['text'] == player and self.buttons[3]['text'] == self.blank:
            return 3
        elif self.buttons[3]['text'] == self.buttons[7]['text'] == player and self.buttons[5]['text'] == self.blank:
            return 5
        else:
            return random.choice(self.fields)


    # defining logic for hard level of difficulty (first check if there are two computer marks in one row, column or
    # diagonaly, and if True, choose a move that will make it three in a row, else check if there are two player marks
    # in one row, column or diagonaly, and choose a move that will block it, else choose random available field on board)
    def hard_c(self, player):
        if player == "X":
            computer = "O"
        else: 
            computer = "X"

        if self.buttons[1]['text'] == self.buttons[2]['text'] == computer and self.buttons[3]['text'] == self.blank: 
            return 3
        elif self.buttons[2]['text'] == self.buttons[3]['text'] == computer and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[3]['text'] == computer and self.buttons[2]['text'] == self.blank:
            return 2
        elif self.buttons[4]['text'] == self.buttons[5]['text'] == computer and self.buttons[6]['text'] == self.blank:
            return 6
        elif self.buttons[5]['text'] == self.buttons[6]['text'] == computer and self.buttons[4]['text'] == self.blank:
            return 4
        elif self.buttons[4]['text'] == self.buttons[6]['text'] == computer and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[7]['text'] == self.buttons[8]['text'] == computer and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[8]['text'] == self.buttons[9]['text'] == computer and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[7]['text'] == self.buttons[9]['text'] == computer and self.buttons[8]['text'] == self.blank:
            return 8
        elif self.buttons[1]['text'] == self.buttons[4]['text'] == computer and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[4]['text'] == self.buttons[7]['text'] == computer and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[7]['text'] == computer and self.buttons[4]['text'] == self.blank:
            return 4
        elif self.buttons[2]['text'] == self.buttons[5]['text'] == computer and self.buttons[8]['text'] == self.blank:
            return 8
        elif self.buttons[5]['text'] == self.buttons[8]['text'] == computer and self.buttons[2]['text'] == self.blank:
            return 2
        elif self.buttons[2]['text'] == self.buttons[8]['text'] == computer and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[3]['text'] == self.buttons[6]['text'] == computer and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[6]['text'] == self.buttons[9]['text'] == computer and self.buttons[3]['text'] == self.blank:
            return 3
        elif self.buttons[3]['text'] == self.buttons[9]['text'] == computer and self.buttons[6]['text'] == self.blank:
            return 6
        elif self.buttons[1]['text'] == self.buttons[5]['text'] == computer and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[5]['text'] == self.buttons[9]['text'] == computer and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[9]['text'] == computer and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[3]['text'] == self.buttons[5]['text'] == computer and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[5]['text'] == self.buttons[7]['text'] == computer and self.buttons[3]['text'] == self.blank:
            return 3
        elif self.buttons[3]['text'] == self.buttons[7]['text'] == computer and self.buttons[5]['text'] == self.blank:
            return 5
        
        if self.buttons[1]['text'] == self.buttons[2]['text'] == player and self.buttons[3]['text'] == self.blank: 
            return 3
        elif self.buttons[2]['text'] == self.buttons[3]['text'] == player and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[3]['text'] == player and self.buttons[2]['text'] == self.blank:
            return 2
        elif self.buttons[4]['text'] == self.buttons[5]['text'] == player and self.buttons[6]['text'] == self.blank:
            return 6
        elif self.buttons[5]['text'] == self.buttons[6]['text'] == player and self.buttons[4]['text'] == self.blank:
            return 4
        elif self.buttons[4]['text'] == self.buttons[6]['text'] == player and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[7]['text'] == self.buttons[8]['text'] == player and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[8]['text'] == self.buttons[9]['text'] == player and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[7]['text'] == self.buttons[9]['text'] == player and self.buttons[8]['text'] == self.blank:
            return 8
        elif self.buttons[1]['text'] == self.buttons[4]['text'] == player and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[4]['text'] == self.buttons[7]['text'] == player and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[7]['text'] == player and self.buttons[4]['text'] == self.blank:
            return 4
        elif self.buttons[2]['text'] == self.buttons[5]['text'] == player and self.buttons[8]['text'] == self.blank:
            return 8
        elif self.buttons[5]['text'] == self.buttons[8]['text'] == player and self.buttons[2]['text'] == self.blank:
            return 2
        elif self.buttons[2]['text'] == self.buttons[8]['text'] == player and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[3]['text'] == self.buttons[6]['text'] == player and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[6]['text'] == self.buttons[9]['text'] == player and self.buttons[3]['text'] == self.blank:
            return 3
        elif self.buttons[3]['text'] == self.buttons[9]['text'] == player and self.buttons[6]['text'] == self.blank:
            return 6
        elif self.buttons[1]['text'] == self.buttons[5]['text'] == player and self.buttons[9]['text'] == self.blank:
            return 9
        elif self.buttons[5]['text'] == self.buttons[9]['text'] == player and self.buttons[1]['text'] == self.blank:
            return 1
        elif self.buttons[1]['text'] == self.buttons[9]['text'] == player and self.buttons[5]['text'] == self.blank:
            return 5
        elif self.buttons[3]['text'] == self.buttons[5]['text'] == player and self.buttons[7]['text'] == self.blank:
            return 7
        elif self.buttons[5]['text'] == self.buttons[7]['text'] == player and self.buttons[3]['text'] == self.blank:
            return 3
        elif self.buttons[3]['text'] == self.buttons[7]['text'] == player and self.buttons[5]['text'] == self.blank:
            return 5
        else:
           return random.choice(self.fields)


    # button action
    def play_field(self, key):
        # setting up current player color
        if self.currentPlayer == 'X':
            self.player_color = self.color_X
        else:
            self.player_color = self.color_O

        # validating if the chosen field is empty
        if self.buttons[key]["text"] != self.blank:
            return
        else:
            # marking a field according to chosen move, and removing that field from available fields list
            self.buttons[key].config(text=self.currentPlayer, fg=self.player_color)
            self.fields.remove(key)
            self.turn_counter+=1
            self.counter.config(text='Move: ' + str(self.turn_counter))

        # checking for a winner   
        if self.isWinner():
            messagebox.showinfo('Winner', self.currentPlayer + ' Won the game!')
            if self.currentPlayer == 'X':
                self.p1_score +=1
            else:
                self.p2_score +=1
            self.reset()

        # checking for a tied game  
        elif self.boardFull():
            messagebox.showinfo('Board Full', 'The game is a tie!')
            self.reset()

        # switching player's turns
        self.currentPlayer, self.nextPlayer = self.nextPlayer, self.currentPlayer
        
        # checking if there is only one human player, and if there are available fields on board
        if self.players == 1 and len(self.fields) > 0:
            self.after(600, self.comp_turn)


    # defining computer move
    def comp_turn(self):
        self.turn_counter+=1
        self.counter.config(text='Move: ' + str(self.turn_counter))
        
        # setting up current player color
        if self.currentPlayer == 'X':
            self.player_color = self.color_X
        else:
            self.player_color = self.color_O

        # choosing a move according to the chosen difficulty
        if self.difficulty == 'easy':
            self.move = random.choice(self.fields)
            self.buttons[self.move].config(text = self.currentPlayer, fg=self.player_color)
            self.fields.remove(self.move)
        
        elif self.difficulty == 'normal':
            self.move = self.normal_c(self.nextPlayer)
            self.buttons[self.move].config(text = self.currentPlayer, fg=self.player_color)
            self.fields.remove(self.move)

        elif self.difficulty == 'hard':
            self.move = self.hard_c(self.nextPlayer)
            self.buttons[self.move].config(text = self.currentPlayer, fg=self.player_color)
            self.fields.remove(self.move)
        
        # checking for a winner
        if self.isWinner():
            messagebox.showinfo('Winner', self.currentPlayer + ' Won the game!')
            if self.currentPlayer == 'X':
                self.p1_score +=1
            else:
                self.p2_score +=1
            self.reset()
            
        # checking for a tied game
        elif self.boardFull():
            messagebox.showinfo('Board Full!', 'The game is a tie!')
            self.reset()

        # switching player's turns
        self.currentPlayer, self.nextPlayer = self.nextPlayer, self.currentPlayer


# initializing game object and starting the app
window = TicTacToe()
window.config(bg='#CAE1FF')
window.mainloop()