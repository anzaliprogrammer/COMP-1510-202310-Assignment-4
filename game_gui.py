import tkinter as tk

gui_dim = (1102,568)
level_caption = ('Entery', 'Level 1', 'Level 2', 'Level 3', 'Finished')
state_caption = ('undiscovered', 'discovered', 'solved', 'failed')
directions = ('n','s','w','e','north', 'south', 'west', 'east','1','2','3','4')
question_answer = ('y','n','yes','no')
board_cells_caption = ("-2 , 2","-1 , 2","0 , 2","1 , 2","2 , 2","-2 , 1","-1 , 1","0 , 1","1 , 1","2 , 1",
                "-2 , 0","-1 , 0","0 , 0","1 , 0","2 , 0","-2 , -1","-1 , -1","0 , -1","1 , -1","2 , -1",
                "-2 , -2","-1 , -2","0 , -2","1 , -2","2 , -2")
challenge_question = ((
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    'base cell',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 =',
    '10 + 90 ='), (
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    'base cell',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 =',
    '15 + 95 ='), (
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    'base cell',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 =',
    '20 + 100 ='))
challenge_results = ((
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    'base cell',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100',
    '100'), (
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    'base cell',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110',
    '110'), (
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    'base cell',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120',
    '120'))

def initial_player():
    game_player = {
        "name": "",
        "level": 0,
        "health": 3,
        "current_position": 12,
        "solved_cells": 0,
        "doing_challenge": False
    }
    return game_player

def initial_board():
    game_board = {
        "level": 0
    }
    for cell_counter in range(0,25):
        game_board.update({str(cell_counter): state_caption[0]})

    return game_board

def can_move(direction, position):
    result = True
    if (direction in {"n","north","1"}) and position < 5:
        result = False
    elif (direction in {"s","south","3"}) and position > 20:
        result = False
    elif (direction in {"e","east","2"}) and (position in {4,9,14,19,24}):
        result = False
    elif (direction in {"w","west","4"}) and (position in {0,5,10,15,20}):
        result = False
    return result

def do_command(command, game_player, game_board):
    result = {
        "succeed": False,
        "caption": "",
        "player": game_player,
        "board": game_board
    }
    if result["player"]["doing_challenge"]:
        result["succeed"] = True
        print(command)
        print(result["player"]["level"])
        print(result["player"]["current_position"])
        print(challenge_results[result["player"]["level"]-1][result["player"]["current_position"]])
        if command == challenge_results[result["player"]["level"]-1][result["player"]["current_position"]]:
            result["board"][str(result["player"]["current_position"])] = state_caption[2]
            result["player"]["solved_cells"] += 1
            result["caption"] = "You won this challenge\nCommands:\n   1. N : go North\n   2. E : go East\n   3. S : go south\n   4. W : go West"
            result["player"]["doing_challenge"] = False
        else:
            result["board"][str(result["player"]["current_position"])] = state_caption[3]
            result["player"]["health"] -= 1
            result["caption"] = "You lost this challenge\nCommands:\n   1. N : go North\n   2. E : go East\n   3. S : go south\n   4. W : go West\n   5. C : do Challenge"
            result["player"]["doing_challenge"] = False
        return result
    if result["player"]["level"] == 0:
        if len(command) <= 2:
            result["succeed"] = False
            result["caption"] = "  your name is too short.\n  select another name, please !!"
        else:
            result["succeed"] = True
            result["caption"] = f"hi {command}\nWelcome !!\nType H or h to get game commands"
            result["player"] = {
                "name": command,
                "level": 1,
                "health": 3,
                "current_position": 12,
                "solved_cells": 0,
                "doing_challenge": False
            }
            result["board"]["level"] = 1
            for cell_counter in range(0,25):
                result["board"].update({str(cell_counter): state_caption[0]})
            result["board"]["12"] = state_caption[1]
    elif command.lower() == "h" or command.lower() == "help" or command.lower() == "?":
        result["succeed"] = True
        result["caption"] = "Commands:\n   1. N : go North\n   2. E : go East\n   3. S : go south\n   4. W : go West"
        if result["player"]["current_position"] != 12:
            if result["board"][str(result["player"]["current_position"])] in (state_caption[1], state_caption[3]):
                result["caption"] = f"{result['caption']}\n   5. C : do Challenge"
    elif command.lower() in directions:
        result["succeed"] = True
        if can_move(command.lower(),result["player"]["current_position"]):
            result["caption"] = "You moved\nCommands:\n   1. N : go North\n   2. E : go East\n   3. S : go south\n   4. W : go West"
            if (command.lower() in {"n","north","1"}):
                result["player"]["current_position"] -= 5
            elif (command.lower() in {"s","south","3"}):
                result["player"]["current_position"] += 5
            elif (command.lower() in {"e","east","2"}):
                result["player"]["current_position"] += 1
            elif (command.lower() in {"w","west","4"}):
                result["player"]["current_position"] -= 1
            if result["board"][str(result["player"]["current_position"])] == state_caption[0]:
                result["board"][str(result["player"]["current_position"])] = state_caption[1]
        else:
            result["caption"] = "You can't move\nCommands:\n   1. N : go North\n   2. E : go East\n   3. S : go south\n   4. W : go West"
        if result["player"]["current_position"] != 12:
            if result["board"][str(result["player"]["current_position"])] in (state_caption[1], state_caption[3]):
                result["caption"] = f"{result['caption']}\n   5. C : do Challenge"
    elif command.lower() == result["player"]["name"].lower():
        result["succeed"] = True
        result["caption"] = f"hi, I know you {result['player']['name']}\nType H or h to get game commands\n"
    else:
        result["succeed"] = True
        result["caption"] = "Type H or h to get game commands\n"
    return result

