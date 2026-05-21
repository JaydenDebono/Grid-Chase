#Sets Title
title = "Grid Chase"

import random

# Sets Variables
grid_ui = []
num = ""
row = "" 
column = ""
random_roll = ""
player_position = ""
player_num = ""
enemy_roll = ""
enemy_position = ""
enemy_num = ""
enemy_msg = ""
stamina_num = ""
stamina = "" 


from tkinter import *

# Sets window
my_window = Tk()
my_window.attributes('-fullscreen', True)
my_window.resizable(True, True)
my_window.title("Grid Chase")

# Function which happens if play button is pressed
def play():
    global grid_ui, grid , grid_canvas, grid_num, num , row , column, player_position , player_num , enemy_position , stamina_num  , stamina

    player_position = 0
    stamina_num = 15
    enemy_position = -1
    stamina = f"Stamina : {stamina_num } "

    # Creates individual squares 100 times
    for i in range(100):
        
        # Sets the number for each square
        num = i + 1

        # Creates An individual square
        grid_canvas = Canvas(
        grid_frame,
        width= 87,       
        height= 67, 
        bd = 8,
        bg="white",      
        )
        
        # Creates the text for the squares
        grid_canvas.create_text(
            25 , 25,            
            text=str(num), 
            font=("Arial", 12, "bold"),
            fill="black"
        )

        # Adds each square to a list for the grid
        grid_ui.append(grid_canvas)
        
        # Sets the vertical squares as multiples of 10 by not using the remainder
        row = i // 10

        # Sets each row from 1 - 9 by using the remainder
        column = i % 10
        
        # using rows from 1 - 9 and columnds from 10 - 100 creates a 10x10 grid
        grid_canvas.grid(row = row , column= column ,padx = 1 , pady = 1)


    # Checks if the position of the player greater than or equal to 100
    # Player position is set to 99 since lists start from 0
    if player_position >= 99:
        # Sets the position to square 100
        player_position = 99
        player_num = 100
    
    # Sets the initial square of the player grey
    grid_ui[player_position].config(
        bg = "grey"
        )

    # Sets and updates the UI
    stamina_lbl.config(
        text = stamina
    )

    title_lbl.pack_forget()
    play_btn.pack_forget()
    grid_frame.pack(side="left", fill="y")
    stats_frame.pack(side="right", fill="both", expand=True)
    stamina_frame.pack( fill= "x" , pady = 30) 
    btn_holder.pack(fill = "x")
    stamina_lbl.pack(fill = "x" )
    dice_btn.pack( side = "left" , pady = 20 , padx = 10)

# Function to happen when the normal dice is pressed
def normal_dice():
    global random_roll , place , player_position, player_num


    # Player position = actuall position -1
    if player_position < 99:
        grid_ui[player_position].config(
            bg = "white"
        )    
        
        # Generates a random roll between 1 and 6
        random_roll = random.randint(1 , 6)
        
        # adds and updates the player position 
        player_position += random_roll 
        
        # Checks if the position of the player greater than or equal to 100
        # Player position is set to 99 since lists start from 0
        if player_position > 99:
            player_position = 99
            player_num = 100

        # Updates the number the player will see
        player_num = player_position + 1
    
        # Sets the tile the player is on to grey
        grid_ui[player_position].config(
            bg = "grey"
        )  
    
    # Sets the player on tile 100 to avoid the player going over the 100th tile
    else:
        player_position = 99
        player_num = 100

    # Gives the enemy his turn
    enemy()


# Sets the the enemy ai
def enemy():
    global enemy_roll  , enemy_position , player_position , enemy_num , player_num , enemy_msg

    # Sets the enemy message according to the number rolled and tile number he is on
    enemy_msg = f"""The enemy has 
moved {enemy_roll}
spaces and is on 
tile {enemy_num}"""


    # Checks if the player made it to a reasonable distance to make it fair
    if player_position > 6 and enemy_position == -1 :
        # Shows the enemy on the grid
        enemy_position = 0
        grid_ui[enemy_position].config(
            bg = "red"
        )
        # Stops the function to prevent the enemy from moving further before giving the player a turn
        return

    # Makes sure the player hasnt won
    if player_position < 99:
        # Makes sure the enemy hasnt made it to square 100
        if enemy_position < 99:
            
            # Checks if the enemy can move
            if enemy_position >= 0: 
                
                # Sets the enemys previous square to white
                grid_ui[enemy_position].config(
                    bg = "white"
                )

                # Creates the random roll the enemy will move
                enemy_roll = random.randint(1 , 6)

                # Updates the enemy position
                enemy_position += enemy_roll 

                # Checks if the position of the enemy greater than or equal to 100
                # enemy position is set to 99 since lists start from 0
                if enemy_position > 99:
                    enemy_position = 99
                    enemy_num = 100

                # Update tile number for the enemy
                enemy_num = enemy_position + 1
                
                # updates and shows the Enemy text
                enemy_roll_lbl.configure(
                    text = enemy_msg
                )
                enemy_roll_lbl.pack()

                # Changes the square the enemy is on to red
                grid_ui[enemy_position].config(
                    bg = "red"
                )
    # Avoids the player or enemy to going over square 100
        else:
            enemy_position = 99
            enemy_num = 100
    else:
        player_position = 99
        player_num = 100


    # Stops the game if the enemy catches the player
    if enemy_position == player_position or enemy_position > player_position:
        enemy_num = player_num
        enemy_position = player_position
        grid_ui[player_position].config(
            bg = "red"
        )

        grid_ui[enemy_position].config(
            bg = "white"
        )

        dice_btn.pack_forget()
    

# Creates the title
title_lbl = Label(
    text = " Grid Chase",
    fg = "black",
    bg = "DeepSkyBlue",
    height = 3,
    width = 30,
    font = ("Courier" , 25 , "bold")
)

# Creates play Button
play_btn = Button(
    my_window,
    text = " Play",
    width = 30,
    height = 2,
    command= play
)

# Creates grid frame
grid_frame = Frame(
    my_window,
    bd = 5,
    relief = "groove",
    bg = "red",
)

# Creates the stats frame
stats_frame = Frame(
    my_window,
    bg = "blue",
)

btn_holder = Frame(
    stats_frame,
    bg = "black"
)

# Creates the dice button
dice_btn = Button(
    btn_holder,
    text = "Normal Dice",
    width = 10,
    height = 7,
    command= normal_dice
)

# Creates the info frame
stamina_frame = Frame(
    stats_frame,
    bg = "black"
)

# Creates the info label
stamina_lbl = Label(
    stamina_frame,
    text = stamina,
    height= 3
)

# Creates the label to show the enemy roll
enemy_roll_lbl = Label(
    stats_frame,
    text = enemy_msg,
    font = ("Courier" , 25 , "bold")
)

# Packs UI
title_lbl.pack( pady = (150 , 0) , expand = TRUE)
play_btn.pack( pady = (100 , 400) , expand = TRUE)

# Keeps the window open
my_window.mainloop()