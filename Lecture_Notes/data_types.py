a = 3
# b = "my name is Nathan"
b = 6.5 
c = "my name"

if a > b:
  print("something here")

print(type(a))
print(type(b))
print(type(c))

c = 5 
print(type(c))

my_list = ["another string", 5, "my age", 5.67]
print(type(my_list))

# accessing list
print(my_list[0]) # 0 represents position in list - starts at 0 not 1 
print(my_list[3]) 

# add item to list
my_list.append("milk")
print(my_list)

# first character of a word in list 
print(my_list[0][0])

# remove from string
my_list.remove(5)
print(my_list)
my_list.pop(2)
print(my_list)

# length of list
print(len(my_list))


# Practice
my_list2 = ["Call Mom", "Walk the dog", "Go to the grocery store"]
my_list2.append("Read a book")
my_list2[1] = "Finish homework"
my_list2.remove("Call Mom")
print(len(my_list2))
print(my_list2)

# Notes again

coordinates = [
  (100,200),
  (200,300)
]








# my_list = [[100,200], [300,4]]

