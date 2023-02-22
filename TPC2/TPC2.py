def somador():
    sum = 0
    switch = True
    received = input()
    input_string = list(received)
    for i in range(len(input_string)):
        if (input_string[i] == 'o' or input_string[i] == 'O'):
            if (input_string[i+1] == 'n' or input_string[i+1] == 'N') and (not switch):
                switch = True
            elif (input_string[i+1] == 'f' or input_string[i+1] == 'F') and (input_string[i+2] == 'f' or input_string[i+2] == 'F') and (switch):
                switch = False
        elif (input_string[i].isnumeric() and switch):
            sum = sum + int(input_string[i])
        elif (input_string[i] == "="):
            print(sum)

somador()