from os import remove, listdir, getlogin
import time


PATH = f"D:\\İndirilenler"

#PATH = f"C:\\Users\\{getlogin()}\\Downloads"

def remove_file():
    try:
        for file in listdir(f"{PATH}"):
            if file.endswith(".png"):
                #time.sleep(10)  # Sleep for 3 seconds
                remove(f"{PATH}\\{file}")

    except Exception as error:
        pass


if __name__ == "__main__":
    # print(f"C:\\Users\\{getlogin()}\\Downloads")
    remove_file()
