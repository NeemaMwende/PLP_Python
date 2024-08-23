#built in data structures in python - list, tuple, set, dictionary
#these are non-primitive(classed as objects)
# can be mutable or immutable
# mutable - eg list
# immutable - eg tuple


#user-defined structures - stack, queue, linked list, tree, graph, hashmap

#lists
my_list = [1,2,3,4,5, "Hello"]
# print(my_list)
# print(my_list[0])
# print(my_list[1:4])
# print(my_list[:])
# print(my_list[-1])

my_list.append(10)
print(my_list)

# names = ["Angel", "Mike", "Carol"]
# print(names)

# my_list.extend(names)
# print(my_list)

# del my_list[5]
# print(my_list)

# my_list.remove(3)
# print(my_list)

# my_list.insert(2, "inserted")
# print(my_list)

# my_list.reverse()
# print(my_list)

#iterating through a list
# for my_list in my_list:
#     print(my_list)

#python list comprehension (expression followed by the for statement inside square brackets)
numbers = [my_list*my_list for my_list in range(5, 10)]
print(numbers)
