# import PyPDF2
# Open the PDF file in binary mode
# with open("CoverLetter.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file)
#     text = ""
#     # Extract text from each page
#     for page in range(len(reader.pages)):
#         text += reader.pages[page].extract_text()
#     print(text)

#reading file contents
# file = open("CoverLetter.pdf", "rt")
# content = file.read()
# print(content)
# file.close()

#writing file contents
# file = open("example.txt", "w")
# file.write("Hey there\n")
# file.write("This is a test.\n")
# file.close()

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open("example.txt", "a") as file:
#     file.write("This is an additional line.\n")

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)
#     file.close()

# Using with statement to read the file
# with open("CoverLetter.pdf", "r") as file:
#     for line in file:
#         print(line.strip())  # Automatically closes the file after reading

# # Open the file in read mode ('r')
# file = open("CoverLetter.pdf", "r")
# # Read each line from the file
# for line in file:
#     print(line.strip())  # The strip() method is used to remove extra spaces or newlines
# file.close()

#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# r, rb, r+, w, wb, w+, wb+, a, ab, a+, ab+ 
#appending file - adding data to an existing file without altering ot overwriting the existing content
# Open the file in append mode ('a')

# Writing to a file for demonstration
# with open("angel.txt", "w") as file:
#     file.write("Hello, this is a sample text.")

# # Open the file in read mode
# with open("angel.txt", "r") as file:
#     # Read and print the first 5 characters
#     print(file.read())  # Output: Hello
#     # Tell the current position (after reading 5 bytes)
#     print("Current file pointer position:", file.tell())  # Output: 5
#     # Seek back to the beginning of the file
#     file.seek(0, 0)  # Move the pointer to the start of the file
#     # Read and print the first 7 characters
#     print(file.read(7))  # Output: Hello, 
#     # Tell the current position
#     print("Current file pointer position:", file.tell())  # Output: 7
#     # Seek to the 10th byte from the start of the file
#     file.seek(10, 0)  # Move 10 bytes forward from the start
#     print(file.read(4))  # Output: this
#     # Seek to the end of the file
#     file.seek(0, 2)  # Move the pointer to the end of the file
#     print("Pointer at the end of the file:", file.tell())  # Output: Total file size


# Open the file and read all lines using readlines()
# with open("example.txt", "r") as file:
#     lines = file.readlines()  # Reads all lines into a list
#     for index, line in enumerate(lines, 1):
#         print(f"Line {index}: {line.strip()}")  # Output each line without newline character


# with open("example.txt", "r+") as file:
#     contents = file.read()
#     file.write("Hello, world\n")
#     print(contents)

# import os
# filename = "example.txt"
# if os.path.exists(filename):
#     os.remove(filename)
#     print(f"{filename} has been deleted")
# else:
#     print(f"{filename} does not exist")

#context managers
class MyContextManager:
    def __enter__ (self):
        print("Entering context")
        return self

    def __exit__ (self, exc_type, exc_val, exc_tb):
        print("Exiting context")
        if exc_type is not None:
            print(f"An error of type {exc_type} occurred: {exc_val}")
        return self
    
with MyContextManager() as cm:
    print("Inside context")