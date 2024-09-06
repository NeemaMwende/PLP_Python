import PyPDF2

# Open the PDF file in binary mode
with open("CoverLetter.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    # Extract text from each page
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    print(text)

#reading file contents
# file = open("CoverLetter.pdf", "rb")
# content = file.read()
# print(content)
# file.close()

#writing file contents
file = open("example.txt", "w")
file.write("Hey there\n")
file.write("This is a test.\n")
file.close()

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

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