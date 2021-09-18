# paths.py - a program that illustrates using pathlib to print, make and remove
# files and directories
def path_exercises():
    import pathlib

    class color:
        BOLD = '\033[1m'
        RED = '\033[91m'
        BLINK = '\033[1;1;5m'
        END = '\033[0m'


    current_dir = pathlib.Path.cwd()  # Variable for the working directory
    print(current_dir)

    mypath = pathlib.Path.cwd() / 'resources/'  # New folder path
    mypath.mkdir() # Make the new folder
    myfile = pathlib.Path(mypath) / 'snakescales.tmp'
    print(myfile)
    print(f"File status before touch():{color.BLINK} {myfile.exists()}{color.END}\n")
    myfile.touch()

    if myfile.exists() and mypath.exists():
        print(f"Your file{color.BOLD + color.RED} '{myfile}'{color.END}\nwas created in the directory{color.BOLD + color.RED} '{mypath}'{color.END}\n")
    else:
        print("Error. Problem creating file/directory.")
    try:
        myfile.unlink()  
        print("Files have been cleaned up.")
    except:
        print("Error cleaning up files.")
    try:
        mypath.rmdir()
        print("Directories have been removed.")
    except:
        print("Error removing directories.")

        
if __name__ == "__main__":
    path_exercises()
