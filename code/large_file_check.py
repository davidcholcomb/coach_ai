import sys
import os


def check_filesize (filename):
    ''' This will check the filesize and append to .gitignore if the file is larger than 100mb'''
    size = float(os.stat(filename).st_size / 1000000)
    if size > 100:
        with open('../.gitignore', "a") as myfile:
            myfile.write(f"{filename}")
            myfile.close()
        return print(f'{filename} added to gitignore')
    else:
        return print(f'{filename} is less than 100MB')


def main():
    filename  = sys.argv
    check_filesize(filename)


if __name__ == "__main__":
    main()