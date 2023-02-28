def somador():
    sum = i = 0
    switch = True
    received = input()
    input_string = list(received)
    limit = len(input_string)
    while (i in range(0,limit)): # Melhorar isto para melhor desempenho.
        if (input_string[i] == 'o' or input_string[i] == 'O'):
            if (input_string[i+1] == 'n' or input_string[i+1] == 'N'):
                switch = True
                i += 2
            elif (input_string[i+1] == 'f' or input_string[i+1] == 'F') and (input_string[i+2] == 'f' or input_string[i+2] == 'F'):
                switch = False
                i += 3
            else:
                i += 1
        elif (input_string[i].isnumeric() and switch):
            num = input_string[i]
            n = i + 1
            while (input_string[n].isnumeric()):
                num += input_string[n]
                n += 1
                if (n >= limit):
                    break
            sum = sum + int(num)
            i = n
        elif (input_string[i] == "="):
            print(sum)
            i += 1
        else:
            i += 1

somador()
