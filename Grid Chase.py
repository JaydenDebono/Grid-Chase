#Sets Title
title = "Grid Chase"

import random

# Sets Variables
grid_ui = []
num = ""
row = "" 
column = ""
player_position = ""
player_num = ""
enemy_roll = ""
enemy_position = ""
enemy_num = ""
enemy_msg = ""
stamina_num = ""
stamina = "" 
score = 0
score_msg = ""
win_msg = """Congratulations!
You managed to get to 
tile 100!"""
lose_msg = """The enemy
caught up to you and
you lost!"""
lose_st_msg = """You ran
out of stamina
and the enemy
caught up to you!"""
roll_msg = ""
normal_msg = "Normal Die : A free 1 in 6 chance move"
target_msg = "Target Die : A 1 in 3 chance move for 15 Stamina"
freeze_msg = """Freeze Die : A 3 in 6 chance move which uses 30 
                  Stamina and if odd, you do not move"""

from tkinter import *

# Sets window
my_window = Tk()
my_window.attributes('-fullscreen', True)
my_window.resizable(True, True)
my_window.title("Grid Chase")

# Function which happens if play button is pressed
def play():
    global grid_ui, grid , grid_canvas, grid_num, num , row , column, player_position , player_num , enemy_position , stamina_num  , stamina, score_msg , roll_msg, enemy_msg
        
    # Resets Variables
    player_position = 0
    player_num = 1
    stamina_num = 20
    enemy_position = -1
    stamina = f"Stamina : {stamina_num } "
    score_msg = f"Score : {score}"
    grid_ui = []
    roll_msg = f"You roled a  ____ and are on tile {player_num}"
    enemy_msg = "The enemy hasn't spawned in yet"

    # Loads UI
    title_lbl.pack_forget()
    play_btn.pack_forget()
    stats_frame.pack(side="right", fill="both", expand=True)
    grid_frame.pack(side="left", fill="y")
    roll_frame.pack(fill = "x" , pady = (10 , 0))
    enemy_roll_lbl.pack(fill = "x" , pady = (10 , 0))
    stamina_frame.pack( fill= "x" , pady = ( 10 , 0))
    score_frame.pack(fill = "x" , pady = (10 , 0)) 
    btn_holder1.pack(fill = "x" , pady = (40,0))
    btn_holder2.pack(fill = "x" , pady = ( 0,20 ) )
    normal_frame.pack( fill= "x" , pady = ( 20 , 0))
    target_frame.pack( fill= "x" , pady = ( 20 , 0) )
    freeze_frame.pack(fill= "x" , pady = ( 20 , 0) )
    score_lbl.pack(fill = "x")
    stamina_lbl.pack(fill = "x" )
    roll_lbl.pack(fill = "x")
    dice_btn.pack( side = "left" , pady = 30 , padx = (35 , 0))
    target_btn.pack(side = "right" , pady = 30 , padx = (0 , 35) )
    freeze_btn.pack( pady = (0, 30)  )
    normal_instructions.pack(fill = "x")
    target_instructions.pack(fill = "x")
    freeze_instructions.pack(fill = "x")

    # Updates window
    my_window.update_idletasks() 

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

        if num % 10 == 0:
            grid_canvas.config(
                bg = "yellow"
            )
            


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
    score_lbl.config(
        text = score_msg
    )
    roll_lbl.config(
        text = roll_msg
    )
    enemy_roll_lbl.config(
        text = enemy_msg
    )



# Function to happen when the normal dice is pressed
def normal_dice():
    global random_roll , player_position, player_num , stamina_num , score , roll_msg



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
        
        # Updates the roll message
        roll_msg = f"You roled a {random_roll} and are on tile {player_num}"
        roll_lbl.config(
            text = roll_msg
        )

        # Checks if the player is on a multiple of 10 tile
        if player_num % 10 == 0:
            # Checks if the player is on a tile less then or equal to 50 and adds 25 or 50 stamina
            if player_num <= 50:
                stamina_num += 25
            else:
                stamina_num += 50
  
        # Updates Stamina
        stamina = f"Stamina : {stamina_num } "
        stamina_lbl.config(
            text = stamina
            )
        
        # Sets the tile the player is on to grey
        grid_ui[player_position].config(
            bg = "grey"
        )

        # Checks if stamina is 0
        if stamina_num == 0:
            lose()

        # Gives the enemy his turn
        enemy()

    # Sets the player on tile 100 to avoid the player going over the 100th tile
    else:
        player_position = 99
        player_num = 100

    # Checks if the player has gotten to tile 100
    if player_num == 100:
        win()

