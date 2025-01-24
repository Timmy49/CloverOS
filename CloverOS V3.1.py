# -*- coding: utf-8 -*-
"""
CloverOS.py
comments,
1. separate modules
2. logging for debug
3. saving data
3.1 what to save

4. data structure, e.g. inventory
4.1 data structure, character
4.2 data structure, about battling, weapons, gems

X. unittest, test driven development

5. movement is infinite, random the scene, not hard coding
5.1 what may happen after move

6. inspect the environment, <--  llm providing the description
6.1 llm_env: describe the environment
6.2 llm_char: describe the chara or enemy, objects (gem etc)
6.3 llm_story:
7. Character
8. Enemy
8.1 random combination design
8.2. Battle
8.3. Escape
8.4. inspect enemy

9. weapons
10. gems
11. clothing


"""

# Guessing Game
def guessing_game():
  number = random.randint(1, 10)
  while True:
    # validate the input
    try:
      guess = int(input("\nGuess a number between 1 and 10 ( 0 to exit )\nAnswer: "))
    except ValueError:
      print("\nInvalid input.")
      continue

    # guessing the number
    if guess == 0:
      break
    elif guess > number:
      print("Too high")
    elif guess < number:
      print("Too low!")
    else:
      print("\nYou guessed correctly!")
      break

# Encrypt / Decryption System
def vigenere_cipher(text, key, mode="encrypt"):
  
    result_text = ""
    key = key.upper()  # Normalize key to uppercase
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():  # Process alphabetic characters only
            key_shift = ord(key[i % key_length]) - ord('A')  # Calculate key shift
            
            # Flip the direction of the shift for decryption
            if mode == "decrypt":
                key_shift = -key_shift
            
            # Handle uppercase and lowercase letters separately
            if char.islower():
                result_char = chr(((ord(char) - ord('a') + key_shift) % 26) + ord('a'))
            else:
                result_char = chr(((ord(char) - ord('A') + key_shift) % 26) + ord('A'))
            
            result_text += result_char
        else:
            result_text += char  # Keep non-alphabetic characters unchanged
    
    return result_text

# Lottery Game
def lottery_game():
  import random
  numbers = [random.randint(1, 5), random.randint(6, 10), random.randint(11, 15), random.randint(16, 20), random.randint(21, 25), random.randint(26, 30)]
  winning_number = (numbers[random.randint(0, 2)])
  try:
    entry_number = int(input("\nWhich is the lottery number?\n" + str(numbers) + "\nAnswer: "))
    if entry_number == winning_number:
      print("\nYou won!")
    else:
      print("\nYou lost! Lottery number was " + str(winning_number))
  except ValueError:
    print("\nInvalid input.")


# Calculator
def calculator():
  while True:
    operation = input("\nWhat order of operation would you like to perform? ( Addition, Subtraction, Multiplication, Division )\nAnswer: ").lower()
    if operation == "addition":
      try:
        number1 = int(input("\nWhat is the first number?\nAnswer: "))
        number2 = int(input("\nWhat is the second number?\nAnswer: "))
        print(str(number1) + " + " + str(number2) + " = " + str(number1 + number2))
      except ValueError:
        print("\nInvalid Input.")
    elif operation == "subtraction":
      try:
        number1 = int(input("\nWhat is the first number?\nAnswer: "))
        number2 = int(input("\nWhat is the second number?\nAnswer: "))
        print(str(number1) + " - " + str(number2) + " = " + str(number1 - number2))
      except ValueError:
        print("\nInvalid Input.")
    elif operation == "multiplication":
      try:
        number1 = int(input("\nWhat is the first number?\nAnswer: "))
        number2 = int(input("\nWhat is the second number?\nAnswer: "))
        print(str(number1) + " x " + str(number2) + " = " + str(number1 * number2))
      except ValueError:
        print("\nInvalid Input.")
    elif operation == "division":
      try:
        number1 = int(input("\nWhat is the first number?\nAnswer: "))
        number2 = int(input("\nWhat is the second number?\nAnswer: "))
        print(str(number1) + " ÷ " + str(number2) + " = " + str(number1 / number2))
      except ValueError:
        print("\nInvalid Input.")
    elif operation == "exit":
      break
    else:
      print("\nInvalid Operation.")


# To Do
tasks = []
def todo():
  global tasks
  while True:
    print("\nTasks:\n" + str(tasks))
    if tasks == []:
      print("\nNo tasks currently.")
    todo_action = input("\nWhat would you like to do? \n1. Add Task\n2. Remove Task\n3. Export Tasks\n4. Exit\n( Type the command )\nAnswer: ").lower()
    if todo_action == "add task":
      add_task = input("\nWhat task would you like to add?\nAnswer: ").lower()
      tasks.append(add_task)
      print("\nTask Added.")
    elif todo_action == "remove task":
      remove_task = input("\nWhat task would you like to mark as done?\nAnswer: ").lower()
      try:
        tasks.remove(remove_task)
        print("\nTask Removed.")
      except ValueError:
        print("\nInvalid Task.")
    elif todo_action == "export tasks":
      todo_file_name = input("\nName your todo list file.\nAnswer: ")
      todo_file = open(todo_file_name, 'w')
      todo_file.write(str(tasks))
      todo_file.close()
      print("\nTasks Exported.")
    elif todo_action == "exit":
      break
    else:
      print("\nInvalid Action.")
