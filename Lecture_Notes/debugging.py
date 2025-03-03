
# Example of syntax error - structure of your code. - Forgot colin, quotation, etc. 

""" Ex: print("Hello world! """

# Example of runtime error - error while running code. 

a = 10 
b = 0 

if b ==0:
  print("Divide by zero error")
  exit()

if b != 0:
  result = a / b

  
""" result = a / b 
print(result) """


# Example of logical error: 

# Program runs but  doesn't give expected result. 

# Goal: Subtract 2 numbers so there is never a negative number as a result. 

""" a = 10 
b = 5

print("b is less than a")
result = a - b 

print(result)
"""

# Example of exception error: 

""" fruits = ["orange", "apple", "banna", "tomato"]

print(fruits[6]) """

# Fix: 

fruits = ["orange", "apple", "banna", "tomato"]

index = 4 
if index < len(fruits):
  print(fruits[index])



# frogger moving 
if event.key == pygame.K_w: # up direction (w)
  cur_pos[1] -= 20    #y-coor
if event.key == pygame.K_s: # down direction (s)
  cur_pos[1] += 20    #y-coor
if event.key == pygame.K_a: # left direction (a)
  cur_pos[0] -= 20    # x-coor
if event.key == pygame.K_d: # right direction (d)
  cur_pos[0] += 20    # x-coor