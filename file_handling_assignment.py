def file_handling():
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is my assignment\n")
            file.write("My name is Neema\n")
            file.write("I will be a PLP Alumni soon\n")
        print("Part one of the assignment complete")
        
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("\n--- File contents after initial write")
            print(content)
            
        with open("my_file.txt", "a") as file:
            file.write("Appending new line: Python is great!\n")
            file.write("Let's append another line.\n")
            file.write("Appended line number 3.\n")
        print("Data appended successfully.")
        
        with open("my_file.txt", "r") as file:
            updated_content = file.read()
            print("\n--- File Content After Appending ---")
            print(updated_content)
            
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You don't have permission to access the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile operation completed.")

# Run the file handling function
if __name__ == "__main__":
    file_handling()