# Notes
notes = []
def notesapp():
  while True:
    global notes
    if notes == []:
      print("\nNo notes currently.")
    else:
      print("\nNotes:\n")
      for note in notes:
        print(note)
    notes_action = input("\nWhat would you like to do? \n1. Add Note\n2. Remove All\n3. Exit\n( Type the command )\nAnswer: ").lower()
    if notes_action == "add note":
      add_note = input("\nWhat note would you like to add?\nAnswer: ").lower()
      notes.append(add_note)
      print("\nNote Added.")
    elif notes_action == "remove all":
      notes.clear()
      print("\nAll notes removed.")
    elif notes_action == "exit":
      break
    else:
      print("\nInvalid Action.")


# Settings
developer_mode = False
def settingsapp():
  global developer_mode, username
  while True:
    settings_action = input("\nWhat would you like to do? \n1. Turn on / off developer mode ( Type: 'developer')\n2. Edit Username\n3. Credits\n4. Exit \nAnswer: ").lower()
    if settings_action == "developer":
      if developer_mode == True:
        developer_mode = False
        print("\nDeveloper Mode Turned Off.")
      else:
        developer_mode = True
        print("\nDeveloper Mode Turned On.")
    elif settings_action == "exit":
      break
    elif settings_action == "edit username":
      username = input("\nNew username: ")
      file_path = "BIOS_2.txt"
      if os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write(username)
      else:
        print("\nWarning: Your BIOS save file is corrupt.")
        time.sleep(1)
        print("\nStarting Recovery Mode...")
        time.sleep(2)
        print("\nManual Options:\n1. Locate BIOS Files\n2. Delete corrupted BIOS files, and reboot.")
        
    elif settings_action == "credits":
      print("\nDeveloper: Timmy\nTesters: Jayaprakash Etash, Avisha Murty, Timmy\nGemini + ChatGPT assisting in coding.\nMust read: Python Essentials; for dummies\nCoding IDLE: Google Colab")
    else:
      print("\nInvalid Action.")


# Help
def helpapp():
  print("\nApplications:\n1. Games\n2. Notes\n3. Bonnet\n4. Calculator\n5. Todo\n6. Encryptor\n7. Settings\n8. Help\n9. Exit\n\nType the name of the application to open. Commands are all common sense, type exit to exit, and help for help!\n\nFor any bugs, please contact ['SeanliOFS@gmail.com']")

"""**Bonnet Game**"""

import time
# Bonnet Game
def bonnet():
  # Game Status
  global bonnet_admin_complex
  game_status = input("\nNew game or Continue game?\nAnswer: ").lower()
  if game_status == "new game":
    bonnet_admin_complex = False
    bonnet_new_game()
  elif game_status == "continue game":
    bonnet_admin_complex = False
    bonnet_import_save()
  else:
    if game_status == "exit":
      print("\nExit")
    else:
      print("\nInvalid Action.")
# Bonnet - New Game
def bonnet_new_game():
  global player_x, player_y, inventory_str, progress_str, inventory_gui, progress_gui, has_CPU_int, has_shovel_int, has_battery_int, has_key_int, cpu_eat
  player_x = 1
  player_y = 1
  inventory_str = "0"
  progress_str = "0"
  inventory_gui = []
  progress_gui = []
  has_CPU_int = 0
  has_shovel_int = 0
  has_battery_int = 0
  has_key_int = 0
  cpu_eat = 1
  location_text()
  location_action()
