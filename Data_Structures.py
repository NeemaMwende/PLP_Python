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

names = ["Angel", "Mike", "Carol"]
print(names)

my_list.extend(names)
print(my_list)