# Sets function for target button
def target():
    global random_roll , player_position, player_num , stamina_num , score

    # Player position = actuall position -1
    if player_position < 99:
        
        # Checks if the player has enough stamina to roll the die
        if stamina_num >= 15:
            #Sets the last tile backl to white
            grid_ui[player_position].config(
                bg = "white"
            )    

            # Generates a random roll between 1 and 6
            random_roll = random.randint(1 , 3)
            
            # adds and updates the player position 
            player_position += random_roll 

            # Reduces stamina by 15
            stamina_num -= 15
        
            # Checks if the position of the player greater than or equal to 100
            # Player position is set to 99 since lists start from 0
            if player_position > 99:
                player_position = 99
                player_num = 100

            # Updates the number the player will see
            player_num = player_position + 1

            # Updates the roll message
            roll_msg = f"You roled a {random_roll} and are on tile {player_num}"
            roll_lbl.config(
                text = roll_msg
            )

            # Checks if the player is on a multiple of 10 tile
            if player_num % 10 == 0:
                # Checks if the player is on a tile less then or equal to 50 and adds 25 or 50 stamina
                if player_num <= 50:
                    stamina_num += 25
                else:
                    stamina_num += 50

            # Prevents the player from going below 0 stamina
            if stamina_num < 0:
                stamina_num = 0
            # Player loses if he gets 0 stamina
            if stamina_num == 0:
                lose()

            # Updates stamina
            stamina = f"Stamina : {stamina_num } "
            stamina_lbl.config(
                text = stamina
                )

            # Sets the tile the player is on to grey
            grid_ui[player_position].config(
                bg = "grey"
            )

            # Checks if the player wins
            if player_num == 100:
                win()
            else:
                # Gives the enemy his turn
                enemy()

        # Tells the player he doesnt have enough stamina if less than 15
        else:
            roll_lbl.config(
                text = "You do not have enough stamina"
            )
            return
        
    # Sets the player on tile 100 to avoid the player going over the 100th tile
    else:
        player_position = 99
        player_num = 100
    
        if player_num == 100:
            win()

# Sewts function for freeze button
def freeze():
    global random_roll , player_position, player_num , stamina_num , score , skip

    # Player position = actuall position -1
    if player_position < 99:
        # Checks if the player has enough stamina
        if stamina_num >= 30:

            # Sets the previous tile to white
            grid_ui[player_position].config(
                bg = "white"
            )    

            # Generates a random roll between 3 and 6
            random_roll = random.randint(3 ,6)
            
            # Checks if the random roll is even
            if random_roll % 2 == 0:
                    
                # Reduces stamina by 30
                stamina_num -= 30

                # adds and updates the player position 
                player_position += random_roll 
            
                # Checks if the position of the player greater than or equal to 100
                # Player position is set to 99 since lists start from 0
                if player_position > 99:
                    player_position = 99
                    player_num = 100

                # Updates the number the player will see
                player_num = player_position + 1

                # Updates the roll message
                roll_msg = f"You roled a {random_roll} and are on tile {player_num}"
                roll_lbl.config(
                    text = roll_msg
                )

                # Checks if the player is on a multiple of 10 tile
                if player_num % 10 == 0:
                    # Checks if the player is on a tile less then or equal to 50 and adds 25 or 50 stamina
                    if player_num <= 50:
                        stamina_num += 25
                    else:
                        stamina_num += 50
                
                # Updates stamina
                stamina = f"Stamina : {stamina_num } "
                stamina_lbl.config(
                    text = stamina
                    )
        
                # Sets the tile the player is on to grey
                grid_ui[player_position].config(
                    bg = "grey"
                )

                # Prevents stamina from going below 0
                if stamina_num < 0:
                    stamina_num = 0
                # Player loses if he has less than 0 stamina
                if stamina_num == 0:
                    lose()

                return
            
            else:
                # Updates roll message
                roll_msg = f"""You roled a {random_roll} and stayed on tile {player_num} 
since you got an odd number"""
                roll_lbl.config(
                    text = roll_msg
                )
                
                # Reduces stamina by 30
                stamina_num -=30
                # Updates stamnina
                stamina = f"Stamina : {stamina_num } "
                stamina_lbl.config(
                    text = stamina
                    )

                # Sets the tile the player is on to grey
                grid_ui[player_position].config(
                    bg = "grey"
                )

                
                # Prevents the player from going below 0 stamina
                if stamina_num < 0:
                    stamina_num = 0
                # Player loses if he gets 0 stamina
                if stamina_num == 0:
                    lose()

                enemy()

        else:
            roll_lbl.config(
            text = "You do not have enough stamina"
            )
            return

    # Sets the player on tile 100 to avoid the player going over the 100th tile
    else:
        player_position = 99
        player_num = 100
    
    if player_num == 100:
        win()