def game_gui():
    def write_to_text(text_var, text_caption, insert_index, delete_bindex, delete_eindex):
        text_var.config(state="normal")
        if delete_bindex != "-1.-1":
            text_var.delete(delete_bindex, delete_eindex)
        if insert_index != "-1.-1":
            text_var.insert(insert_index, text_caption)
        text_var.config(state="disabled")

    def draw_board_cells(game_player, game_board):
        for cell_counter in range(0,25):
            label_board_cells[cell_counter].config(background="light grey")
            if game_board[str(cell_counter)] == state_caption[0]:
                label_board_cells[cell_counter].config(foreground="lightgrey")
            elif game_board[str(cell_counter)] == state_caption[1]:
                label_board_cells[cell_counter].config(foreground="black")
            elif game_board[str(cell_counter)] == state_caption[2]:
                label_board_cells[cell_counter].config(foreground="green")
            elif game_board[str(cell_counter)] == state_caption[3]:
                label_board_cells[cell_counter].config(foreground="red")
        label_board_cells[game_player["current_position"]].config(background="light green")

    def show_status(game_player, game_board):
        write_to_text(text_status, f"{game_player['name']}\n---------------------------", tk.INSERT, "1.0", tk.END)
        write_to_text(text_status, f"\nCurrent level : {level_caption[game_player['level']]}", tk.INSERT, "-1.-1", "")
        write_to_text(text_status, f"\nYour position : {board_cells_caption[game_player['current_position']]}", tk.INSERT, "-1.-1", "")
        write_to_text(text_status, f"\nHealth : {game_player['health']}", tk.INSERT, "-1.-1", "")
        write_to_text(text_status, f"\nSolved : {game_player['solved_cells']}", tk.INSERT, "-1.-1", "")
        write_to_text(text_status, f"\nFailed : {3-game_player['health']}", tk.INSERT, "-1.-1", "")
        draw_board_cells(game_player, game_board)


    def initial_gui():
        label_board_cells[12].config(background="light green")

        write_to_text(text_room_space, "<----   PUZZLE LAND   ---->\n\nPlease enter your name:",tk.INSERT, "1.0", tk.END)

        write_to_text(text_status, "", "-1.-1", "1.0", tk.END)

        entry_command.delete("0",tk.END)

    def show_challenge(position, level):
        write_to_text(text_room_space, "<----   PUZZLE LAND   ---->",tk.INSERT, "1.0", tk.END)
        write_to_text(text_room_space, f"\nLevel : {level} - Challenge No : {position}", tk.INSERT, "-1.-1", "")
        write_to_text(text_room_space, f"\n{challenge_question[level-1][position]}", tk.INSERT, "-1.-1", "")

    def play_game(event):
        if event.char == "\r":
            nonlocal player, board
            if player["health"] <= 0 or player["solved_cells"] > 23:
                if entry_command.get() in question_answer:
                    if entry_command.get() in ('y','yes'):
                        swap_level = 1
                        swap_health = 3
                        if player["solved_cells"] > 23 and player["level"] < 4:
                            swap_level = player["level"]
                            swap_health = player["health"]
                        player = initial_player()
                        board = initial_board()
                        player["level"] = swap_level
                        board["level"] = swap_level
                        player["health"] = swap_health
                        board["12"] = state_caption[1]
                    else:
                        game_windows.destroy()
                        return
                else :
                    entry_command.delete(0, tk.END)
                    return
            if (entry_command.get() in {"c","5"}) and (not player["doing_challenge"]):
                if player["current_position"] != 12 and board[str(player["current_position"])] != state_caption[2]:
                    player["doing_challenge"] = True
                    show_challenge(player["current_position"], player["level"])
                    entry_command.delete(0, tk.END)
                    return
            command_result = do_command(entry_command.get(), player, board)
            entry_command.delete(0, tk.END)
            write_to_text(text_room_space, "<----   PUZZLE LAND   ---->",tk.INSERT, "1.0", tk.END)
            write_to_text(text_room_space, f"\n{command_result['caption']}", tk.INSERT, "-1.-1", "")
            if command_result["succeed"]:
                player = command_result["player"]
                board = command_result["board"]
                show_status(player, board)
                if player["health"] <= 0:
                    write_to_text(text_room_space, "<----   PUZZLE LAND   ---->",tk.INSERT, "1.0", tk.END)
                    write_to_text(text_room_space, "\n<><> GAME OVER <><>\nDo you want to play again ? (y/n)", tk.INSERT, "-1.-1", "")
                elif player["solved_cells"] > 23:
                    if player["level"] == 3:
                        write_to_text(text_room_space, "<----   PUZZLE LAND   ---->",tk.INSERT, "1.0", tk.END)
                        write_to_text(text_room_space, "\n<><> YOU WIN <><>\nDo you want to play again ? (y/n)", tk.INSERT, "-1.-1", "")
                    else:
                        write_to_text(text_room_space, "<----   PUZZLE LAND   ---->",tk.INSERT, "1.0", tk.END)
                        write_to_text(text_room_space, "\n/\\__/\\/\\ Level up /\\/\\__/\\\nDo you want to continue ? (y/n)", tk.INSERT, "-1.-1", "")
                    player["level"] += 1
            else:
                write_to_text(text_room_space, "\nPlease enter your name:", tk.INSERT, "-1.-1", "")


    def make_gui(dims):
        gui_windows = tk.Tk()
        screen_width = gui_windows.winfo_screenwidth()
        screen_height = gui_windows.winfo_screenheight()
        position_right = int(screen_width / 2 - dims[0]/2)
        position_top = int(screen_height/2 -dims[1]/2)
        gui_windows.resizable(width=False, height=False)
        gui_windows.geometry(f'{dims[0]}x{dims[1]}+{position_right}+{position_top}')
        gui_windows.title("SUD - game panel")

        gui_windows.rowconfigure(0, weight=3)
        gui_windows.rowconfigure(1, weight=3)
        gui_windows.rowconfigure(2, weight=4)
        gui_windows.rowconfigure(3, weight=2)
        gui_windows.rowconfigure(4, weight=1)
        gui_windows.columnconfigure(0, weight=1)
        gui_windows.columnconfigure(1, weight=20)
        gui_windows.columnconfigure(2, weight=1)

        return gui_windows

    game_windows = make_gui(gui_dim)
    label_board_cells = []

    text_room_space = tk.Text(game_windows, font=('helvetica',25,'bold'), width=44, height=13, foreground="yellow", background="blue")
    text_status = tk.Text(game_windows, font=('helvetica',20,'normal'), width=10, height=7,foreground="orange", background="black")
    label_command = tk.Label(game_windows, text="Command line :", width=12, font=('helvetica',12,'bold'))
    entry_command = tk.Entry(game_windows, font=('helvetica',17,'normal'), foreground="white", background="black")
    frm_map = tk.Frame(game_windows, relief=tk.FLAT, bd=1)
    for row_counter in range (0,5):
        for col_counter in range (0,5):
            label_board_cells.append(tk.Label(frm_map, text=board_cells_caption[row_counter*5+col_counter], height=3, width=7, background="light grey"))
            label_board_cells[row_counter*5+col_counter].grid(row=row_counter, column=col_counter, sticky="nsew", padx=1, pady=1)
    btn_exit = tk.Button(game_windows, text="Exit", font=('Times New Roman',17,'bold'), command=game_windows.destroy)

    text_room_space.grid(row=0, column=0, sticky="nsew", rowspan=4, columnspan=2, padx=5, pady=5)
    frm_map.grid(row=0, column=2, sticky="nsew", rowspan=2, padx=5, pady=5)
    text_status.grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
    label_command.grid(row=4, column=0, padx=5, pady=5)
    entry_command.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
    btn_exit.grid(row=4, column=2, sticky="ewns", padx=5, pady=5)

    initial_gui()

    player = initial_player()
    board = initial_board()

    game_windows.bind("<Key>", play_game)

    game_windows.mainloop()
