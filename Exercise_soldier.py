def soldier(path, file_format):
    import os
    os.chdir(path)
    num = 1

    for files in os.listdir(path):

        if os.path.isfile(files):
            os.rename(files, files.capitalize())

            if files.endswith(f".{file_format}"):
                os.rename(files, f"{num}.{file_format}")
                num = num + 1

if __name__ == "__main__":

    print("\n <-- Oh Soldier Prettify My Folder -> \n --> Do you want to prettify your Folder. If yes, follow the instructions below: \n")
    path = input("-> Enter your path of folder in which you want to capitalize the first letter of files not directory:\n")
    file_format = input("-> Enter your file format of files which you want to rename the files in integer(1-100...):\n")

    soldier(path, file_format)

