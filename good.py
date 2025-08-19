def file_read_write():
    
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            content = f.read()

       
        modified = content.upper()

       
        new_filename = "modified_" + filename
        with open(new_filename, "w") as f:
            f.write(modified)

        print(f"✅ Successfully created {new_filename}")

    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")



# This code reads a file, modifies its content, and writes it to a new file.
# It handles errors such as file not found and permission issues.       
# The user is prompted to enter the filename to read.