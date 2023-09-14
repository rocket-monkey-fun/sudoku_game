import random as rd
import dearpygui.dearpygui as dpg
import pygame
import text
import time
import threading
import colors as col

pygame.init()
start_generating_map_sound = pygame.mixer.Sound("resources/start_generating_map.wav")
correct = pygame.mixer.Sound("resources/correct.wav")
incorrect = pygame.mixer.Sound("resources/incorrect.wav")
win_game = pygame.mixer.Sound("resources/win_game.wav")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
stage = []
sudoku = []
easy_mode = []
new_text = [True]
timer_on = [True]
number_of_mistakes = []
start_creating_maps = [False]
new_map = []

def iteration_1(range_i, range_j, range_k, random_numbers):
    for i in range(range_i[0], range_i[1]):
        for j in range(range_j[0], range_j[1]):
            for k in range(range_k[0], range_k[1]):
                if random_numbers[i] != sudoku[j][k]:
                    stage.append(1)
                    if len(stage) == 9:
                        stage.clear()
                else:
                    stage.clear()
                    return False

def iteration_2(range_i, range_j, random_numbers):
    for i in range(range_i[0], range_i[1]):
        for j in range(range_j[0], range_j[1]):
            if random_numbers[i] != sudoku[j][i]:
                stage.append(1)
                if len(stage) == 9:
                    stage.clear()
            else:
                stage.clear()
                return False    

def callback_start_creating_maps():
    start_creating_maps.pop()
    start_creating_maps.append(True)

    callback_new_game_generate()

def callback_new_game(sender, app_data):
    sound = get_value_sound()

    dpg.configure_item("loading", show = True)
    dpg.configure_item("funny_text", show = True)
    dpg.configure_item("minion", show = True)

    if sound == "On":
        start_generating_map_sound.play()

    sudoku.clear()



    thread1.daemon = True
    thread1.start()
    thread2.daemon = True
    thread2.start()
    thread3.daemon = True
    thread3.start()

