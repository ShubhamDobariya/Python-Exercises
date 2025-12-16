import os


"""
Return a list of files and folders inside the given directory.
"""
print(f"List of files and folders : ", os.listdir())

"""
Return current working directory.
"""
print(f"Current working directory : ", os.getcwd())


"""
Create new directory
"""
os.mkdir("new_folder")
print(f"New Directory created!")


"""
Create multiple nested folder at once
"""
os.makedirs("folder1/folder2/folder3")
print(f"Multimple nested folders created.")


"""
remove empty folder only 
"""
os.rmdir("new_folder")
print(f"remove folder successfully.")


"""
remove multiple nested folders. 
"""
os.removedirs("folder1/folder2/folder3")
print(f"remove multiple mested folders successfully.")


""""
Delete a file.
"""
os.remove("test.txt")
print(f"Remove file successfully.")


"""
Rename a files or directory
"""
os.rename("old.txt", "new.txt")
print(f"successfully rename done!")


"""
Check if a file or folder exists.
"""
os.path.exists("Problem1.py")


"""
Check if the path is a file.
"""
os.path.isfile("Proble2.py")

"""
Check if the path is a folder.
"""

os.path.isdir("Problem4")


"""
Get the current working directory.
"""
print(f"Current working directory", os.getcwd())


"""
Change the current working directory.
"""
# os.chdir("c://Users/subha/OneDrive/Desktop")
print(f"Successfully changed working directory.")

"""
Walk (loop) through all files and folders recursively.
(Very useful for scanning large directory structures.)
"""
for root, dirs, files in os.walk("."):
    print(root, dirs, files)


"""
More advanced version of listdir().
Gives file type info (file/dir) and full paths.
"""
with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "|", entry.is_file())


"""
Gives you access to environment variables (like system paths, API keys, etc.).
"""
print(os.environ("PATH"))


"""
Safely combine paths (avoids manual slashes).
"""

full_path = os.path.join("old_folder", "old_file.py")
print("created full path", full_path)


"""
Get the size of a file in bytes.
"""

os.path.getsize("Problem1.py")


"""
Get the last modified time of a file.
"""
os.path.getmtime("Problem2.py")


"""
Get the absolute (full) path of a file or folder.
"""
os.path.abspath("Problem4.py")
