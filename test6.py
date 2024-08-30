import os

def my_func():
    password = "password123"  # Hardcoded password

    os.system("rm -rf /")  # Dangerous command

    data = [1, 2, 3]
    for i in range(4):  # Index out of range
        print(data[i])

my_func()
