def fuzz_buzz(num_max, num_fizz, num_buzz):
    cnt = 1
    while cnt <= num_max:
        if cnt % num_fizz == 0 and cnt % num_buzz ==0:
            print("Fizz Buzz!")
        else:
            if cnt % num_fizz ==0:
                print("Fizz!")
            else:
                if cnt % num_buzz == 0:
                    print("Buzz!")
                else:
                    print(cnt)
        cnt = cnt + 1
fuzz_buzz(16, 3, 5)
