def file_read_write():
    filename = input("Enter the filename to read: ").strip()

    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        print(f"✅ Successfully read {content} file.")

        modified = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(modified)

        print(f"✅ Successfully created {new_filename} file.")

    except FileNotFoundError:
        print(" Error: The file does not exist.")
    except PermissionError:
        print(" Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

if __name__ == "__main__":
    file_read_write()



# This code reads a file, modifies its content, and writes it to a new file.
# It handles errors such as file not found and permission issues.       
# The user is prompted to enter the filename to read.

# Append "welcome to PLP" to readme.md
# with open("readme.md", "a", encoding="utf-8", errors="ignore") as file:
#     file.write("\nwelcome to PLP")
# # print("File structure module loaded successfully.")# Now read and print the updated file
# with open("readme.md", "r", encoding="utf-8", errors="ignore") as file:
#     print(file.read())