# Bonnet - Continued Game
def bonnet_import_save():
  save_option = input("\n\nSelect a import option: File / Character String ( File / String )\nAnswer: ").lower()
  global player_x, player_y, inventory_str, progress_str, developer_mode, has_key_int, has_key, progress_gui, inventory_gui, has_shovel_int, has_CPU_int, has_battery_int, has_shovel, has_CPU, has_battery
  if save_option == "file":
    try:
      save_file_open = open('bonnet_savefile_cloverOS.txt', 'r')
      save_file_data = save_file_open.read()
      save_file_open.close()
      player_x = int(save_file_data[0])
      player_y = int(save_file_data[1])

      # Extract inventory + recognising item
      inventory_str = str(save_file_data[2])
      try:
        if inventory_str == "0":
          inventory_gui = []
        elif inventory_str == "1":
          inventory_gui = ["key"]
        elif inventory_str == "2":
          inventory_gui = ["shovel"]
        elif inventory_str == "3":
          inventory_gui = ["cpu card"]
        elif inventory_str == "4":
          inventory_gui = ["battery"]
        elif inventory_str == "5":
          inventory_gui = ["key", "cpu card"]
        elif inventory_str == "6":
          inventory_gui = ["key", "battery"]
        elif inventory_str == "7":
          inventory_gui = ["key", "shovel"]
        elif inventory_str == "8":
          inventory_gui = ["key", "cpu card", "shovel"]
        elif inventory_str == "9":
          inventory_gui = ["key", "battery", "shovel"]
        elif inventory_str == "a":
          inventory_gui = ["key", "cpu card", "battery"]
        elif inventory_str == "b":
          inventory_gui = ["key", "cpu card", "battery", "shovel"]
        elif inventory_str == "c":
          inventory_gui = ["shovel", "battery"]
        elif inventory_str == "d":
          inventory_gui = ["shovel", "cpu card"]
        elif inventory_str == "e":
          inventory_gui = ["shovel", "battery", "cpu card"]
        elif inventory_str == "f":
          inventory_gui = ["battery", "cpu card"]
        else:
          print("\nInvlid save file. Try again.")
          bonnet_import_save()
      except (ValueError, IndexError):
        print("\nInvalid save file. Try again.")
        bonnet_import_save()

      # Extract progress + recognising progress
      progress_str = int(save_file_data[3])
      try:
        if progress_str == 0:
          progress_gui = []
        elif progress_str == 1:
          progress_gui = ["shovelyes"]
        else:
          print("\nInvalid save file. Try again.")
          bonnet_import_save()
      except (ValueError, IndexError):
        print("\nInvalid save file. Try again.")
        bonnet_import_save()

      # Extract Shovel? CPU? Battery?
      has_shovel_int = int(save_file_data[4])
      has_CPU_int = int(save_file_data[5])
      has_battery_int = int(save_file_data[6])
      try:
        if has_shovel_int == 1:
          has_shovel = True
        elif has_shovel_int == 0:
          has_shovel = False
        else:
          print("\nInvalid save file. Try again.")
          bonnet_import_save()
      except (ValueError, IndexError):
        print("\nInvalid save file. Try again.")
        bonnet_import_save()
      try:
        if has_CPU_int == 1:
          has_CPU = True
        elif has_CPU_int == 0:
          has_CPU = False
        else:
          print("\nInvalid save file. Try again.")
          bonnet_import_save()
      except (ValueError, IndexError):
        print("\nInvalid save file. Try again.")
        bonnet_import_save()
      try:
        if has_battery_int == 1:
          has_battery = True
        elif has_battery_int == 0:
          has_battery = False
        else:
          print("\nInvalid save file. Try again.")
          bonnet_import_save
      except (ValueError, IndexError):
        print("\nInvalid save file. Try again.")
        bonnet_import_save()

      # Extract Key?
      has_key_int = int(save_file_data[7])
      try:
        if has_key_int == 1:
          has_key = True
        elif has_key_int == 0:
          has_key = False
        else:
          print("\nInvalid save file. Try again.")
      except (ValueError, IndexError):
        print("\nInvalid save file. Try again.")
          
      print("\nYour save:\n" + str(player_x) + str(player_y) + str(inventory_gui))
      player_x = int(player_x)
      player_y = int(player_y)
      location_text()
      location_action()
    except FileNotFoundError:
      print("\nNo save file found. Starting new game...")
      bonnet_new_game()
    except IndexError:
      print("\nInvalid save file. Try again.")
      bonnet_import_save()
  elif save_option == "string":
    save_str_open = input("\n\nEnter your save string.\nAnswer: ")
    try:
      save_file_data = save_str_open
      player_x = int(save_file_data[0])
      player_y = int(save_file_data[1])
      inventory_str = str(save_file_data[2])
      try:
        if inventory_str == "0":
          inventory_gui = []
        elif inventory_str == "1":
          inventory_gui = ["key"]
        elif inventory_str == "2":
          inventory_gui = ["shovel"]
        elif inventory_str == "3":
          inventory_gui = ["cpu card"]
        elif inventory_str == "4":
          inventory_gui = ["battery"]
        elif inventory_str == "5":
          inventory_gui = ["key", "cpu card"]
        elif inventory_str == "6":
          inventory_gui = ["key", "battery"]
        elif inventory_str == "7":
          inventory_gui = ["key", "shovel"]
        elif inventory_str == "8":
          inventory_gui = ["key", "cpu card", "shovel"]
        elif inventory_str == "9":
          inventory_gui = ["key", "battery", "shovel"]
        elif inventory_str == "a":
          inventory_gui = ["key", "cpu card", "battery"]
        elif inventory_str == "b":
          inventory_gui = ["key", "cpu card", "battery", "shovel"]
        elif inventory_str == "c":
          inventory_gui = ["shovel", "battery"]
        elif inventory_str == "d":
          inventory_gui = ["shovel", "cpu card"]
        elif inventory_str == "e":
          inventory_gui = ["shovel", "battery", "cpu card"]
        else:
          inventory_gui = ["battery", "cpu card"]
      except (ValueError, IndexError):
        print("\nInvalid save string. Try again.")
        bonnet_import_save()

      progress_str = int(save_file_data[3])
      try:
        if progress_str == 0:
          progress_gui = []
        elif progress_str == 1:
          progress_gui = ["shovelyes"]
      except (ValueError, IndexError):
        print("\nInvalid save string. Try again.")
        bonnet_import_save()

      # Extract Shovel? CPU? Battery?
      has_shovel_int = int(save_file_data[4])
      has_CPU_int = int(save_file_data[5])
      has_battery_int = int(save_file_data[6])
      try:
        if has_shovel_int == 1:
          has_shovel = True
        elif has_shovel_int == 0:
          has_shovel = False
        else:
          print("\nInvalid save string. Try again.")
          bonnet_import_save()
      except (ValueError, IndexError):
        print("\nInvalid save string. Try again.")
        bonnet_import_save()
      try:
        if has_CPU_int == 1:
          has_CPU = True
        elif has_CPU_int == 0:
          has_CPU = False
        else:
          print("\nInvalid save string. Try again.")
          bonnet_import_save()
      except (ValueError, IndexError):
        print("\nInvalid save string. Try again.")
        bonnet_import_save()
      try:
        if has_battery_int == 1:
          has_battery = True
        elif has_battery_int == 0:
          has_battery = False
        else:
          print("\nInvalid save string. Try again.")
          bonnet_import_save
      except (ValueError, IndexError):
        print("\nInvalid save string. Try again.")
        bonnet_import_save()

      # Extract Key?
      has_key_int = int(save_file_data[7])
      try:
        if has_key_int == 1:
          has_key = True
        elif has_key_int == 0:
          has_key = False
        else:
          print("\nInvalid save file. Try again.")
      except (ValueError, IndexError):
        print("\nInvalid save file. Try again.")
          
      print("\nYour save:\n" + str(player_x) + str(player_y) + str(inventory_gui))
      player_x = int(player_x)
      player_y = int(player_y)

      location_text()
      location_action()
    except IndexError:
      print("\nInvalid save string. Try again.")
      bonnet_import_save()
    except ValueError:
      print("\nInvalid save string. Try again.")
      bonnet_import_save()
  elif save_option == "exit":
    print("\nExit")
    home_screen()
  else:
    print("\nInvalid Action.")

