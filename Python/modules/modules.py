import math
import random
import datetime
import os
import sys
import platform

def system_info():
    print("OS:", platform.system())
    print("Processor:", platform.processor())
    print("Python Version:", platform.python_version())

def random_operations():
    print("Random Integer:", random.randint(1, 100))
    print("Random Choice:", random.choice(['apple', 'banana', 'cherry']))

def math_operations():
    print("Square Root of 25:", math.sqrt(25))
    print("Pi Value:", math.pi)

def file_operations():
    print("Current Directory:", os.getcwd())
    print("Python Version:", sys.version)

def datetime_operations():
    now = datetime.datetime.now()
    print("Current Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    system_info()
    random_operations()
    math_operations()
    file_operations()
    datetime_operations()