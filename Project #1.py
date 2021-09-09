terrain_types = {0:"Grass", 1:"Forest"}

map = [[0,0,1], [0,1,1], [1,1,1]]
       
current_loc = {'x_loc':0, 'y_loc':0}

# -----------------------------------
current_loc["x_loc"] += 0
current_loc["y_loc"] += 0

x_loc = current_loc["x_loc"]
y_loc = current_loc["y_loc"]

map_val = map[y_loc][x_loc]
# print(terrain_types[map_val])

# -----------------------------------

directions = ['N', 'S', 'E', 'W']

# North Function 
def north(x, y):
  current_loc["x_loc"] += 1
  current_loc["y_loc"] = 0 
# South Function 
def south(x, y):
  current_loc["x_loc"] -= 1
  current_loc["y_loc"] = 0 
# East Function 
def east(x, y):
  current_loc["x_loc"] = 0 
  current_loc["y_loc"] += 1 # Updates y cordinate 
# West Function 
def west(x, y):
  current_loc["x_loc"] = 0
  current_loc["y_loc"] += 1 # Updates y cordinate 

# ----------------------------------------------

user_location = []
running = True 

# Game Loop 
while running:
  print(f"\nYou are in {terrain_types[map_val]}")
  loc = terrain_types[map_val]
  user_location.append(loc)
  # Gathering User Input 
  user_input = input("\nWhere do you want to go? (N, S, E, W): ")
  user_input.upper()
  user_input[:0]
  if user_input in directions:
    # If the User Decides to go North 
    if user_input == 'N':
      north(x_loc, y_loc)
      if x_loc == 2: # Preventing the User from falling out of the map
        print("\nYou feel off of the map and died.")
        print("\nLocations Visited: ")
        print(*user_location, sep=", ")
        running = False
        break 
      x_loc = current_loc["x_loc"]
      y_loc = current_loc["y_loc"]
      map_val = map[y_loc][x_loc]
      continue 
      print(terrain_types[map_val])
    elif user_input == 'S': # if the user decides to go south 
      south(x_loc, y_loc) 
      if x_loc == 6: # preventing user from falling off of the map 
        print("\nYou fell off of the map and died.")
        running = False
        print("\nLocations Visited: ")
        print(*user_location, sep=", ")

        break 
      # Updating Cordinates 
      x_loc = current_loc["x_loc"]
      y_loc = current_loc["y_loc"]
      map_val = map[y_loc][x_loc]
      print(terrain_types[map_val])
      continue
    elif user_input == 'E':
      east(x_loc, y_loc)
      if y_loc == 2:
        print("\nYou feel off of the map and died. :( ")
        running = False 
        print("\nLocations Visited: ")
        print(*user_location, sep=", ")

        break 
      # Updating Cordinates 
      x_loc = current_loc["x_loc"]
      y_loc = current_loc["y_loc"]
      map_val = map[y_loc][x_loc]
      print(terrain_types[map_val])
      continue
    # West 
    elif user_input == 'W':
      west(x_loc, y_loc)
      if y_loc == 2:
        print("\nYou fell off of the map and died.")
        running = False 
        print("\nLocations Visited: ")
        print(*user_location, sep=", ")

        break
      x_loc = current_loc["x_loc"]
      y_loc = current_loc["y_loc"]
      map_val = map[y_loc][x_loc]
      print(terrain_types[map_val])
      continue
  # If input is invalid
  else:

    print("\nInvalid Command. Please try again and enter (N, S, E, W)")
    continue
