import random as rd
import dearpygui.dearpygui as dpg
import pygame
import text
import time
import threading
import colors as col

pygame.init()
start_generating_map_sound = pygame.mixer.Sound("resources/start_gereating_map.wav")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
stage = []
sudoku = []
easy_mode = []
new_text = [True]
number_of_mistakes = []

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

def callback_new_game(sender, app_data):
    sound = get_value_sound()

    dpg.configure_item("loading", show = True)
    dpg.configure_item("funny_text", show = True)
    dpg.configure_item("minion", show = True)

    if sound == "On":
        start_generating_map_sound.play()

    sudoku.clear()

    random_numbers_first_row = rd.sample(numbers, k = 9)
    sudoku.append(random_numbers_first_row)

    thread1.daemon = True
    thread1.start()
    thread2.daemon = True
    thread2.start()
    thread3.daemon = True
    thread3.start()

def callback_new_game_generate():
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
    dpg.configure_item(sender, texture_tag = app_data)
    row_column = "".join(number for number in sender if number.isdecimal())
    row = int(row_column[0])
    column = int(row_column[1])
    new_number = int("".join(number for number in app_data if number.isdecimal()))
    old_number = sudoku[row - 1][column - 1]

    if old_number != new_number:
        print ("fudge")
        print(f"button_{row}_{column}")
        dpg.configure_item(f"button_{row}_{column}", texture_tag = f"image_{new_number}_c")
        time.sleep(2)
        dpg.configure_item(f"button_{row}_{column}", texture_tag = f"image_0_a")
        number_of_mistakes.append(0)
        dpg.set_value("mistakes", f"Number of mistakes: {len(number_of_mistakes)}")
    
    if old_number == new_number:
        position = (((row - 1) * 9) + column) - 1
        easy_mode.remove(position)

        if len(easy_mode) == 0:
            print("win")
            dpg.configure_item("finish_popup", show = True)
            dpg.set_value("stat_mistakes", f"Number of mistakes: {len(number_of_mistakes)}")

    print(len(easy_mode))

def callback_start_game():
    dpg.configure_item("welcome_screen", show = False)
    dpg.configure_item("game_screen", show = True)
    dpg.set_primary_window("game_screen", True)

    #thread4.daemon = True
    #thread4.start()

def callback_start_timer():
    start_time = time.time()

    while 5 > 4:
        mid_time = time.time()
        elapsed_time = int(round(abs(mid_time - start_time), 0))
        if elapsed_time <= 9:
            dpg.set_value("timer", f"00:0{elapsed_time}")
        if elapsed_time in range(10, 61):
            dpg.set_value("timer", f"00:{elapsed_time}")

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
            dpg.configure_item(f"button_{row}_{column}", texture_tag = f"image_{flat_sudoku[number_value]}_a")
            if flat_sudoku[number_value] > 0:
                dpg.configure_item(f"button_{row}_{column}", payload_type = "no_change")
        print(test)
        test.clear()

def get_value_sound():
    sound = dpg.get_value("sound")
    return sound

thread1 = threading.Thread(target = callback_new_game_generate)
thread2 = threading.Thread(target = callback_change_funny_text)
thread3 = threading.Thread(target = callback_change_funny_text_2)
#thread4 = threading.Thread(target = callback_start_timer)

##############################################################################################################################################################################################

dpg.create_context()

width_0_a, height_0_a, channels_0_a, data_0_a = dpg.load_image("resources/image_0_a.png")

width_1_a, height_1_a, channels_1_a, data_1_a = dpg.load_image("resources/image_1_a.png")
width_1_b, height_1_b, channels_1_b, data_1_b = dpg.load_image("resources/image_1_b.png")
width_1_c, height_1_c, channels_1_c, data_1_c = dpg.load_image("resources/image_1_c.png")

width_2_a, height_2_a, channels_2_a, data_2_a = dpg.load_image("resources/image_2_a.png")
width_2_b, height_2_b, channels_2_b, data_2_b = dpg.load_image("resources/image_2_b.png")
width_2_c, height_2_c, channels_2_c, data_2_c = dpg.load_image("resources/image_2_c.png")