# Sets the the enemy ai
def enemy():
    global enemy_roll  , enemy_position , player_position , enemy_num , player_num , enemy_msg , score , skip

    skip = 0

    # Checks if the player made it to a reasonable distance to make it fair
    if player_position > 2 and enemy_position == -1 :
        # Shows the enemy on the grid
        enemy_position = 0
        enemy_num = 1
        grid_ui[enemy_position].config(
            bg = "red"
        )

        enemy_msg = f"""The enemy has spawned and is 
        on tile {enemy_num}"""
                                
        # updates and shows the Enemy text
        enemy_roll_lbl.configure(
            text = enemy_msg
        )

        # Stops the function to prevent the enemy from moving further before giving the player a turn
        return

    # Makes sure the player hasnt won
    if player_position < 99:
        # Makes sure the enemy hasnt made it to square 100
        if enemy_position < 99:
            
            # Checks if the enemy can move
            if enemy_position >= 0: 
                
                # Leaves the multiple of 10s yellow and the rest white after the enemy moves
                if (enemy_position +1) % 10 == 0:
                    grid_ui[enemy_position].config(
                    bg = "yellow"
                    )
                else:
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

                # Sets the enemy message according to the number rolled and tile number he is on
                enemy_msg = f"""The enemy has moved {enemy_roll} spaces and is 
on tile {enemy_num}"""
                                
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
    if enemy_position >= player_position and enemy_position > 0:

        # Sets the enemies previous tile back to white
        grid_ui[enemy_position].config(
            bg = "white"
        )

        # Sets the enemy instead of the players tile
        enemy_num = player_num
        enemy_position = player_position
        
        # Sets the tile to red
        grid_ui[player_position].config(
            bg = "red"
        )

        # The player loses
        lose()
    
    # Updates window
    my_window.update_idletasks() 
    
# Function to happen if player wins
def win():
    global score , score_msg
    
    # Adds score by 100 and updates the score message
    score += 100 
    score_msg = f"Score : {score}"
    score_lbl.config(
        text = score_msg
    )

    # Updates the UI
    btn_holder1.pack_forget()
    btn_holder2.pack_forget()
    normal_frame.pack_forget()
    target_frame.pack_forget()
    freeze_frame.pack_forget()
    win_lbl.pack(fill = "x" , pady = 50)
    playagn_btn.pack( pady = 100)

    # Updates window
    my_window.update_idletasks() 
    
# Function to happen if player loses
def lose():
    global score

    # Updates the UI
    btn_holder1.pack_forget()
    btn_holder2.pack_forget()
    normal_frame.pack_forget()
    target_frame.pack_forget()
    freeze_frame.pack_forget()
    # Checks if the player didnt have enough stamina or if he was caught by the enemy
    if stamina_num == 0:
        lose_st_lbl.pack(fill = "x" , pady = 50)
    else:
        lose_lbl.pack(fill = "x" , pady = 50)
    playagn_btn.pack(pady = 100)

    # Resets score value to 0
    score = 0
    
    # Updates window
    my_window.update_idletasks() 
    
