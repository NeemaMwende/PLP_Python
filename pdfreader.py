import PyPDF2

# Open the PDF file
with open("CoverLetter.pdf", "rb") as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)
    
    # Extract text from all pages
    text = ""
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()

    # Convert the text to lowercase for case-insensitive search
    text = text.lower()

    # Words to search for
    words_to_search = ["computer science", "internship", "victor"]

    # Check if words are present in the text
    for word in words_to_search:
        if word.lower() in text:
            print(f"The word '{word}' is present in the cover letter.")
        else:
            print(f"The word '{word}' is NOT present in the cover letter.")
