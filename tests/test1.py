import os



def readfile():
    filename = 'word.txt'
    with open(filename, 'r') as file:
        for line in file:
            print(line)


def readfile2():
    filename = 'word1.txt'
    cur_dir = os.getcwd()
    full_path = os.path.join(cur_dir, 'tests',filename)
    print(f'full path: {full_path}')
    with open(full_path, 'r') as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    print("Hello, World!")
    cur_dir = os.getcwd()
    print(f'current directory: {cur_dir}')
    readfile()
    readfile2()