import random as rd
import dearpygui.dearpygui as dpg
import pygame
import text
import time
import threading
import colors as col
import linecache
import sudoku_map

version = "1.0"

version_popup_text = f"Version 1.0: First release."

pygame.init()
start_generating_map_sound = pygame.mixer.Sound("resources/start_generating_map.wav")
correct = pygame.mixer.Sound("resources/correct.wav")
incorrect = pygame.mixer.Sound("resources/incorrect.wav")
win_game = pygame.mixer.Sound("resources/win_game.wav")

start_generating_map_sound_exp = pygame.mixer.Sound("resources/start_generating_map_exp.wav")
correct_exp = pygame.mixer.Sound("resources/correct_exp.wav")
incorrect_exp = pygame.mixer.Sound("resources/incorrect_exp.wav")
win_game_exp = pygame.mixer.Sound("resources/win_game_exp.wav")
pencil_exp = pygame.mixer.Sound("resources/pencil_exp.wav")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_difficulty = ["Easy", "Medium", "Evil"]
list_gamemode = ["Check continuously", "Check on finish"]

new_text = [True]
timer_on = [True]
number_of_mistakes = []

sudoku = []
flat_sudoku = []
flat_sudoku_temp = []
hidden_sudoku = []
sudoku_current = []
hidden_values_temp = []
list_correct = []
list_incorrect = []

def callback_sudoku_map_start_creating_maps_button():
    dpg.configure_item("start_creating_maps_button", enabled = False)
    thread_1_create.daemon = True
    thread_1_create.start()

def callback_sudoku_map_stop_creating_maps_button():
    dpg.configure_item("stop_creating_maps_button", enabled = False)
    sudoku_map.func_stop_creating_maps_button()



def callback_start_generating_map(sender, app_data):
    sound = get_value_sound()
    if sound == "On":
        start_generating_map_sound.play()
    if sound == "Explicit":
        start_generating_map_sound_exp.play()

    dpg.configure_item("loading", show = True)
    dpg.configure_item("funny_text", show = True)
    dpg.configure_item("minion", show = True)

    dpg.configure_item("difficulty", enabled = False )
    dpg.configure_item("gamemode_select", enabled = False)
    dpg.configure_item("sound", enabled = False)

    sudoku.clear()

    load_valid_map()

def load_valid_map():
    new_map_load = open("valid_maps.txt")
    count = sum(1 for _ in new_map_load)
    line = rd.randint(1, count)
    selected_line = linecache.getline("valid_maps.txt", line)

    selected_line = selected_line.replace("[", "")
    selected_line = selected_line.replace("]", "")
    selected_line = selected_line.replace(",", "")
    selected_line = selected_line.replace(" ", "")
    selected_line = selected_line.replace("\n", "")

    for i in selected_line:
        flat_sudoku_temp.append(int(i))
        flat_sudoku.append(int(i))

    for i in range(0, 9):
        sudoku.append([])
        for j in range(0, 9):
            sudoku[i].append(flat_sudoku_temp[0])
            flat_sudoku_temp.pop(0)

    time.sleep(3.5)

    dpg.configure_item("loading", show = False)
    dpg.configure_item("funny_text", show = False)
    dpg.configure_item("minion", show = False)
    dpg.configure_item("generate_map", show = False)
    dpg.configure_item("start_game", show = True)
    
    create_board()

