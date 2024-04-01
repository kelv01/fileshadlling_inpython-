def handle_file_operations():
  try:
    # Create and write to file
    with open("my_file.txt", "w") as file:
      file.write("This is the first line of text.\n")
      file.write("123 456 789\n")
      file.write("This is another line with a mix of strings and numbers: 54321.\n")

    # Read and display contents
    with open("my_file.txt", "r") as file:
      contents = file.read()
      print("Contents of the file:")
      print(contents)

    # Append to file
    with open("my_file.txt", "a") as file:
      file.write("This line is appended later.\n")
      file.write("More text to append.\n")
      file.write("Last appended line.\n")

  except FileNotFoundError:
    print("Error: File not found.")
  except PermissionError:
    print("Error: Permission denied for file operation.")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    print("File operations complete.")

if __name__ == "__main__":
  handle_file_operations()
