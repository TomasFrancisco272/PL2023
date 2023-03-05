# Lista de dicionarios

dicts_ficheiro = []

def transfer_file_to_data():
    ficheiro = open("processos.txt","r")
    for linha in ficheiro:
        dicionario = {}
        items = linha.split("::")
        if (len(items) < 6):
            break
        else:
            dicionario["pasta"] = items[0]
            ano_mes_dia = items[1].split("-")
            dicionario["ano"] = ano_mes_dia[0]
            dicionario["mes"] = ano_mes_dia[1]
            dicionario["dia"] = ano_mes_dia[2]
            dicionario["nome"] = items[2]
            dicionario["pai"] = items[3]
            dicionario["mae"] = items[4]
            dicionario["extras"] = items[5]
            dicts_ficheiro.append(dicionario)

def processos_por_ano():
    result = {}
    for entry in dicts_ficheiro:
        ano = entry["ano"]
        result[ano] = result.setdefault(ano, 0) + 1
    return result

def det_seculo(seculo : str):
    half = len(seculo)//2
    sec = int(seculo[:half])
    if (int(seculo[half:]) != 0):
        sec += 1
    return sec

def det_nomes(nome : str):
    nomes = nome.split(" ")
    return nomes

def name_count_sorted(list_dicts):
    nomes = {}
    for i in list_dicts.values(): 
        for m,n in i.items():
            if (m in nomes.keys()):
                nomes[m] = nomes[m] + n
            else:
                nomes[m] = n
        nomes = dict(sorted(nomes.items(),key=lambda x: x[1]))
    return nomes

def nomes_por_seculo():
    result = {}
    for entry in dicts_ficheiro:
        seculo = det_seculo(entry["ano"])
        result[seculo] = result.setdefault(seculo,{})
        nomes = det_nomes(entry["nome"])
        proprio = nomes[0]
        apelido = nomes[-1]
        result[seculo][proprio] = result[seculo].setdefault(proprio,0) + 1
        result[seculo][apelido] = result[seculo].setdefault(apelido,0) + 1
    nomes = name_count_sorted(result)
    keys = list(nomes)
    for x in range(-1,-6,-1):
        print(str(keys[x]) + ":" + str(nomes[keys[x]]) + "\n")
    return(result)

transfer_file_to_data()
print(nomes_por_seculo())