def func_gamemode_selector(sender, app_data):
    gamemode = get_value_gamemode()
    sound = get_value_sound()

    row_column = "".join(number for number in sender if number.isdecimal())
    row = int(row_column[0])
    column = int(row_column[1])

    current_number = sudoku_current[row - 1][column - 1]

    if app_data != "image_blank":
        new_number_image_type = "".join(number for number in app_data if number.isdecimal())
        new_number = int(new_number_image_type[0])

    old_number = sudoku[row - 1][column - 1]

    if app_data != "image_blank": # pen or pencil mark was used
        if app_data == f"image_{new_number}2": # pen mark was used
            if old_number != new_number: # incorrect value is played
                print(f"row: {row} column: {column}")
                print(f"incorrect value: {new_number}")
                print(f"correct value: {old_number}")
                sudoku_current[row - 1].pop(column - 1)
                sudoku_current[row - 1].insert(column - 1, 0)
                number_of_mistakes.append(0)
                dpg.set_value("mistakes", len(number_of_mistakes))
                if gamemode == list_gamemode[0]:
                    dpg.configure_item(sender, texture_tag = f"image_{new_number}3")
                    if sound == "On":
                        incorrect.play()
                    if sound == "Explicit":
                        incorrect_exp.play()
                    time.sleep(1.5)
                    dpg.configure_item(sender, texture_tag = f"image_blank")
                if gamemode == list_gamemode[1]:
                    dpg.configure_item(sender, texture_tag = app_data)
                    list_incorrect.append(0)

            if old_number == new_number and current_number != new_number: # correct value is played
                dpg.configure_item(sender, texture_tag = app_data)
                sudoku_current[row - 1].pop(column - 1)
                sudoku_current[row - 1].insert(column - 1, new_number)
                if gamemode == list_gamemode[0]:
                    dpg.configure_item(sender, payload_type = "no_change")
                position = (((row - 1) * 9) + column) - 1
                hidden_values_temp.remove(position)
                if len(hidden_values_temp) != 0 and gamemode == list_gamemode[0]:
                    if sound == "On":
                        correct.play()
                    if sound == "Explicit":
                        correct_exp.play()
                if gamemode == list_gamemode[1]:
                    list_correct.append(0)

                if len(hidden_values_temp) == 0 and gamemode == list_gamemode[0]:
                    print("win")
                    dpg.configure_item("finish_popup", show = True)
                    dpg.configure_item("stat_mistakes", show = True)
                    elapsed_time = dpg.get_value("timer")
                    dpg.set_value("stat_time", f"Your time is: {elapsed_time}")
                    dpg.set_value("stat_mistakes", f"Number of mistakes: {len(number_of_mistakes)}")
                    timer_on.pop()
                    timer_on.append(False)
                    if sound == "On":
                        win_game.play()
                    if sound == "Explicit":
                        win_game_exp.play()

        if app_data == f"image_{new_number}4": # pencil mark was used
            if sound == "Explicit":
                pencil_exp.play()
            dpg.configure_item(sender, texture_tag = app_data)
    
    if app_data == "image_blank": # reset mark was used
        dpg.configure_item(sender, texture_tag = app_data)
        if gamemode == list_gamemode[1]:
            if current_number != 0:
                position = (((row - 1) * 9) + column) - 1
                hidden_values_temp.append(position)

    print(f"remaining fields: {len(hidden_values_temp)}")

def callback_start_game():
    gamemode = get_value_gamemode()
    sound = get_value_sound()
    dpg.configure_item("welcome_screen", show = False)
    dpg.configure_item("game_screen", show = True)
    dpg.set_primary_window("game_screen", True)

    if gamemode == list_gamemode[1]:
        dpg.configure_item("evaluate_button", show = True)
        dpg.configure_item("mistakes_tree", show = False)

    if sound == "On":
        start_generating_map_sound.stop()
    if sound == "Explicit":
        start_generating_map_sound_exp.stop()
    
    thread_1_game.daemon = True
    thread_1_game.start()

def callback_start_timer():
    start_time = time.time()

    try:
        while timer_on[0] == True:
            mid_time = time.time()
            elapsed_time = int(abs(mid_time - start_time))
            if elapsed_time < 60:
                dpg.set_value("timer", elapsed_time)
            if elapsed_time >= 60:
                minutes = elapsed_time // 60
                seconds = elapsed_time % 60
                dpg.set_value("timer", f"{minutes}:{seconds}")
    except: Exception
    return

def func_hidden_values():
    difficulty = get_value_difficulty()

    if difficulty == "Easy":
        k = 43
        hidden_values = rd.sample(range(0, 81), k)
        for i in range(0, k):
            hidden_values_temp.append(hidden_values[i])

    if difficulty == "Medium":
        k = 49
        hidden_values = rd.sample(range(0, 81), k)
        for i in range(0, k):
            hidden_values_temp.append(hidden_values[i])

    if difficulty == "Evil":
        k = 56
        hidden_values = rd.sample(range(0, 81), k)
        for i in range(0, k):
            hidden_values_temp.append(hidden_values[i])

    return hidden_values

def create_board():
    hidden_values = func_hidden_values()

    for i in hidden_values: 
        flat_sudoku.pop(i)
        flat_sudoku.insert(i, 0)

    for row in range(1, 10):
        sudoku_current.append([])
        for column in range(1, 10):
            number_value = 9 * (row - 1) + (column - 1)
            hidden_sudoku.append(flat_sudoku[number_value])
            sudoku_current[row - 1].append(flat_sudoku[number_value])
            if flat_sudoku[number_value] > 0:
                dpg.configure_item(f"button_{row}_{column}", texture_tag = f"image_{flat_sudoku[number_value]}1", payload_type = "no_change")
        print(hidden_sudoku)
        hidden_sudoku.clear()

