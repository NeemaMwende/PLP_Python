# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print("Blastoff!")
# print(n)


# while True:
#     line = input('< ')
#     if line[0] == "#":
#         continue
#     if line == "done" :
#         break
#     print(line)
# print("Done")


# welcome_message = "Welcome to PLP"
# for i in range(10):
#     print(welcome_message)


# count = 0
# while count <= 10:
#     print(count)
#     count += 1

# colors = ["blue", "green", "white", "yellow", "brown", "cream"]
# color_i_want = "white"

# for color in colors:
    
#     if color == color_i_want:
#         print("They have the color i want")
#         break
#     print(color)

# largest_so_far = -1
# print("Before", largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15]:
#     if the_num > largest_so_far:
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# print("After", largest_so_far)

# n = 5
# while n > 0:
#     print(n)
# print("All done")

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

n = 0
while n > 0 :
    print('Lather')
    print('Rinse')
print('Dry off!')