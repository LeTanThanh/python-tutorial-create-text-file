if __name__ == "__main__":
  # Using the open() function to create a new text file

  """
  To create a new text file, you use the open() function.
  The open() function has many parameters.
  However, we'll focus on first two parameters:

  file = open(path_to_file, mode)

  In this syntax, the path_to_file parameter specifies the path to the text file that you want to create.
  For creating a new text file, you use one of the following modes:

  - w:  open a file for writing.
        If the file doesn't exist, the open() function creates a new file.
        Otherwise, it'll overwrite the contents of the existing file.

  - x:  open a file for exclusive creation.
        If the file exists, the open() function raise an error FileExistError.
        Otherwise, it'll create the text file.

  For example, the following creates a new file called readme.txt and write some text into it:
  """

  with open("readme.txt", "w") as file:
    file.write("Create a new text file!")

  """
  This script creates a file with the name "readme.txt" in the same directory where the script file locates.
  If you want to create a file in a specified directory e.g., doc/readme.txt, you need to ensure that the docs directory exists before creating the file.
  Otherwise, you'll get an exception.
  For example:

  with open("docs/readme.txt", "w") as file:
    file.write("Create a new text file!")

  In this example, Python raise an exception because the docs directory doesn't exist.
  Therefore, it could not create the readme.txt file in that directory.
  To fix the issue, you need to create the docs directory first and then create the readme.txt file in that folder.

  Also, you can handle the exception using the try-except statement as follows:
  """

  try:
    with open("docs/readme.txt", "w") as file:
      file.write("Create a new text file!")
  except FileNotFoundError:
    print("The 'docs' directory doesn not exist")

  """
  If you don't want to create a new text file in case it already exist, you can use the "x" mode when calling the open() method
  """

  try:
    with open("readme.txt", "x") as file:
      file.write("Create a new text file!")
  except FileExistsError as error:
    print(error)