def callback_evaluate():
    timer_on.pop()
    timer_on.append(False)
    elapsed_time = dpg.get_value("timer")

    dpg.configure_item("finish_popup", show = True)
    dpg.configure_item("stat_incomplete", show = True)
    dpg.configure_item("stat_correct", show = True)
    dpg.configure_item("stat_incorrect", show = True)

    dpg.set_value("stat_time", f"Your time is: {elapsed_time}")
    dpg.set_value("stat_incomplete", f"Incomplete fields: {elapsed_time}")
    dpg.set_value("stat_correct", f"Correct fields: {len(list_correct)}")
    dpg.set_value("stat_incorrect", f"Incorrect fields: {elapsed_time}")

def get_value_sound():
    sound = dpg.get_value("sound")
    return sound    

def get_value_difficulty():
    difficulty = dpg.get_value("difficulty")
    return difficulty

def get_value_gamemode():
    gamemode = dpg.get_value("gamemode_select")
    return gamemode

def load_image_resource(image_number, image_type):
    width, height, channels, data = dpg.load_image(f"resources/image_{image_number}{image_type}.png")
    return width, height, channels, data

def add_static_texture(image_number, image_type):
    dpg.add_static_texture(width = image_width[image_number - 1][image_type - 1], height = image_height[image_number - 1][image_type - 1], default_value = image_data[image_number - 1][image_type - 1], tag = f"image_{image_number}{image_type}")

thread_1_game = threading.Thread(target = callback_start_timer)

thread_1_create = threading.Thread(target = sudoku_map.func_start_creating_maps_button)

image_width = []
image_height = []
image_channels = []
image_data = []

##############################################################################################################################################################################################

dpg.create_context()

dpg.set_exit_callback(callback = sudoku_map.func_stop_creating_maps_button)

for image_number in range(1, 10):
    image_width.append([])
    image_height.append([])
    image_channels.append([])
    image_data.append([])
    for image_type in range(1, 5):
        width, height, channels, data = load_image_resource(image_number, image_type)
        image_width[image_number - 1].append(width)
        image_height[image_number - 1].append(height)
        image_channels[image_number - 1].append(channels)
        image_data[image_number - 1].append(data)

width_blank, height_blank, channels_blank, data_blank = dpg.load_image("resources/image_blank.png")
width_reset, height_reset, channels_reset, data_reset = dpg.load_image("resources/image_reset.png")
width_logo, height_logo, channels_logo, data_logo = dpg.load_image("resources/rocket_monkey_logo.png")

with dpg.texture_registry():

    for image_number in range(1, 10):
        for image_type in range(1, 5):
            add_static_texture(image_number, image_type)

    dpg.add_static_texture(width = width_blank, height = height_blank, default_value = data_blank, tag = "image_blank")
    dpg.add_static_texture(width = width_reset, height = height_reset, default_value = data_reset, tag = "image_reset")
    dpg.add_static_texture(width = width_logo, height = height_logo, default_value = data_logo, tag = "image_logo")

dpg.create_viewport(title = 'Sudoku', width = 600, height = 600, small_icon = "resources/icon.ico", large_icon = "resources/icon.ico", resizable = False)