# Bonnet - Location Text
def location_text():
  global player_x, player_y, progress_gui, inventory_gui, has_key_int, inventory_str, progress_str, developer_mode, bonnet_admin_complex, has_CPU_int, has_shovel_int, has_battery_int, has_key_int
  # Update inventory gui and str sync in background
  update_str_gui()
  # Add \n before every location text!!!
  # Y = 1
  if player_x == 1 and player_y == 1:
    print("\nYou find yourself standing in the middle of a dirt road. The road leads far off to the east. There are tall palm trees on the side of the walkway.")
  elif player_x == 2 and player_y == 1:
    print("\nThe ground is much softer here. The road leads to the east and west.")
  elif player_x == 3 and player_y == 1:
    print("\nThe road leads to the east and west. You notice another small road leading south.")
  elif player_x == 4 and player_y == 3:
    print("\nEast/West road.")
  elif player_x == 5 and player_y == 3:
    print("\nA tall, building stands in front of you. The road leads back to the west.")
  elif player_x == 6 and player_y == 3:
    print("\nYou're standing in the hallway of a tall, marble decorated building. There are doors leading to the north and south, and the hallway continues to the east and back to the west.")
  elif player_x == 6 and player_y == 4:
    # Computer Room
    print("\nAn old looking computer sits at the corner of the room.")
  # Y = 2
  elif player_x == 3 and player_y == 2:
    print("\nThere is a large pile of metal scraps here. The road continues to the north and south.")
  # Y = 3
  elif player_x == 3 and player_y == 3:
    print("\nThe road forks off to the east and west. The looks like it's been walked on before.")
    # MODIFY AFTER ADDING DROP COMMAND
    if has_key_int == 0:
      print("\nThere's a small, golden key lying on the floor.")
  elif player_x == 2 and player_y == 3:
    print("\nEast/West road.")
  elif player_x == 1 and player_y == 3:
    if has_battery_int == 1:
      print("\nOpened wooden chest.")
    else:    
      print("\nA large, wooden chest sits at the end of the dirt walkway. It's soft, brown colour blends into the road.")
  # Non - Existent Text
  else:
    print("\nThere is no description for this location yet. Current location: X = " + str(player_x) + ", Y = " + str(player_y) + ".")
  # Location XY for developer
  if developer_mode == True:
    if bonnet_admin_complex == True:
      print("\nGame Status:\n\nPosition:" + str(player_x) + " " + str(player_y) + "\nFalse Position Check:" + str(false_player_x) + " " + str(false_player_y) + "\nInventory_GUI:" + str(inventory_gui) + "\nProgress_GUI:" + str(progress_gui) + "\nInventory_STR:" + str(inventory_str) + "\nProgress_STR:" + str(progress_str) + "\nItem STR List:\n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nProgress STR List:\n1shovelyes" + "\nhas shovel / cpu / battery / key ID:" + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
    else:
      print("\nCurrent location: X = " + str(player_x) + ", Y = " + str(player_y))
# Bonnet - Action + Game Engine
def location_action():
  global cpu_eat, player_x, player_y, false_player_x, false_player_y, has_key_int, inventory_gui, progress_gui, inventory_str, progress_str, bonnet_action, developer_mode, bonnet_admin_complex, has_CPU_int, has_shovel_int, has_battery_int
  while True:
    bonnet_action = input("\nWhat would you like to do?\nAnswer: ").lower()
    # Movement
    false_player_x = player_x
    false_player_y = player_y
    # Important Note: Player starts bottom left of map. South is + 1Y, East is + 1X
    if bonnet_action == "east":
      false_player_x = player_x + 1
      run_movement()
    elif bonnet_action == "west":
      false_player_x = player_x - 1
      run_movement()
    elif bonnet_action == "south":
      false_player_y = player_y + 1
      run_movement()
    elif bonnet_action == "north":
      false_player_y = player_y - 1
      run_movement()


    # Inventory Command
    elif bonnet_action == "inventory":
      print("\n" + str(inventory_gui))
      location_text()
      location_action()


    # Save Command
    elif bonnet_action == "save":
      save_method = input("\n\nSelect a save option: File / Character String ( File / String )\nAnswer: ").lower()
      if save_method == "file":
        try:
          save_file = open('bonnet_savefile_cloverOS.txt', 'r+')
          save_file.write(str(player_x) + str(player_y) + str(inventory_str) + str(progress_str) + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
          save_file.close()
          print("\nSave file updated.")
          location_text()
          location_action()
        except FileNotFoundError:
          print("\nNo save file found. Creating new save file...")
          save_file = open('bonnet_savefile_cloverOS.txt', 'w')
          save_file.write(str(player_x) + str(player_y) + str(inventory_str) + str(progress_str) + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
          save_file.close()
          print("\nSave file created.")
          location_text()
          location_action()
      elif save_method == "string":
        print("\nYour save:\n" + str(player_x) + str(player_y) + str(inventory_str) + str(progress_str) + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
        location_text()
        location_action()
      elif save_method == "exit":
        location_text()
        location_action()
      else:
        print("\nInvalid Action.")
        location_text()
        location_action()


    # Exit
    elif bonnet_action == "exit":
      home_screen()
      break


    # Admin Command
    elif bonnet_action == "admin":
      if developer_mode == True:
        print("\n\nGame_Status:\n\nPosition:" + str(player_x) + " " + str(player_y) + "\nFalse Position Check:" + str(false_player_x) + " " + str(false_player_y) + "\nInventory_GUI:" + str(inventory_gui) + "\nProgress_GUI:" + str(progress_gui) + "\nInventory_STR:" + str(inventory_str) + "\nProgress_STR:" + str(progress_str) + "\nItem STR List:\n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nProgress STR List:\n1shovelyes" + "\nhas shovel / cpu / battery ID:" + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
        add_type = input("\nItem / Progress / Debug Mode ( I / P / D )\nAnswer: ").lower()
        if add_type == "i":
          add_item = str(input("\nItem? \n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nAnswer: "))
          try:
            if add_item == "0":
              inventory_gui = []
            elif add_item == "1":
              inventory_gui = ["key"]
            elif add_item == "2":
              inventory_gui = ["shovel"]
            elif add_item == "3":
              inventory_gui = ["cpu card"]
            elif add_item == "4":
              inventory_gui = ["battery"]
            elif add_item == "5":
              inventory_gui = ["key", "cpu card"]
            elif add_item == "6":
              inventory_gui = ["key", "battery"]
            elif add_item == "7":
              inventory_gui = ["key", "shovel"]
            elif add_item == "8":
              inventory_gui = ["key", "cpu card", "shovel"]
            elif add_item == "9":
              inventory_gui = ["key", "battery", "shovel"]
            elif add_item == "a":
              inventory_gui = ["key", "cpu card", "battery"]
            elif add_item == "b":
              inventory_gui = ["key", "cpu card", "battery", "shovel"]
            elif add_item == "c":
              inventory_gui = ["shovel", "battery"]
            elif add_item == "d":
              inventory_gui = ["shovel", "cpu card"]
            elif add_item == "e":
              inventory_gui = ["shovel", "battery", "cpu card"]
            elif add_item == "f":
              inventory_gui = ["battery", "cpu card"]
            else:
              print("\nTf you doing thats not valid\nYou're probably not even the developer")
              location_text()
              location_action()
          except ValueError:
            print("\nTf you doing thats not valid\nYou're probably not even the developer")
            location_text()
            location_action()
          inventory_str = add_item
          print("\nInventory set. Current inventory:" + str(inventory_gui))
          location_text()
          location_action()
        elif add_type == "p":
          add_progress = int(input("\nProgress? \n1shovelyes\nAnswer: "))
          try:
            if add_progress == 0:
              progress_gui = []
            elif add_progress == 1:
              progress_gui = ["shovelyes"]
            else:
              print("\nTf you doing thats not valid\nYou're probably not even the developer")
              location_text()
              location_action()
          except (ValueError, IndexError):
            print("\nTf you doing thats not valid\nYou're probably not even the developer")
            location_text()
            location_action()
          progress_str = add_progress
          print("\nComplete. Current progress:" + str(progress_gui))
          location_text()
          location_action()
        elif add_type == "d":
          if bonnet_admin_complex == True:
            bonnet_admin_complex = False
            print("\nDebug Mode Off.")
            location_text()
            location_action()
          else:
            print("\nDebug Mode On.")
            bonnet_admin_complex = True
            location_text()
            location_action()
        else:
          print("\nExited Admin.")
          location_text()
          location_action()
      else:
        print("\nInvalid Action. ( Turn on developer mode )")
        location_text()
        location_action()


    # Progress
    elif bonnet_action == "progress":
      if developer_mode == True:
        print(str(progress_gui))
        location_text()
        location_action()
      else:
        print("\nInvalid Action. ( Turn on developer mode )")
        location_text()
        location_action()
    # Help
    elif bonnet_action == "help":
      print("\n==== HELP START ====\n\nBonnet is a text based adventure game inspired by Dunnet ( Emacs ).\n\nList of commands:\n\n1. Move ( Type the direction to move, eg. 'north' to move north. )\n\n2. Inventory ( Type: 'inventory' )\n\n3. Dig ( Dig at your current position by typing: 'dig' )\n\n4. Search ( Type: 'search <direct object>' )\n\n5. Interact\nThe 'interact' command breaks down into 3 types of interactions.\n\nThe first interaction type are with NPCs.\n( Type: 'talk to <NPC Name>' to interact )\n\nThe second interaction type is to physically move something either in your surrounding or in your inventory.\n( Type: 'place <direct object> into / onto <indirect object>' )\n\nThe third interaction type is to examine an object around you or in your inventory. Note that examining an object does not physically interact with it; use 'search' instead.\n( Type: 'examine <direct object>' )\n\n6. Special actions:\n  • N / A\n\n==== HELP END ====")
      location_text()
      location_action()

    # Take
    elif "take" in bonnet_action:
      if "key" in bonnet_action:
        if player_x == 3 and player_y == 3:
          print("\nTaken.")
          inventory_gui.append("key")
          has_key_int = 1
          location_text()
          location_action()
        else:
          print("\nYou don't see that here.")
          location_text()
          location_action()
      else:
        print("\nYou don't see that here.")
        location_text()
        location_action()

    # Special Actions
    elif bonnet_action == "dig":
      if player_x == 2 and player_y == 1:
        if "shovel" in inventory_gui:
          if has_CPU_int == 0:
            print("\nYou found a cpu card.")
            inventory_gui.append("cpu card")
            has_CPU_int = 1
            location_text()
            location_action()
          else:
            print("\nYou've already dug here.")
        else:
          print("\nYou need a shovel to dig.")
          location_text()
          location_action()
      else:
        if "shovel" in inventory_gui:
          print("\nThe ground is too hard to dig.")
          location_text()
          location_action()
        else:
          print("\nYou need a shovel to dig.")
          location_text()
          location_action()
    elif "search" in bonnet_action:
      # Add any search area here
      if "scraps" in bonnet_action or "metal scraps" in bonnet_action or "metal" in bonnet_action:
        # Add any search location X Y here
        if player_x == 3 and player_y == 2:
          if has_shovel_int == 0:
            print("\nYou found a shovel.")
            inventory_gui.append("shovel")
            has_shovel_int = 1
            location_text()
            location_action()
          else:
            print("\nYou've already searched here.")
        else:
          print("\nYou don't see that here.")
          location_text()
          location_action()
      elif "chest" in bonnet_action:
        if player_x == 1 and player_y == 3:
          if "key" in inventory_gui:
            if has_battery_int == 0:
              print("\nYou place the key into the keyhole, and twist slowly. After a click, you open the chest.\n\nYou found a battery.")
              inventory_gui.append("battery")
              has_battery_int = 1
              location_text()
              location_action()
            else:
              print("\nYou've already searched here.")
          else:
            print("\nYou don't have a key")
        else:
          print("\nYou don't see that here.")
      else:
        print("\nYou cannot search there.")
        location_text()
        location_action()
    # Examine Command
    elif "examine" in bonnet_action:
      if "scraps" in bonnet_action or "metal" in bonnet_action or "metal scraps" in bonnet_action:
        if player_x == 3 and player_y == 1:
          print("\nThe metal scraps look old and rusty. Most of the pieces are too damaged, but some objects in the pile still seem intact.")
          location_text()
          location_action()
        elif player_x == 3 and player_y == 2:
          print("\nThe metal scraps look old and rusty. Most of the pieces are too damaged, but some objects in the pile still seem intact.")
          location_text()
          location_action()
        else:
          print("\nYou don't see that here")
          location_text()
          location_action()
      # add more things in environment to examine.
      elif "chest" in bonnet_action:
        if player_x == 1 and player_y == 3:
          print("\nThe chest looks wooden, with silver decorations embedded. To open, use the search command.")
          location_text()
          location_action()
        else:
          print("\nYou don't see that here.")
          location_text()
          location_action()

      # Inventory objets to examine:
      elif "shovel" in bonnet_action:
        if "shovel" in inventory_gui:
          print("\nThe shovel isn't in the best shape and has probably seen better days, but could still serve as a useful tool.")
          location_text()
          location_action()
        else:
          print("\nYou don't have that in your inventory")
          location_text()
          location_action()
      elif "battery" in bonnet_action:
        if "battery" in inventory_gui:
          print("\nAn average looking AAA battery, with the wrapper around it peeled off. It's probably the kind you find at Fair Price, Energizer brand.")
          location_text()
          location_action()
        else:
          print("\nYou don't have that in your inventory")
          location_text()
          location_action()
      elif "cpu card" in bonnet_action:
        if "cpu card" in inventory_gui:
          print("\nThe CPU card is dusty and small. It's probably useless. For some reason, your stomach grumbles in hunger looking at it.")
          location_text()
          location_action()
        else:
          print("\nYou don't have that in your inventory")
          location_text()
          location_action()
      else:
        print("\nYou see nothing special about that")
        location_text()
        location_action()
    elif bonnet_action == "eat cpu card" or bonnet_action == "eat cpu":
      if "cpu card" in inventory_gui:
        if cpu_eat == 1:
          print("\nYou pause for a moment and try to figure out why the hell you thought about eating the cpu.\nAfter 37 seconds of concentration, you decide to shake the thought away.")
          cpu_eat += 1
          location_text()
          location_action()
        elif cpu_eat == 2:
          print("\nOnce again, you stop and think, this time for 43.2 seconds. You decide you will need mental therapy as soon as possible.")
          cpu_eat += 1
          location_text()
          location_action()
        elif cpu_eat == 3:
          cpu_eat += 1
          print("\n...")
          location_text()
          location_action()
        elif cpu_eat == 4:
          print("\nUnable to control yourself, your hand slowly reaches out towards the cpu card...")
          time.sleep(3)
          print("\nYou force the CPU down your throat, and you start choking...")
          time.sleep(2)
          death(message = "choked on a cpu card...?")
      else:
        print("\nYou pause for a moment and try to figure out why the hell you thought about eating the cpu.\nAfter 37 seconds of concentration, you reach for you cpu card... except you don't have it.")


    # Refresh False XY
    elif bonnet_action == "refresh":
      if developer_mode == True:
        print()
        location_text()
        location_action()
      else:
        print("\nInvalid Action.")
        location_text()
        location_action()

    # Invalid Command
    else:
      print("\nInvalid Action.")
      location_text()
      location_action()

def death(message):
  print("\nGame over. Cause of death: " + message)
  home_screen()

# Update inventory_str with gui and progress_str with gui
def update_str_gui():
  global inventory_str, progress_str, inventory_gui, progress_gui, has_battery_int, has_shovel_int, has_cpu_int, has_key_int
  if inventory_gui == []:
    inventory_str = "0"
  elif set(inventory_gui) == {"key"}:
    inventory_str = "1"
  elif set(inventory_gui) == {"shovel"}:
    inventory_str = "2"
  elif set(inventory_gui) == {"cpu card"}:
    inventory_str = "3"
  elif set(inventory_gui) == {"battery"}:
    inventory_str = "4"
  elif set(inventory_gui) == {"key", "cpu card"}:
    inventory_str = "5"
  elif set(inventory_gui) == {"key", "battery"}:
    inventory_str = "6"
  elif set(inventory_gui) == {"key", "shovel"}:
    inventory_str = "7"
  elif set(inventory_gui) == {"key", "cpu card", "shovel"}:
    inventory_str = "8"
  elif set(inventory_gui) == {"key", "battery", "shovel"}:
    inventory_str = "9"
  elif set(inventory_gui) == {"key", "cpu card", "battery"}:
    inventory_str = "a"
  elif set(inventory_gui) == {"key", "cpu card", "battery", "shovel"}:
    inventory_str = "b"
  elif set(inventory_gui) == {"shovel", "battery"}:
    inventory_str = "c"
  elif set(inventory_gui) == {"shovel", "cpu card"}:
    inventory_str = "d"
  elif set(inventory_gui) == {"shovel", "battery", "cpu card"}:
    inventory_str = "e"
  elif set(inventory_gui) == {"battery", "cpu card"}:
    inventory_str = "f"
  else:
    print("\nWarning: Invalid inventory_gui, unable to sync with string.")
    time.sleep(2)
    print("\nReport:\n\nPosition:" + str(player_x) + " " + str(player_y) + "\nFalse Position Check:" + str(false_player_x) + " " + str(false_player_y) + "\nInventory_GUI:" + str(inventory_gui) + "\nProgress_GUI:" + str(progress_gui) + "\nInventory_STR:" + str(inventory_str) + "\nProgress_STR:" + str(progress_str) + "\nItem STR List:\n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nProgress STR List:\n1shovelyes" + "\nhas shovel / cpu / battery ID:" + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
    time.sleep(1)
    print("\nGame Crashed.")
    time.sleep(1)
    home_screen()
  if progress_gui == []:
    progress_str = "0"
  elif progress_gui == ["shovelyes"]:
    progress_str = "1"
  else:
    print("\nWarning: Invalid progress_gui, unable to sync with string.")
    time.sleep(2)
    print("\nReport:\n\nPosition:" + str(player_x) + " " + str(player_y) + "\nFalse Position Check:" + str(false_player_x) + " " + str(false_player_y) + "\nInventory_GUI:" + str(inventory_gui) + "\nProgress_GUI:" + str(progress_gui) + "\nInventory_STR:" + str(inventory_str) + "\nProgress_STR:" + str(progress_str) + "\nItem STR List:\n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nProgress STR List:\n1shovelyes" + "\nhas shovel / cpu / battery ID:" + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
    time.sleep(1)
    print("\nGame Crashed.")
    time.sleep(1)
    home_screen()
  # Has_item_before sync
  if has_shovel_int == 0 and inventory_str in (2, 3, 5, 7, 8, 9, "a" "b", "c", "d", "e", "f"):
    print("\nWarning: has_shovel_int == 0, contrasts with inventory_str ID.")
    time.sleep(2)
    print("\nReport:\n\nPosition:" + str(player_x) + " " + str(player_y) + "\nFalse Position Check:" + str(false_player_x) + " " + str(false_player_y) + "\nInventory_GUI:" + str(inventory_gui) + "\nProgress_GUI:" + str(progress_gui) + "\nInventory_STR:" + str(inventory_str) + "\nProgress_STR:" + str(progress_str) + "\nItem STR List:\n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nProgress STR List:\n1shovelyes" + "\nhas shovel / cpu / battery ID:" + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
    time.sleep(1)
    print("\nGame Crashed.")
    time.sleep(1)
    home_screen()
  if has_CPU_int == 0 and inventory_str in (3, 5, 8, "a", "b", "d", "e", "f"):
    print("\nWarning: has_cpu_int == 0, contrasts with inventory_str ID.")
    time.sleep(2)
    print("\nReport:\n\nPosition:" + str(player_x) + " " + str(player_y) + "\nFalse Position Check:" + str(false_player_x) + " " + str(false_player_y) + "\nInventory_GUI:" + str(inventory_gui) + "\nProgress_GUI:" + str(progress_gui) + "\nInventory_STR:" + str(inventory_str) + "\nProgress_STR:" + str(progress_str) + "\nItem STR List:\n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nProgress STR List:\n1shovelyes" + "\nhas shovel / cpu / battery ID:" + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
    time.sleep(1)
    print("\nGame Crashed.")
    time.sleep(1)
    home_screen()
  if has_battery_int == 0 and inventory_str in (4, 6, 9, "a", "b", "c", "e", "f"):
    print("\nWarning: has_battery_int == 0, contrasts with inventory_str ID.")
    time.sleep(2)
    print("\nReport:\n\nPosition:" + str(player_x) + " " + str(player_y) + "\nFalse Position Check:" + str(false_player_x) + " " + str(false_player_y) + "\nInventory_GUI:" + str(inventory_gui) + "\nProgress_GUI:" + str(progress_gui) + "\nInventory_STR:" + str(inventory_str) + "\nProgress_STR:" + str(progress_str) + "\nItem STR List:\n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nProgress STR List:\n1shovelyes" + "\nhas shovel / cpu / battery ID:" + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
    time.sleep(1)
    print("\nGame Crashed.")
    time.sleep(1)
    home_screen()
  if has_key_int == 0 and inventory_str in (1, 5, 6, 7, 8, 9, "a", "b"):
    print("\nWarning: has_key_int == 0, contrasts with inventory_str ID.")
    time.sleep(2)
    print("\nReport:\n\nPosition:" + str(player_x) + " " + str(player_y) + "\nFalse Position Check:" + str(false_player_x) + " " + str(false_player_y) + "\nInventory_GUI:" + str(inventory_gui) + "\nProgress_GUI:" + str(progress_gui) + "\nInventory_STR:" + str(inventory_str) + "\nProgress_STR:" + str(progress_str) + "\nItem STR List:\n1k2s3b4c5ks6kb7kc8ksb9kscAkbc\nBksbcCsbDscEscbFbc\nProgress STR List:\n1shovelyes" + "\nhas shovel / cpu / battery ID:" + str(has_shovel_int) + str(has_CPU_int) + str(has_battery_int) + str(has_key_int))
    time.sleep(1)
    print("\nGame Crashed.")
    time.sleep(1)
    home_screen()

# Check Player Movement
def run_movement():
  global player_x, player_y, false_player_x, false_player_y
  # Out of bounds?
  if false_player_x < 1:
    print("\nYou cannot move that way.")
    location_text()
    location_action()
  elif false_player_y < 1:
    print("\nYou cannot move that way.")
    location_text()
    location_action()
  elif false_player_x > 12:
    print("\nYou cannot move that way.")
    location_text()
    location_action()
  elif false_player_y > 12:
    print("\nYou cannot move that way.")
    location_text()
    location_action()
  # Walls? Can't move?
  elif false_player_x in [1, 2] and false_player_y == 2:
    print("\nYou cannot move that way. ( Tip: Follow the road )")
    location_text()
    location_action()
  # Check if X or Y moved, executes movement
  else:
    if false_player_x == player_x + 1 or false_player_x == player_x - 1:
      player_x = false_player_x
      location_text()
      location_action()
    elif false_player_y == player_y + 1 or false_player_y == player_y - 1:
      player_y = false_player_y
      location_text()
      location_action()

"""Destiny"""
# work in progress heheh


"""Application Selection"""

# System OS
import os
import sys
import time
import random
import openai

def home_screen():
  while True:
    try:
      application = input("\nSelect an application\nAnswer: ").lower()
    except KeyboardInterrupt:
      exit_confirmation = input("\n\nAre you sure you want to exit? (y/n)\nAnswer: ").lower()
      if exit_confirmation == "y":
        break
      else:
        continue
    if application == "games":
      print("\nAvailable games currently:\n1. Lottery game\n2. Guessing game\n3. Destiny")
      game_selection = input("\nSelect a game ( 1 / 2 / 3 )\nAnswer: ").lower()
      if game_selection == "1":
        lottery_game()
      elif game_selection == "2":
        guessing_game()
      elif game_selection == "3":
         destiny_game()
      else:
        print("\nInvalid Action.")
    elif application == "bonnet":
      bonnet()
    elif application == "calculator":
      calculator()
    elif application == "todo":
      todo()
    elif application == "help":
      helpapp()
    elif application == "notes":
      notesapp()
    elif application == "settings":
      settingsapp()
    elif application == "encryptor":
      print("\nVigenère Cipher decryption V1.0")
      while True:
        encrypt_or_decrypt = input("\nDo you want to encrypt or decrypt?\nAnswer: ")
        if encrypt_or_decrypt == "encrypt":
          KEY = input("\nEnter your key.\nAnswer: ")
          time.sleep(1)
          ciphertext = input("\nEnter the code you want to encrypt.\nAnswer: ")
          time.sleep(random.randint(1,3))
          print("\nEncrypted text:", vigenere_cipher(ciphertext, KEY, mode="encrypt"))
        elif encrypt_or_decrypt == "decrypt":
          KEY = input("\nEnter your key.\nAnswer: ")
          time.sleep(1)
          ciphertext = input("\nEnter the code you want to decrypt.\nAnswer: ")
          time.sleep(random.randint(1,3))
          print("\nDecrypted text:", vigenere_cipher(ciphertext, KEY, mode="decrypt"))
        elif encrypt_or_decrypt == "exit":
          home_screen()
        else:
          print("\nInvalid action.")
    elif application == "exit":
      exit_confirmation = input("\n\nAre you sure you want to exit? ( y / n )\nAnswer: ").lower()
      if exit_confirmation == "y":
        break
      else:
        continue
    else:
      print("\nInvalid Application.")


def type_text(text, delay=0.02):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(delay)
  print()

def first_time(file_path="BIOS_1.txt"):

    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read().strip()
                run_count = int(content) if content.isdigit() else 0
        else:
            run_count = 0
    except (FileNotFoundError, ValueError):
        run_count = 0

    run_count += 1

    with open(file_path, "w") as file:
        file.write(str(run_count))

    return run_count

def get_username(file_path="BIOS_2.txt"):
  
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            username = file.read().strip()
    else:
        username = ""
    return username

def save_username(username, file_path="BIOS_2.txt"):

    with open(file_path, "w") as file:
        file.write(username)

# BIOS
run_count = first_time()

try:
    if run_count == 1:  # First time running the script
        type_text("\nWelcome to Clover OS, an operating system powered by Python script.")
        time.sleep(1)
        username = input("\nSelect a username: ").strip()
        save_username(username)  # Save the username
        type_text("\nBooting...")
        time.sleep(0.5)
        type_text("\nPlease do not turn off this script.")
        time.sleep(2)
        type_text("\nType 'help' to start.")
        home_screen()
    elif run_count > 1:  # Subsequent runs
        username = get_username()
        if not username:  # If username retrieval fails
            print("\nWarning: Your BIOS save file is corrupt.")
            time.sleep(1)
            print("\nStarting Recovery Mode...")
            time.sleep(2)
            print("\nManual Options:\n1. Locate BIOS Files\n2. Delete corrupted BIOS files, and reboot.")
        else:
            type_text(f"\nWelcome Back, {username}. Logins: {run_count}")
            time.sleep(0.5)
            home_screen()
    else:
        print("\nWarning: Your BIOS save file is corrupt.")
        time.sleep(1)
        print("\nStarting Recovery Mode...")
        time.sleep(2)
        print("\nManual Options:\n1. Locate BIOS Files\n2. Delete corrupted BIOS files, and reboot.")
except Exception as e:
    print(f"An error occurred: {e}")
