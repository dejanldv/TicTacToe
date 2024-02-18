import turtle
import math

# function that will draw tic-tac-toe board using 2 for loops
def drawBoard():
    # drawing horizontal lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-150, 50 - 100*i)
        drawer.pendown()
        drawer.forward(300)

    drawer.right(90)

    # drawing vertical lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-50 + 100*i, 150)
        drawer.pendown()
        drawer.forward(300)

    # writing field number in top left corner of each board field
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-140 + 100*j, 125 - 100*i)
            drawer.pendown()
            drawer.write(num, font=("Arial", 11))
            num +=1

    screen.update()


# functions that creates 2D list for keeping track of player moves
def makeboard():
    global board
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(' ')
        board.append(row)



# draws X in correct position on board
def drawX(x,y):
    drawer.penup()
    drawer.goto(x,y)
    drawer.pendown()

    drawer.setheading(60)

    for i in range(2):
        drawer.forward(35)
        drawer.backward(70)
        drawer.forward(35)
        drawer.left(60)

    screen.update()


# draws O in correct position on board
def drawO(x,y):
    drawer.penup()
    drawer.goto(x, y + 30)
    drawer.pendown()

    drawer.setheading(0)
    for i in range(180):
        drawer.forward((60 * math.pi)/180)
        drawer.right(2)
    
    screen.update()


# activating event listeners (when key (1-9) is pressed)
def activate(functions):
    for i in range(9):
        screen.onkey(functions[i], str(i+1))
    screen.onscreenclick(screenClick)



# deactivating all event listeners
def deactivate():
    for i in range(9):
        screen.onkey(None, str(i+1))
        screen.onscreenclick(None)


# adding X to the correct position on board (when clicked or inputed by keyboard)
def addX(row, column):
    global turn_counter
    
    # checking if game is a tie if turn counter is 9 and there is no winner
    if turn_counter > 8:
        announcer.goto(-50, 200)
        announcer.write("It's a tie!", font=("Arial", 18))
        turtle.ontimer(restart, t= 1000)

    turn_counter +=1

    announcer.clear()
    
    # checking if position is taken
    if board[row][column] != ' ':
        announcer.write("That spot is taken", font=("Arial", 18))
        screen.update()
    else:
        drawX(-100 + 100 * column, 100 - 100 * row)

        # adding X to correct board position in board list
        board[row][column] = 'x'

    # checking for a winner, and deactivating event listeners if there is a winner
    if checkWinner('x'):
        global score_X, score_O
        announcer.goto(-50,200)
        announcer.write("You Won!", font=("Ariel", 18))
        score_X +=1
        score.clear()
        score.write('X: ' + str(score_X) + '\n' + "O: " + str(score_O), font=("Arial Bold", 12))
        
        screen.update()
        deactivate()
        turtle.ontimer(restart, t= 1000)

    else:
        # checking if game is a tie if turn counter is 9 and there is no winner
        if turn_counter > 8:
            announcer.goto(-50, 200)
            announcer.write("It's a tie!", font=("Arial", 18))
            turtle.ontimer(restart, t= 1000)

        # if X hasn't won, O will play
        addO()
        turn_counter +=1
        print(turn_counter)
        # checking if O won
        if checkWinner('o'):
            announcer.goto(-50, 200)
            announcer.write("You lost!", font=("Arial", 18))
            score_O += 1
            score.clear()
            score.write('X: ' + str(score_X) + '\n' + "O: " + str(score_O), font=("Arial Bold", 12))

            screen.update()
            deactivate()
            turtle.ontimer(restart, t= 1000)

def addO():
    # checking if there if available spot for three O's in a row
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'
                if checkWinner('o'):
                    drawO(-100 + 100*j, 100 - 100*i)
                    return
                board[i][j] = ' '
    
    # checking if there is available spot for blocking X
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'x'
                if checkWinner('x'):
                    board[i][j] = 'o'
                    drawO(-100 + 100*j, 100 - 100*i)
                    return
                board[i][j] = ' '

    # putting O in a first available position on board
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'o'
                drawO(-100 + 100*j, 100 - 100*i)
                return


# function that will check if there is a winner
def checkWinner(mark):
    for i in range(3):
        # checking if there are three in a row vertically
        if board[0][i] == board[1][i] == board[2][i] == mark: return True

        # checking if there are three in a row horizontally
        if board[i][0] == board[i][1] == board[i][2] == mark: return True

        # checking if there are three in a row diagonally
        if board[0][0] == board[1][1] == board[2][2] == mark: return True
        if board[0][2] == board[1][1] == board[2][0] == mark: return True
    return False



# functions for event listeners (key-press (1-9))
def squareOne():
    addX(0,0)
def squareTwo():
    addX(0,1)
def squareThree():
    addX(0,2)
def squareFour():
    addX(1,0)
def squareFive():
    addX(1,1)
def squareSix():
    addX(1,2)
def squareSeven():
    addX(2,0)
def squareEight():
    addX(2,1)
def squareNine():
    addX(2,2)



# function for event listener (mouse-click)
def screenClick(x,y):
    board_fields = {
                    1: (-145, -55, 145, 55), 2: (-45, 45, 145, 55), 3: (55, 145, 145, 55),
                    4: (-145, -55, 45, -45), 5: (-45, 45, 45, -45), 6: (55, 145, 45, -45),
                    7: (-145, -55, -55, -145), 8:(-45, 45, -55, -145), 9:(55, 145, -55, -145)
                    }

    for key, coor in board_fields.items():
        if coor[0] <= x <= coor[1] and coor[2] >= y >= coor[3]:
            functions[key-1]()
    

def restart():
    global turn_counter
    turn_counter = 0

    turtle.resetscreen()

    drawer.pensize(5)
    drawer.ht()

    announcer.penup()
    announcer.ht()
    announcer.goto(-50, 200)
    announcer.color('red')

    score.penup()
    score.goto(-235,200)
    score.ht()
    score.color('green')
    score.write('X: ' + str(score_X) + '\n' + "O: " + str(score_O), font=("Arial Bold", 12))

    screen = turtle.Screen()
    screen.tracer(0)
    screen.setup(500,500)

    drawBoard()
    makeboard()
    activate(functions)

    screen.update()


# list of event listener functions
functions = [squareOne, squareTwo, squareThree, 
            squareFour, squareFive, squareSix, 
            squareSeven, squareEight, squareNine]

score_X = 0
score_O = 0

# creating turtles
drawer = turtle.Turtle()
announcer = turtle.Turtle()
score = turtle.Turtle()

# setting up drawer turtle
drawer.pensize(5)
drawer.ht()

# setting up announcer turtle
announcer.penup()
announcer.ht()
announcer.goto(-50, 0)
announcer.color('red')

# setting up score turtle
score.penup()
score.ht()
score.goto(-235, 200)
score.color('green')
score.write('X: ' + str(score_X) + '\n' + "O: " + str(score_O), font=("Arial Bold", 12))

# setting up screen
screen = turtle.Screen()
screen.tracer(0)
screen.setup(500,500)


drawBoard()
makeboard()


activate(functions)
screen.listen()
turn_counter = 0

turtle.mainloop()