#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    return list(map(lambda num: num ** 2, int_list))
    print(square_integers([1, 2, 3, 4]))


def fizzbuzz(num,):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    


def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))