with dpg.window(label = "Welcome screen", pos = (100, 100), tag = "welcome_screen"):
    with dpg.menu_bar():
        with dpg.menu(label = "Map creation", show = True):
            dpg.add_button(label = "Start creating maps", callback = callback_sudoku_map_start_creating_maps_button, width = 150, tag = "start_creating_maps_button")
            dpg.add_button(label = "Stop creating maps", callback = callback_sudoku_map_stop_creating_maps_button, width = 150, tag = "stop_creating_maps_button")
        
        with dpg.menu(label = "About"):
            dpg.add_text("Developed by Rocket Monkey")
            dpg.add_image("image_logo", width = 100, height = 100)
            dpg.add_text(f"Version {version}", tag = "version_popup")

            with dpg.popup(parent = "version_popup", mousebutton = dpg.mvMouseButton_Left):
                dpg.add_text("test")
                
    with dpg.tree_node(label = "Difficulty:", default_open = True, bullet = True, leaf = True):
        dpg.add_radio_button(list_difficulty, horizontal = True, default_value = "Easy", tag = "difficulty")

    with dpg.tree_node(label = "Game mode:", default_open = True, bullet = True, leaf = True):
        dpg.add_radio_button(list_gamemode, horizontal = True, default_value = "Check continuously", tag = "gamemode_select")
        with dpg.tooltip("gamemode_select"):
            dpg.add_text(text.gamemode_continuous, bullet = True)
            dpg.add_text(text.gamemode_finish, bullet = True)

    with dpg.tree_node(label = "Sound:", default_open = True, bullet = True, leaf = True):
        dpg.add_radio_button(("On", "Off", "Explicit"), horizontal = True, default_value = "On", tag = "sound")

    with dpg.theme(tag = "button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, col.retro_red)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, col.retro_red)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, col.retro_red)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 40)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 40, 20)

    dpg.add_button(label = "Start generating map", callback = callback_start_generating_map, tag = "generate_map")
    dpg.bind_item_theme(dpg.last_item(), "button_theme")

    dpg.add_loading_indicator(label = "Creating new map", color = col.retro_red, secondary_color = col.retro_red, show = False, tag = "loading")
    dpg.add_text(rd.choice(text.text_snippets), show = False, tag = "funny_text")
    dpg.add_text("Please be patient, the minions are working slow today...", show = False, tag = "minion")

    dpg.add_button(label = "     Start game     ", callback = callback_start_game, show = False, tag = "start_game")
    dpg.bind_item_theme(dpg.last_item(), "button_theme")

with dpg.window(label = "Game screen", pos = (100, 100), show = False, tag = "game_screen"):
    for row in range(1, 10):
        with dpg.group(horizontal = True):
            for column in range(1, 10):
                dpg.add_image_button("image_blank", width = 30, height = 30, drop_callback = func_gamemode_selector, payload_type = "strings", tag = f"button_{row}_{column}")
 
                if row > 0 and column == 9:
                    dpg.add_image_button(f"image_{row}2", width = 30, height = 30, indent = 450)
                    with dpg.drag_payload(parent = dpg.last_item(), drag_data = f"image_{row}2", payload_type = "strings"):
                        dpg.add_text(f"{row}")

                    dpg.add_image_button(f"image_{row}4", width = 30, height = 30, indent = 500)
                    with dpg.drag_payload(parent = dpg.last_item(), drag_data = f"image_{row}4", payload_type = "strings"):
                        dpg.add_text(f"{row}")

    dpg.add_image_button("image_reset", width = 30, height = 30, indent = 500, show = True)
    with dpg.drag_payload(parent = dpg.last_item(), drag_data = "image_blank", payload_type = "strings"):
        dpg.add_text("reset")

    with dpg.draw_layer():
        dpg.draw_rectangle((0, 0), (134, 118), color  = col.retro_grey)
        dpg.draw_rectangle((134, 0), (272, 118), color = col.retro_grey)
        dpg.draw_rectangle((272, 0), (407, 118), color = col.retro_grey)

        dpg.draw_rectangle((0, 118), (134, 238), color = col.retro_grey)
        dpg.draw_rectangle((134, 118), (272, 238), color = col.retro_grey)
        dpg.draw_rectangle((272, 118), (407, 238), color = col.retro_grey)

        dpg.draw_rectangle((0, 238), (134, 357), color = col.retro_grey)
        dpg.draw_rectangle((134, 238), (272, 357), color = col.retro_grey)
        dpg.draw_rectangle((272, 238), (407, 357), color = col.retro_grey)

        dpg.draw_rectangle((0, 0), (407, 357), color = col.retro_red, thickness = 2)

    with dpg.tree_node(label = "Instructions:", default_open = True, bullet = True, leaf = True):
        dpg.add_text(text.instructions_gamemode_continuous)

    with dpg.tree_node(label = "Time:", default_open = True, bullet = True, leaf = True):
        dpg.add_text("0", tag = "timer")

    with dpg.tree_node(label = "Mistakes:", default_open = True, bullet = True, leaf = True, tag = "mistakes_tree"):
        dpg.add_text("0", tag = "mistakes")

    dpg.add_button(label = "Evaluate!", callback = callback_evaluate, show = False, tag = "evaluate_button")
    dpg.bind_item_theme(dpg.last_item(), "button_theme")

    with dpg.window(label = "Finish", modal = True, show = False, no_title_bar = True, pos = (100, 100), tag = "finish_popup"):
        dpg.add_text("Congratulations, here are your stats:")
        dpg.add_separator()
        dpg.add_text("Your time is:", tag = "stat_time")
        dpg.add_text("Number of mistakes:", show = False, tag = "stat_mistakes")
        dpg.add_text("Incomplete fields:", show = False, tag = "stat_incomplete")
        dpg.add_text("Correct fields:", show = False, tag = "stat_correct")
        dpg.add_text("Incorrect fields", show = False, tag = "stat_incorrect")
        with dpg.group(horizontal=True):
            dpg.add_button(label = "OK", width = 75, callback = lambda: dpg.configure_item("finish_popup", show = False))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("welcome_screen", True)
dpg.start_dearpygui()
dpg.destroy_context()