def callback_new_game_generate():
    random_numbers_first_row = rd.sample(numbers, k = 9)
    sudoku.append(random_numbers_first_row)

    while len(sudoku) != 9:
        random_numbers = rd.sample(numbers, k = 9)

        print(len(sudoku))

        while len(sudoku) == 1:
            if iteration_1((0, 3), (0, 1), (0, 3), random_numbers) == False:
                break
            if iteration_1((3, 6), (0, 1), (3, 6), random_numbers) == False:
                break
            if iteration_1((6, 9), (0, 1), (6, 9), random_numbers) == False:
                break
            else:
                sudoku.append(random_numbers)
                break

        while len(sudoku) == 2:
            if iteration_1((0, 3), (0, 2), (0, 3), random_numbers) == False:
                break
            if iteration_1((3, 6), (0, 2), (3, 6), random_numbers) == False:
                break
            if iteration_1((6, 9), (0, 2), (6, 9), random_numbers) == False:
                break
            else:
                sudoku.append(random_numbers)
                break

        while len(sudoku) == 3:
            if iteration_2((0, 3), (0, 3), random_numbers) == False:
                break
            if iteration_2((3, 6), (0, 3), random_numbers) == False:
                break
            if iteration_2((6, 9), (0, 3), random_numbers) == False:
                break
            else:
                sudoku.append(random_numbers)
                break

        while len(sudoku) == 4:
            if iteration_1((0, 3),(3, 4), (0, 3), random_numbers) == False or iteration_2((0, 3), (0, 3), random_numbers) == False:
                break
            if iteration_1((3, 6),(3, 4), (3, 6), random_numbers) == False or iteration_2((3, 6), (0, 3), random_numbers) == False:
                break
            if iteration_1((6, 9),(3, 4), (6, 9), random_numbers) == False or iteration_2((6, 9), (0, 3), random_numbers) == False:
                break
            else:
                sudoku.append(random_numbers)
                break

        while len(sudoku) == 5:
            if iteration_1((0, 3),(3, 5), (0, 3), random_numbers) == False or iteration_2((0, 3), (0, 3), random_numbers) == False:
                break
            if iteration_1((3, 6),(3, 5), (3, 6), random_numbers) == False or iteration_2((3, 6), (0, 3), random_numbers) == False:
                break
            if iteration_1((6, 9),(3, 5), (6, 9), random_numbers) == False or iteration_2((6, 9), (0, 3), random_numbers) == False:
                break
            else:
                sudoku.append(random_numbers)
                break

        while len(sudoku) == 6:
            if iteration_2((0, 3), (0, 6), random_numbers) == False:
                break
            if iteration_2((3, 6), (0, 6), random_numbers) == False:
                break
            if iteration_2((6, 9), (0, 6), random_numbers) == False:
                break
            else:
                sudoku.append(random_numbers)
                break

        while len(sudoku) == 7:
            if iteration_1((0, 3),(6, 7), (0, 3), random_numbers) == False or iteration_2((0, 3), (0, 6), random_numbers) == False:
                break
            if iteration_1((3, 6),(6, 7), (3, 6), random_numbers) == False or iteration_2((3, 6), (0, 6), random_numbers) == False:
                break
            if iteration_1((6, 9),(6, 7), (6, 9), random_numbers) == False or iteration_2((6, 9), (0, 6), random_numbers) == False:
                break
            else:
                sudoku.append(random_numbers)
                break

        while len(sudoku) == 8:
            if iteration_1((0, 3),(6, 8), (0, 3), random_numbers) == False or iteration_2((0, 3), (0, 6), random_numbers) == False:
                break
            if iteration_1((3, 6),(6, 8), (3, 6), random_numbers) == False or iteration_2((3, 6), (0, 6), random_numbers) == False:
                break
            if iteration_1((6, 9),(6, 8), (6, 9), random_numbers) == False or iteration_2((6, 9), (0, 6), random_numbers) == False:
                break
            else:
                sudoku.append(random_numbers)
                print("\n""\n", sudoku[0], "\n", sudoku[1], "\n", sudoku[2], "\n", sudoku[3], "\n", sudoku[4], "\n", sudoku[5], "\n", sudoku[6], "\n", sudoku[7], "\n", sudoku[8])
                break

    if start_creating_maps[0] == True:
        new_map_open = open("valid_maps.txt", "a")
        for i in range(0, 9):
            new_map.append(sudoku[i])
        new_map_open.write("\n")
        new_map_open.write(f"{new_map}")
        new_map.clear()
        new_map_open.close()
        start_creating_maps.pop()
        start_creating_maps.append(False)
        sudoku.clear()
        callback_start_creating_maps()
        
        

    dpg.configure_item("loading", show = False)
    dpg.configure_item("funny_text", show = False)
    dpg.configure_item("minion", show = False)
    dpg.configure_item("funny_2", show = False)
    dpg.configure_item("funny_3", show = False)
    dpg.configure_item("funny_4", show = False)
    dpg.configure_item("generate_map", show = False)
    dpg.configure_item("start_game", show = True)
    new_text.pop()
    new_text.append(False)
    create_easy_board()
    
def callback_change_funny_text():
    while new_text[0] == True:
        dpg.set_value("funny_text", rd.choice(text.text_snippets))
        time.sleep(15)
    print("close thread 2")
    return

def callback_change_funny_text_2():
    time.sleep(30)
    if new_text[0] == True:
        dpg.configure_item("funny_2", show = True)
    time.sleep(15)
    if new_text[0] == True:
        dpg.configure_item("funny_3", show = True)
        time.sleep(15)
    if new_text[0] == True:
        dpg.configure_item("funny_4", show = True)
    print("close thread 3")
    return

