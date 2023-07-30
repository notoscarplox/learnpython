def prime_checker(number):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            print("It is prime")
        else:
            print("It is not prime")
                  


n = int(input("Check this number: "))
prime_checker(number=n)