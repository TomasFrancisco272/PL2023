import re

def csv_to_json():
    nome_ficheiro_leitura = input()
    ficheiro_leitura = open(nome_ficheiro_leitura,"r")
   
    if (ficheiro_leitura.closed):
        print("Erro: Ficheiro não abriu.")
        return
    
    nome_ficheiro_escrita = nome_ficheiro_leitura[:-4] + ".json"
    ficheiro_escrita = open(nome_ficheiro_escrita,"w")

    conteudo = ficheiro_leitura.readlines()
    ficheiro_leitura.close()

    parametros = re.split(r',',conteudo[0])
    parametros_iter = iter(parametros)
    parametros_type = []

    for par in parametros_iter:
        if (re.match(r'[A-zÀ-ÿ]+',par)):
            parametros_type.append(1)
        elif (re.match(r'[A-zÀ-ÿ]+\{(\d+)\}',par)):
            pattern = re.match(r'[A-zÀ-ÿ]+\{(\d+)\}',par)
            limit = int(pattern.group(1))
            for i in range(1,limit):
                next(par)
                if (not re.match(r'^$'),par):
                    print("Parâmetros mal definidos.(Número de colunas para lista incorretas.)")
                    return
            parametros_type.append(2)
            parametros_type.append(limit)
        elif (re.match(r'[A-zÀ-ÿ]+\{(\d+),(\d+)\}',par)):
            pattern = re.match(r'[A-zÀ-ÿ]+\{(\d+),(\d+)\}',par)
            minimum = int(pattern.group(1))
            maximum = int(pattern.group(2))
            if (maximum < minimum):
                print("Parâmetros mal definidos.(Intervalo de listas não fazem sentido.)")
                return
            for i in range(1,maximum):
                next(par)
                if (not re.match(r'^$'),par):
                    print("Parâmetros mal definidos.(Número de colunas para lista menor do que esperado.)")
                    return
            parametros_type.append(3)
            parametros_type.append(maximum)
        elif (re.match(r'[A-zÀ-ÿ]+\{(\d+),(\d+)\}::([A-zÀ-ÿ]+)',par)):
            pattern = re.match(r'[A-zÀ-ÿ]+\{(\d+),(\d+)\}::([A-zÀ-ÿ]+)',par)
            minimum = int(pattern.group(1))
            maximum = int(pattern.group(2))
            if (maximum < minimum):
                print("Parâmetros mal definidos.(Intervalo de listas não faz sentido.)")
                return
            for i in range(1,maximum):
                next(par)
                if (not re.match(r'^$'),par):
                    print("Parâmetros mal definidos.(Número de colunas para lista menor do que esperado.)")
                    return
            function = pattern.group(3)
            parametros_type.append(4)
            parametros_type.append(maximum)
            parametros_type.append(function)
        elif (re.match(r'^$'),par):
            parametros_type.append(5)
        else:
            parametros_type.append(0)

    if (parametros_type.count(0) > 0):
        print("Foi detetado um 0 nos parâmetros.")
        return

    ficheiro_escrita.write("[\n")
    for line in range(1,len(conteudo)-1):
        ficheiro_escrita.write("\t{\n")
        line_content = re.split(r',',conteudo[line])
        for i in range(0,len(line_content)-1):
            if (parametros_type[i] == 1):
                ficheiro_escrita.write('\t\t"' + parametros[i] + '": "' + line_content[i] + '"')
                if (i != len(line_content)):
                    ficheiro_escrita.write(',\n')
                else:
                    ficheiro_escrita.write('\n')
            elif (parametros_type[i] == 2):
                ficheiro_escrita.write('\t\t"' + parametros[i] + '": [')
                limit = parametros_type[i+1]
                for j in range(i,i+limit-1):
                    ficheiro_escrita.write(line_content[j])
                    if (j != i+limit-1):
                        ficheiro_escrita.write(',')
                ficheiro_escrita.write("]")
                if (i != len(line_content)):
                    ficheiro_escrita.write(',\n')
                else:
                    ficheiro_escrita.write('\n')
                i += 1
            elif (parametros_type[i] ==3):
                ficheiro_escrita.write('\t\t"' + parametros[i] + '": [')
                limit = parametros_type[i+1]
                for j in range(i,i+limit-1):
                    if (line_content[j] != ''):
                        ficheiro_escrita.write(line_content[j])
                        if (j != i+limit-1):
                            ficheiro_escrita.write(',')
                ficheiro_escrita.write("]")
                if (i != len(line_content)):
                    ficheiro_escrita.write(',\n')
                else:
                    ficheiro_escrita.write('\n')
                i += 1
            elif (parametros_type[i] ==4):
                function = parametros_type[i+2]
                ficheiro_escrita.write('\t\t' + parametros[i] + "_" + function + '": ')
                limit = parametros_type[i+1]
                lista = []
                for j in range(1,i+limit-1):
                    if (line_content[j] != ''):
                        lista.append(line_content[j])
                argument = "(["
                for z in range(0,len(lista)):
                    if (z == len(lista)):
                        argument += parametros[i]
                    else:
                        argument += (parametros[i] + ',')
                argument += "])"
                ficheiro_escrita.write(eval(function + argument))
                if (i != len(line_content)):
                    ficheiro_escrita.write(',\n')
                else:
                    ficheiro_escrita.write('\n')
                i += 2
        ficheiro_escrita.write('\t}')
        if (line != len(conteudo)):
            ficheiro_escrita.write(',\n')
        else:
            ficheiro_escrita.write('\n')
    ficheiro_escrita.write(']')
    ficheiro_escrita.close()

csv_to_json()
