#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i>0:
        print(i)
        i -= 1
    print("Happy New Year!")
    # pass

def square_integers(int_list):
    return [k**2 for k in int_list]
    pass

def fizzbuzz():
    for x in range(1, 101):
        if x %3 ==0 and x %5 == 0:
            print("FizzBuzz")
        elif x %3 ==0:
            print("Fizz")
        elif x %5 ==0:
            print("Buzz")
        else:
            print(x)
    # pass