width_3_a, height_3_a, channels_3_a, data_3_a = dpg.load_image("resources/image_3_a.png")
width_3_b, height_3_b, channels_3_b, data_3_b = dpg.load_image("resources/image_3_b.png")
width_3_c, height_3_c, channels_3_c, data_3_c = dpg.load_image("resources/image_3_c.png")

width_4_a, height_4_a, channels_4_a, data_4_a = dpg.load_image("resources/image_4_a.png")
width_4_b, height_4_b, channels_4_b, data_4_b = dpg.load_image("resources/image_4_b.png")
width_4_c, height_4_c, channels_4_c, data_4_c = dpg.load_image("resources/image_4_c.png")

width_5_a, height_5_a, channels_5_a, data_5_a = dpg.load_image("resources/image_5_a.png")
width_5_b, height_5_b, channels_5_b, data_5_b = dpg.load_image("resources/image_5_b.png")
width_5_c, height_5_c, channels_5_c, data_5_c = dpg.load_image("resources/image_5_c.png")

width_6_a, height_6_a, channels_6_a, data_6_a = dpg.load_image("resources/image_6_a.png")
width_6_b, height_6_b, channels_6_b, data_6_b = dpg.load_image("resources/image_6_b.png")
width_6_c, height_6_c, channels_6_c, data_6_c = dpg.load_image("resources/image_6_c.png")

width_7_a, height_7_a, channels_7_a, data_7_a = dpg.load_image("resources/image_7_a.png")
width_7_b, height_7_b, channels_7_b, data_7_b = dpg.load_image("resources/image_7_b.png")
width_7_c, height_7_c, channels_7_c, data_7_c = dpg.load_image("resources/image_7_c.png")

width_8_a, height_8_a, channels_8_a, data_8_a = dpg.load_image("resources/image_8_a.png")
width_8_b, height_8_b, channels_8_b, data_8_b = dpg.load_image("resources/image_8_b.png")
width_8_c, height_8_c, channels_8_c, data_8_c = dpg.load_image("resources/image_8_c.png")

width_9_a, height_9_a, channels_9_a, data_9_a = dpg.load_image("resources/image_9_a.png")
width_9_b, height_9_b, channels_9_b, data_9_b = dpg.load_image("resources/image_9_b.png")
width_9_c, height_9_c, channels_9_c, data_9_c = dpg.load_image("resources/image_9_c.png")

width_99, height_99, channels_99, data_99 = dpg.load_image("resources/image_99.png")

