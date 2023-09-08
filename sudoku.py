import random as rd
import dearpygui.dearpygui as dpg
import funny_text
import time
import threading

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
stage = []
sudoku = []
new_text = [True]

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
    dpg.configure_item("loading", show = True)
    dpg.configure_item("funny_text", show = True)
    dpg.configure_item("minion", show = True)

    sudoku.clear()

    random_numbers_first_row = rd.sample(numbers, k = 9)
    sudoku.append(random_numbers_first_row)

    thread1.start()
    thread2.start()
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
    
def callback_change_funny_text():
    while new_text[0] == True:
        dpg.set_value("funny_text", rd.choice(funny_text.text_snippets))
        time.sleep(15)

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

def callback_set_1(sender, app_data):
    dpg.configure_item(sender, texture_tag = app_data)

def callback_start_game():
    dpg.configure_item("welcome_screen", show = False)
    dpg.configure_item("game_screen", show = True)
    dpg.set_primary_window("game_screen", True)


thread1 = threading.Thread(target = callback_new_game_generate)
thread2 = threading.Thread(target = callback_change_funny_text)
thread3 = threading.Thread(target = callback_change_funny_text_2)

##############################################################################################################################################################################################

dpg.create_context()

width_0, height_0, channels_0, data_0 = dpg.load_image("resources\image_0.png")
width_1, height_1, channels_1, data_1 = dpg.load_image("resources\image_1.png")
width_2, height_2, channels_2, data_2 = dpg.load_image("resources\image_2.png")
width_3, height_3, channels_3, data_3 = dpg.load_image("resources\image_3.png")
width_4, height_4, channels_4, data_4 = dpg.load_image("resources\image_4.png")
width_5, height_5, channels_5, data_5 = dpg.load_image("resources\image_5.png")
width_6, height_6, channels_6, data_6 = dpg.load_image("resources\image_6.png")
width_7, height_7, channels_7, data_7 = dpg.load_image("resources\image_7.png")
width_8, height_8, channels_8, data_8 = dpg.load_image("resources\image_8.png")
width_9, height_9, channels_9, data_9 = dpg.load_image("resources\image_9.png")

with dpg.texture_registry():
    dpg.add_static_texture(width = width_0, height = height_0, default_value = data_0, tag = "image_0")
    dpg.add_static_texture(width = width_1, height = height_1, default_value = data_1, tag = "image_1")
    dpg.add_static_texture(width = width_2, height = height_2, default_value = data_2, tag = "image_2")
    dpg.add_static_texture(width = width_3, height = height_3, default_value = data_3, tag = "image_3")
    dpg.add_static_texture(width = width_4, height = height_4, default_value = data_4, tag = "image_4")
    dpg.add_static_texture(width = width_5, height = height_5, default_value = data_5, tag = "image_5")
    dpg.add_static_texture(width = width_6, height = height_6, default_value = data_6, tag = "image_6")
    dpg.add_static_texture(width = width_7, height = height_7, default_value = data_7, tag = "image_7")
    dpg.add_static_texture(width = width_8, height = height_8, default_value = data_8, tag = "image_8")
    dpg.add_static_texture(width = width_9, height = height_9, default_value = data_9, tag = "image_9")

dpg.create_viewport(title = 'Sudoku', width = 600, height = 600, small_icon = "resources\icon.ico", large_icon = "resources\icon.ico", resizable = False)

with dpg.window(label = "Welcome screen", pos = (100, 100), tag = "welcome_screen"):

    with dpg.theme(tag = "button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [93, 150, 120])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [93, 150, 120])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [93, 150, 120])
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 40)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 40, 20)

    dpg.add_button(label = "Start generating map", callback = callback_new_game, tag = "generate_map")
    dpg.bind_item_theme(dpg.last_item(), "button_theme")

    dpg.add_loading_indicator(label = "Creating new map", color = [93, 150, 120], secondary_color = [93, 150, 120], show = False, tag = "loading")
    dpg.add_text(rd.choice(funny_text.text_snippets), show = False, tag = "funny_text")
    dpg.add_text("Please be patient, the minions are working slow today...", show = False, tag = "minion")
    dpg.add_text("Like really slow...", show = False, tag = "funny_2")
    dpg.add_text("Like really, really slow...", show = False, tag = "funny_3")
    dpg.add_text("Like really, really, really slow...", show = False, tag = "funny_4")


    dpg.add_button(label = "Start game", callback = callback_start_game, show = False, tag = "start_game")
    dpg.bind_item_theme(dpg.last_item(), "button_theme")

with dpg.window(label = "Game screen", pos = (100, 100), show = False, tag = "game_screen"):
    for row in range(1, 10):
        with dpg.group(horizontal = True):
            for column in range(1, 10):
                dpg.add_image_button("image_0", width = 30, height = 30, drop_callback = callback_set_1, payload_type = "strings", tag = f"button_{row}_{column}")
 
                if row > 0 and column == 9:
                    dpg.add_image_button(f"image_{row}", width = 30, height = 30, indent = 450)
                    with dpg.drag_payload(parent = dpg.last_item(), drag_data = f"image_{row}", payload_type = "strings"):
                        dpg.add_text(f"{row}")

    dpg.add_image_button("image_0", width = 30, height = 30, indent = 450)
    with dpg.drag_payload(parent = dpg.last_item(), drag_data = "image_0", payload_type = "strings"):
        dpg.add_text("reset")

    with dpg.draw_layer():
        dark_grey = [117, 117, 117]

        dpg.draw_rectangle((0, 0), (134, 118), color = dark_grey)
        dpg.draw_rectangle((134, 0), (272, 118), color = dark_grey)
        dpg.draw_rectangle((272, 0), (407, 118), color = dark_grey)

        dpg.draw_rectangle((0, 118), (134, 238), color = dark_grey)
        dpg.draw_rectangle((134, 118), (272, 238), color = dark_grey)
        dpg.draw_rectangle((272, 118), (407, 238), color = dark_grey)

        dpg.draw_rectangle((0, 238), (134, 357), color = dark_grey)
        dpg.draw_rectangle((134, 238), (272, 357), color = dark_grey)
        dpg.draw_rectangle((272, 238), (407, 357), color = dark_grey)

        dpg.draw_rectangle((0, 0), (407, 357), color = [93, 150, 120], thickness = 2)

    dpg.add_text("Instructions:", bullet = True)
    dpg.add_text("Drag and drop the desired number from the right hand side to the target cell.", bullet = True)
    dpg.add_text("Use the empty block to reset a value.", bullet = True)
    dpg.add_text("Have fun!", bullet = True)




dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("welcome_screen", True)
dpg.start_dearpygui()
dpg.destroy_context()