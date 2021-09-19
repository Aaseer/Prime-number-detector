prime_number_count = 0
ask = str(input('Do you want to manually put all the prime numbers or a series of prime numbers? (Type "m" for manual and "s" for series)\n'))

if ask == 'm':
    input_prime = str(input('Please input the numbers list from which you want to get the prime numbers. (Seperate each number with a " "): '))

    as_list = input_prime.split(", ")

    prime_list = list(map(int, as_list))

    if len(input_prime) < 1:
        print('Hey, you have to give some numbers!')

    else:
        pass

    for i in range(0, len(prime_list)):

        if prime_list[i] == 1:
            pass
        elif prime_list[i] % 2 == 1 and prime_list[i] % 3 != 0 and prime_list[i] % 5 != 0:
            print(prime_list[i])
            prime_number_count += 1

        elif prime_list[i] == 2:
            print(prime_list[i])
            prime_number_count += 1
        
        elif prime_list[i] == 3:
            print(prime_list[i])
            prime_number_count += 1
        
        elif prime_list[i] == 5:
            print(prime_list[i])
            prime_number_count += 1

        else:
            pass
    print(f'\n \n \n{prime_number_count} prime numbers were detected')
    prime_number_count = 0

elif ask == 's':
    input_prime_series = str(input('Put the number to start from and the number to end the program with and seperate with a ", " example: 0, 213 (gets prime numbers from 0 to 213) \n'))

    if input_prime_series == '':
        print('Hey, you have to pass in 2 arguments')
    
    else:
        asSplit = input_prime_series.split(", ")
        series_list = list(map(int, asSplit))

        
        for i in range(series_list[0], series_list[1] + 1):

            if i == 1:
                pass
            elif i % 2 == 1 and i % 3 != 0 and i % 5 != 0:
                print(i)
                prime_number_count += 1

            elif i == 2:
                print(i)
                prime_number_count += 1
            
            elif i == 3:
                print(i)
                prime_number_count += 1
            
            elif i == 5:
                print(i)
                prime_number_count += 1

            else:
                pass
        
        print(f'\n \n \n {prime_number_count} prime numbers were detected')
        prime_number_count = 0
else:
    print('That\'s an invalid argument. Your commands are either s or m')
