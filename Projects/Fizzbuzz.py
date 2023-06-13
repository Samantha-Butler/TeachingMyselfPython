for fizzbuzz in range(101):
    if fizzbuzz % 4 == 0 and fizzbuzz % 6 == 0:
        print("FIZZBUZZ!")
    elif fizzbuzz % 4 == 0:
        print("Fizz!")
        continue
    elif fizzbuzz % 6 == 0:
        print("Buzz!")
        continue
    print(fizzbuzz)