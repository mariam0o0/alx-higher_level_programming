#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            if i % 5 == 0:
                print("FizzBuzz", end = " ")
            print("Fizz", end = " ")
        else:
            print(i, end = " ")
