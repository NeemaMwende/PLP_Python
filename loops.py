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

colors = ["blue", "green", "white", "yellow", "brown", "cream"]
color_i_want = "white"

for color in colors:
    
    if color == color_i_want:
        print("They have the color i want")
        break
    print(color)