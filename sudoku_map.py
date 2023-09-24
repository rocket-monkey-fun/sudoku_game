import random 
import time

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valid_map = []
new_map = []
stage = []
overtime = [False]
start_time= []
stop_creating = [False]

def func_start_creating_maps_button():
    start_time.clear()
    start_time.append(time.time())

    func_start_creating_maps()

def func_stop_creating_maps_button():
    stop_creating.clear()
    stop_creating.append(True)
    print("stopped")

def func_start_creating_maps():
    random_numbers_first_row = random.sample(numbers, k = 9)
    valid_map.append(random_numbers_first_row)

    while len(valid_map) != 9:
        current_time = time.time()
        elapsed_time = current_time - start_time[0]
        if elapsed_time > 8 or stop_creating[0] == True:
            break
        else:
            random_numbers = random.sample(numbers, k = 9)

            print(len(valid_map))

            while len(valid_map) == 1:
                if iteration_1((0, 3), (0, 1), (0, 3), random_numbers) == False:
                    break
                if iteration_1((3, 6), (0, 1), (3, 6), random_numbers) == False:
                    break
                if iteration_1((6, 9), (0, 1), (6, 9), random_numbers) == False:
                    break
                else:
                    valid_map.append(random_numbers)
                    break

            while len(valid_map) == 2:
                if iteration_1((0, 3), (0, 2), (0, 3), random_numbers) == False:
                    break
                if iteration_1((3, 6), (0, 2), (3, 6), random_numbers) == False:
                    break
                if iteration_1((6, 9), (0, 2), (6, 9), random_numbers) == False:
                    break
                else:
                    valid_map.append(random_numbers)
                    break

            while len(valid_map) == 3:
                if iteration_2((0, 3), (0, 3), random_numbers) == False:
                    break
                if iteration_2((3, 6), (0, 3), random_numbers) == False:
                    break
                if iteration_2((6, 9), (0, 3), random_numbers) == False:
                    break
                else:
                    valid_map.append(random_numbers)
                    break

            while len(valid_map) == 4:
                if iteration_1((0, 3), (3, 4), (0, 3), random_numbers) == False or iteration_2((0, 3), (0, 3), random_numbers) == False:
                    break
                if iteration_1((3, 6), (3, 4), (3, 6), random_numbers) == False or iteration_2((3, 6), (0, 3), random_numbers) == False:
                    break
                if iteration_1((6, 9), (3, 4), (6, 9), random_numbers) == False or iteration_2((6, 9), (0, 3), random_numbers) == False:
                    break
                else:
                    valid_map.append(random_numbers)
                    break

            while len(valid_map) == 5:
                if iteration_1((0, 3), (3, 5), (0, 3), random_numbers) == False or iteration_2((0, 3), (0, 3), random_numbers) == False:
                    break
                if iteration_1((3, 6), (3, 5), (3, 6), random_numbers) == False or iteration_2((3, 6), (0, 3), random_numbers) == False:
                    break
                if iteration_1((6, 9), (3, 5), (6, 9), random_numbers) == False or iteration_2((6, 9), (0, 3), random_numbers) == False:
                    break
                else:
                    valid_map.append(random_numbers)
                    break

            while len(valid_map) == 6:
                if iteration_2((0, 3), (0, 6), random_numbers) == False:
                    break
                if iteration_2((3, 6), (0, 6), random_numbers) == False:
                    break
                if iteration_2((6, 9), (0, 6), random_numbers) == False:
                    break
                else:
                    valid_map.append(random_numbers)
                    break

            while len(valid_map) == 7:
                if iteration_1((0, 3), (6, 7), (0, 3), random_numbers) == False or iteration_2((0, 3), (0, 6), random_numbers) == False:
                    break
                if iteration_1((3, 6), (6, 7), (3, 6), random_numbers) == False or iteration_2((3, 6), (0, 6), random_numbers) == False:
                    break
                if iteration_1((6, 9), (6, 7), (6, 9), random_numbers) == False or iteration_2((6, 9), (0, 6), random_numbers) == False:
                    break
                else:
                    valid_map.append(random_numbers)
                    break

            while len(valid_map) == 8:
                if iteration_1((0, 3), (6, 8), (0, 3), random_numbers) == False or iteration_2((0, 3), (0, 6), random_numbers) == False:
                    break
                if iteration_1((3, 6), (6, 8), (3, 6), random_numbers) == False or iteration_2((3, 6), (0, 6), random_numbers) == False:
                    break
                if iteration_1((6, 9), (6, 8), (6, 9), random_numbers) == False or iteration_2((6, 9), (0, 6), random_numbers) == False:
                    break
                else:
                    valid_map.append(random_numbers)
                    break

    if len(valid_map) != 9 and stop_creating[0] == False:
        func_start_creating_maps_button()

    if stop_creating[0] == False:
        new_map_open = open("valid_maps.txt", "a")
        for i in range(0, 9):
            new_map.append(valid_map[i])
        new_map_open.write("\n")
        new_map_open.write(f"{new_map}")
        new_map.clear()
        new_map_open.close()
        valid_map.clear()
        func_start_creating_maps_button()

def iteration_1(range_i, range_j, range_k, random_numbers):
    for i in range(range_i[0], range_i[1]):
        for j in range(range_j[0], range_j[1]):
            for k in range(range_k[0], range_k[1]):
                if random_numbers[i] != valid_map[j][k]:
                    stage.append(1)
                    if len(stage) == 9:
                        stage.clear()
                else:
                    stage.clear()
                    return False
                
def iteration_2(range_i, range_j, random_numbers):
    for i in range(range_i[0], range_i[1]):
        for j in range(range_j[0], range_j[1]):
            if random_numbers[i] != valid_map[j][i]:
                stage.append(1)
                if len(stage) == 9:
                    stage.clear()
            else:
                stage.clear()
                return False