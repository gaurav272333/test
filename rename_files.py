import os

#Just for checking

def rename_file():
    file_list = os.listdir("D:\Python Practice\prank")
    print(file_list)

    saved_path = os.getcwd()
    os.chdir("D:\Python Practice\prank")

    for file_name in file_list:
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)
rename_file()