# Function to happen if play again button is pressed
def playagn():
    global player_num , enemy_num
    
    # Updates UI
    enemy_roll_lbl.pack_forget()
    grid_frame.pack_forget()
    stats_frame.pack_forget()
    score_frame.pack_forget()
    stamina_frame.pack_forget()
    lose_lbl.pack_forget()
    lose_st_lbl.pack_forget()
    win_lbl.pack_forget()
    playagn_btn.pack_forget()

    # Helps reset the grid
    for a in (grid_ui):
        a.destroy()
    
    # Calls play function
    play()

    

# Creates the title
title_lbl = Label(
    text = " Grid Chase",
    fg = "black",
    bg = "DeepSkyBlue",
    height = 3,
    width = 30,
    font = ("Courier" , 25 , "bold")
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
    bg = "blue"
)

# Creates first button holder
btn_holder1 = Frame(
    stats_frame,
    bg = "black",
)

# Creates second button holder
btn_holder2 = Frame(
    stats_frame,
    bg = "black",
)

# Creates the info frame
stamina_frame = Frame(
    stats_frame,
    bg = "black"
)

# Creates score frame
score_frame = Frame(
    stats_frame,
    bg = "black"
)

# Creates roll Frame
roll_frame = Frame(
    stats_frame,
    bg = "black"
)

# Creates normal frame
normal_frame = Label(
    stats_frame,
    bg = "black"
)

# Creates target frame
target_frame = Frame(
    stats_frame,
    bg = "black"
)

# Creates freeze frame
freeze_frame = Frame(
    stats_frame,
    bg = "black"
)


# Creates the info label
stamina_lbl = Label(
    stamina_frame,
    text = stamina,
    height= 3
)

# Creates score label
score_lbl = Label(
    score_frame,
    text = score_msg,
    height = 3
)

# Creates the label to show the enemy roll
enemy_roll_lbl = Label(
    stats_frame,
    text = enemy_msg,
    height = 3
)

# Creates win label
win_lbl = Label(
    stats_frame,
    text = win_msg,
    height = 8,
    font = ("Courier", 25, "bold"),
)

# Creates lose label
lose_lbl = Label(
    stats_frame,
    text = lose_msg,
    height = 8,
    font = ("Courier", 25, "bold"),
)

# Creates lose label for running out of stamina
lose_st_lbl = Label(
    stats_frame,
    text = lose_st_msg,
    height = 8,
    font = ("Courier", 25, "bold"),
)

# Creates Roll Label
roll_lbl = Label(
    roll_frame,
    text = roll_msg,
    height = 3
)

# Creates normal instructions label
normal_instructions = Label(
    normal_frame,
    text = normal_msg,
    height = 3
)

# Creates target instruction label
target_instructions = Label(
    target_frame,
    text = target_msg,
    height = 3
)

# Creates freeze instructions label
freeze_instructions = Label(
    freeze_frame,
    text = freeze_msg,
    height = 3
)


# Creates play Button
play_btn = Button(
    my_window,
    text = " Play",
    width = 30,
    height = 2,
    command= play
)

# Creates the dice button
dice_btn = Button(
    btn_holder1,
    text = """Normal Dice
Free""",
    bg = "grey",
    highlightbackground = "grey",
    width = 10,
    height = 7,
    command= normal_dice
)

# Creates play again button
playagn_btn = Button(
    stats_frame,
    text = " Play Again",
    width = 30,
    height = 2,
    command = playagn
)

# Creates target button
target_btn = Button(
    btn_holder1,
    text = """Target Dice
-15 Stamina""",
    highlightbackground = "DeepSkyBlue",
    width = 10,
    height = 7,
    command= target
)

# Creates freeze button
freeze_btn = Button(
    btn_holder2,
    text = """Freeze Dice
-30 Stamina""",
    highlightbackground = "gold",
    width = 10,
    height = 7,
    command= freeze
)


# Packs UI
title_lbl.pack( pady = (150 , 0) , expand = TRUE)
play_btn.pack( pady = (100 , 400) , expand = TRUE)

# Keeps the window open
my_window.mainloop()
