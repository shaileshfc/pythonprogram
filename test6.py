import os
import sys

def process_data(data):
    if len(data) > 0:
        for i in range(len(data)):
            print(data[i])
    else:
        print("No data to process")

def insecure_function(password):
    # Hardcoded password (Security issue: bandit should flag this)
    if password == "12345":
        print("Access Granted!")
    else:
        print("Access Denied!")

def calculate_sum(a, b):
    return a + b

def unused_function():
    print("This function is never used")

def main():
    data = [1, 2, 3, 4]
    
    # Potentially problematic command (Security issue: bandit should flag this)
    os.system('ls -al')

    process_data(data)

    # Unused variable (should be flagged by pyflakes or pylint)
    unused_variable = "This variable is not used"

    # Incorrect indentation (should be flagged by pycodestyle or pylint)
      sum_result = calculate_sum(10, 20)
    print("Sum:", sum_result)

if __name__ == "__main__":
    main()