def callback_set_to_number(sender, app_data):
    sound = get_value_sound()
    row_column = "".join(number for number in sender if number.isdecimal())
    row = int(row_column[0])
    column = int(row_column[1])
    new_number_image_type = "".join(number for number in app_data if number.isdecimal())
    new_number = int(new_number_image_type[0])
    old_number = sudoku[row - 1][column - 1]

    if app_data == f"image_{new_number}2":
        if old_number != new_number:
            print ("fudge")
            print(f"button_{row}_{column}")
            print(new_number)
            dpg.configure_item(f"button_{row}_{column}", texture_tag = f"image_{new_number}3")
            number_of_mistakes.append(0)
            dpg.set_value("mistakes", len(number_of_mistakes))
            if sound == "On":
                incorrect.play()
            time.sleep(1.5)
            dpg.configure_item(f"button_{row}_{column}", texture_tag = f"image_blank")
            
        if old_number == new_number:
            dpg.configure_item(sender, texture_tag = app_data)
            position = (((row - 1) * 9) + column) - 1
            easy_mode.remove(position)
            if sound == "On":
                correct.play()

            if len(easy_mode) == 0:
                print("win")
                dpg.configure_item("finish_popup", show = True)
                elapsed_time = dpg.get_value("timer")
                dpg.set_value("stat_time", f"Your time is: {elapsed_time}")
                dpg.set_value("stat_mistakes", f"Number of mistakes: {len(number_of_mistakes)}")
                timer_on.pop()
                timer_on.append(False)
                if sound == "On":
                    win_game.play()
        print(len(easy_mode))

    if app_data == f"image_{new_number}4":
        dpg.configure_item(sender, texture_tag = app_data)


def callback_start_game():
    sound = get_value_sound()
    dpg.configure_item("welcome_screen", show = False)
    dpg.configure_item("game_screen", show = True)
    dpg.set_primary_window("game_screen", True)
    if sound == "On":
        start_generating_map_sound.stop()

    thread4.daemon = True
    thread4.start()

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

def create_easy_board():
    easy_mode_values = rd.sample(range(0, 81), k = 43)
    for i in range(0, 43):
        easy_mode.append(easy_mode_values[i])
    print(easy_mode)
    flat_sudoku = sum(sudoku, [])
    print(flat_sudoku)
    for i in easy_mode: 
        flat_sudoku.pop(i)
        flat_sudoku.insert(i, 0)
    print("\n")

    test = []

    for row in range(1, 10):
        for column in range(1, 10):
            number_value = 9 * (row - 1) + (column - 1)
            test.append(flat_sudoku[number_value])
            print(flat_sudoku[number_value])
            if flat_sudoku[number_value] > 0:
                dpg.configure_item(f"button_{row}_{column}", texture_tag = f"image_{flat_sudoku[number_value]}1", payload_type = "no_change")
        print(test)
        test.clear()

def get_value_sound():
    sound = dpg.get_value("sound")
    return sound    

def load_image_resource(image_number, image_type):
    width, height, channels, data = dpg.load_image(f"resources/image_{image_number}{image_type}.png")
    return width, height, channels, data

def add_static_texture(image_number, image_type):
    dpg.add_static_texture(width = image_width[image_number - 1][image_type - 1], height = image_height[image_number - 1][image_type - 1], default_value = image_data[image_number - 1][image_type - 1], tag = f"image_{image_number}{image_type}")

thread1 = threading.Thread(target = callback_new_game_generate)
thread2 = threading.Thread(target = callback_change_funny_text)
thread3 = threading.Thread(target = callback_change_funny_text_2)
thread4 = threading.Thread(target = callback_start_timer)

image_width = []
image_height = []
image_channels = []
image_data = []

##############################################################################################################################################################################################

dpg.create_context()

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

with dpg.texture_registry():

    for image_number in range(1, 10):
        for image_type in range(1, 5):
            add_static_texture(image_number, image_type)

    dpg.add_static_texture(width = width_blank, height = height_blank, default_value = data_blank, tag = "image_blank")
    dpg.add_static_texture(width = width_reset, height = height_reset, default_value = data_reset, tag = "image_reset")

