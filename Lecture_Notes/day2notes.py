age = 15
age2 = 15

if age > 21:
  print("You are an adult.")
  print("You are old.")
else:
  print("You are young.")

age = 30 # difference = 15
difference = age - age2
if difference >= 0:
  print("positive or zero")
elif difference > 5:
  print("big number")
elif difference < 0:
  print("negative")

if difference > 5:
  print("big number")


counter = 0 
while counter <= 10:
  print(counter)
  # incriment counter
  # counter = counter + 1 or 
  counter += 1

# for loop
inventory = ["sword", "shield", "key"]
for item in inventory:
  print(item)

# boolean operators
is_game_paused = False 
is_dead = True

if is_game_paused or is_dead:
  print("Game Paused")
else:
  print("Game Not Paused")

if is_game_paused and is_dead:
  print("Game Over")

health = 50 
# one = sign means you are setting the variable. Two = signs mean check if equals to. 
if health == 0:
  is_dead = True
  