def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            # print(res)
            # return res
        elif num % 2 == 1:
            num = 3 * num + 1

        print(num)
    print(f"final {num}")


num = int(input("Enter number "))

collatz(num)