dpg.create_viewport(title = 'Sudoku', width = 600, height = 600, small_icon = "resources/icon.ico", large_icon = "resources/icon.ico", resizable = False)

with dpg.window(label = "Welcome screen", pos = (100, 100), tag = "welcome_screen"):
    with dpg.tree_node(label = "Difficulty:", default_open = True, bullet = True, leaf = True):
        dpg.add_radio_button(("Easy", "Medium", "Evil"), horizontal = True, default_value = "Easy")

    with dpg.tree_node(label = "Game mode:", default_open = True, bullet = True, leaf = True):
        dpg.add_radio_button(("Check continuously", "Check on finish"), horizontal = True, default_value = "Check continuously", tag = "game_mode_select")
        with dpg.tooltip("game_mode_select"):
            dpg.add_text(text.gamemode_continuous, bullet = True)
            dpg.add_text(text.gamemode_finish, bullet = True)

    with dpg.tree_node(label = "Sound:", default_open = True, bullet = True, leaf = True):
        dpg.add_radio_button(("On", "Off"), horizontal = True, default_value = "On", tag = "sound")

    with dpg.theme(tag = "button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, col.retro_red)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, col.retro_red)
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, col.retro_red)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 40)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 40, 20)

    dpg.add_button(label = "Start generating map", callback = callback_new_game, tag = "generate_map")
    dpg.bind_item_theme(dpg.last_item(), "button_theme")

    dpg.add_button(label = "Start creating maps", callback = callback_start_creating_maps)

    dpg.add_loading_indicator(label = "Creating new map", color = col.retro_red, secondary_color = col.retro_red, show = False, tag = "loading")
    dpg.add_text(rd.choice(text.text_snippets), show = False, tag = "funny_text")
    dpg.add_text("Please be patient, the minions are working slow today...", show = False, tag = "minion")
    dpg.add_text("Like really slow...", show = False, tag = "funny_2")
    dpg.add_text("Like really, really slow...", show = False, tag = "funny_3")
    dpg.add_text("Like really, really, really slow...", show = False, tag = "funny_4")

    dpg.add_button(label = "     Start game     ", callback = callback_start_game, show = False, tag = "start_game")
    dpg.bind_item_theme(dpg.last_item(), "button_theme")

with dpg.window(label = "Game screen", pos = (100, 100), show = False, tag = "game_screen"):
    for row in range(1, 10):
        with dpg.group(horizontal = True):
            for column in range(1, 10):
                dpg.add_image_button("image_blank", width = 30, height = 30, drop_callback = callback_set_to_number, payload_type = "strings", tag = f"button_{row}_{column}")
 
                if row > 0 and column == 9:
                    dpg.add_image_button(f"image_{row}2", width = 30, height = 30, indent = 450)
                    with dpg.drag_payload(parent = dpg.last_item(), drag_data = f"image_{row}2", payload_type = "strings"):
                        dpg.add_text(f"{row}")

                    dpg.add_image_button(f"image_{row}4", width = 30, height = 30, indent = 500)
                    with dpg.drag_payload(parent = dpg.last_item(), drag_data = f"image_{row}4", payload_type = "strings"):
                        dpg.add_text(f"{row}")

    dpg.add_image_button("image_reset", width = 30, height = 30, indent = 450, show = False)
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

    with dpg.tree_node(label = "Mistakes:", default_open = True, bullet = True, leaf = True):
        dpg.add_text("0", tag = "mistakes")

    with dpg.window(label = "Finish", modal = True, show = False, no_title_bar = True, tag = "finish_popup"):
        dpg.add_text("Congratulations, here are your stats:")
        dpg.add_separator()
        dpg.add_text("Your time is:", tag = "stat_time")
        dpg.add_text(f"Number of mistakes: 0", tag = "stat_mistakes")
        with dpg.group(horizontal=True):
            dpg.add_button(label = "OK", width = 75, callback = lambda: dpg.configure_item("finish_popup", show = False))




dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("welcome_screen", True)
dpg.start_dearpygui()
dpg.destroy_context()