with dpg.texture_registry():
    dpg.add_static_texture(width = width_0_a, height = height_0_a, default_value = data_0_a, tag = "image_0_a")
    
    dpg.add_static_texture(width = width_1_a, height = height_1_a, default_value = data_1_a, tag = "image_1_a")
    dpg.add_static_texture(width = width_1_b, height = height_1_b, default_value = data_1_b, tag = "image_1_b")
    dpg.add_static_texture(width = width_1_c, height = height_1_c, default_value = data_1_c, tag = "image_1_c")

    dpg.add_static_texture(width = width_2_a, height = height_2_a, default_value = data_2_a, tag = "image_2_a")
    dpg.add_static_texture(width = width_2_b, height = height_2_b, default_value = data_2_b, tag = "image_2_b")
    dpg.add_static_texture(width = width_2_c, height = height_2_c, default_value = data_2_c, tag = "image_2_c")

    dpg.add_static_texture(width = width_3_a, height = height_3_a, default_value = data_3_a, tag = "image_3_a")
    dpg.add_static_texture(width = width_3_b, height = height_3_b, default_value = data_3_b, tag = "image_3_b")
    dpg.add_static_texture(width = width_3_c, height = height_3_c, default_value = data_3_c, tag = "image_3_c")

    dpg.add_static_texture(width = width_4_a, height = height_4_a, default_value = data_4_a, tag = "image_4_a")
    dpg.add_static_texture(width = width_4_b, height = height_4_b, default_value = data_4_b, tag = "image_4_b")
    dpg.add_static_texture(width = width_4_c, height = height_4_c, default_value = data_4_c, tag = "image_4_c")

    dpg.add_static_texture(width = width_5_a, height = height_5_a, default_value = data_5_a, tag = "image_5_a")
    dpg.add_static_texture(width = width_5_b, height = height_5_b, default_value = data_5_b, tag = "image_5_b")
    dpg.add_static_texture(width = width_5_c, height = height_5_c, default_value = data_5_c, tag = "image_5_c")

    dpg.add_static_texture(width = width_6_a, height = height_6_a, default_value = data_6_a, tag = "image_6_a")
    dpg.add_static_texture(width = width_6_b, height = height_6_b, default_value = data_6_b, tag = "image_6_b")
    dpg.add_static_texture(width = width_6_c, height = height_6_c, default_value = data_6_c, tag = "image_6_c")

    dpg.add_static_texture(width = width_7_a, height = height_7_a, default_value = data_7_a, tag = "image_7_a")
    dpg.add_static_texture(width = width_7_b, height = height_7_b, default_value = data_7_b, tag = "image_7_b")
    dpg.add_static_texture(width = width_7_c, height = height_7_c, default_value = data_7_c, tag = "image_7_c")

    dpg.add_static_texture(width = width_8_a, height = height_8_a, default_value = data_8_a, tag = "image_8_a")
    dpg.add_static_texture(width = width_8_b, height = height_8_b, default_value = data_8_b, tag = "image_8_b")
    dpg.add_static_texture(width = width_8_c, height = height_8_c, default_value = data_8_c, tag = "image_8_c")

    dpg.add_static_texture(width = width_9_a, height = height_9_a, default_value = data_9_a, tag = "image_9_a")
    dpg.add_static_texture(width = width_9_b, height = height_9_b, default_value = data_9_b, tag = "image_9_b")
    dpg.add_static_texture(width = width_9_c, height = height_9_c, default_value = data_9_c, tag = "image_9_c")

    dpg.add_static_texture(width = width_99, height = height_99, default_value = data_99, tag = "image_99")

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
                dpg.add_image_button("image_0_a", width = 30, height = 30, drop_callback = callback_set_to_number, payload_type = "strings", tag = f"button_{row}_{column}")
 
                if row > 0 and column == 9:
                    dpg.add_image_button(f"image_{row}_b", width = 30, height = 30, indent = 450)
                    with dpg.drag_payload(parent = dpg.last_item(), drag_data = f"image_{row}_b", payload_type = "strings"):
                        dpg.add_text(f"{row}")

    dpg.add_image_button("image_99", width = 30, height = 30, indent = 450)
    with dpg.drag_payload(parent = dpg.last_item(), drag_data = "image_0_a", payload_type = "strings"):
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

    dpg.add_text("Instructions:", bullet = True)
    dpg.add_text("Drag and drop the desired number from the right hand side to the target cell.", bullet = True)
    dpg.add_text("Use the empty block to reset a value.", bullet = True)
    dpg.add_text("Have fun!", bullet = True)

    dpg.add_text("Time: 00:00", tag = "timer")
    dpg.add_text("Number of mistakes: 0", tag = "mistakes")

    with dpg.window(label = "Finish", modal = True, show = False, no_title_bar = True, tag = "finish_popup"):
        dpg.add_text("Congratulations, here are your stats:")
        dpg.add_separator()
        dpg.add_text("Your time:")
        dpg.add_text(f"Number of mistakes: 0", tag = "stat_mistakes")
        with dpg.group(horizontal=True):
            dpg.add_button(label = "OK", width = 75, callback = lambda: dpg.configure_item("finish_popup", show = False))




dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("welcome_screen", True)
dpg.start_dearpygui()
dpg.destroy_context()