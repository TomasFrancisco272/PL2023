import myheart
import Distribution_Module as distribution

number_of_patients = 0

def file_to_module():
    heart = open("myheart.csv",'r')
    exec(open("./myheart.py").read())
    linhas = heart.readlines()
    try:
        for i in range(1,len(linhas)):
                dados = linhas[i].split(",")
                myheart.add_idade(dados[0])
                myheart.add_sexo(dados[1])
                myheart.add_tensao(dados[2])
                myheart.add_colesterol(dados[3])
                myheart.add_batimento(dados[4])
                myheart.add_temDoenca(dados[5])
                number_of_patients = number_of_patients + 1
    except:
        heart.close()

def doenca_por_sexo():
    atributos = distribution(["masculinos_doenca","masculinos_n_doenca","femininos_doenca","femininos_n_doenca"])
    for i in number_of_patients:
        if (myheart.sexo[i] == "Masculino"):
            if (myheart.temDoenca[i] == 1):
                atributos.masculinos_doenca = atributos.masculinos_doenca + 1
            else:
                atributos.masculinos_n_doenca = atributos.masculinos_n_doenca + 1
        else:
            if (myheart.temDoenca[i] == 1):
                atributos.femininos_doenca = atributos.femininos_doenca + 1
            else:
                atributos.femininos_n_doenca = atributos.femininos_n_doenca + 1

    print("Pacientes masculinos que tem a doenca:",atributos.masculinos_doenca)
    print("Pacientes masculinos que nao tem doenca",atributos.masculinos_n_doenca)
    print("Pacientes femininos que tem a doenca:",atributos.femininos_doenca)
    print("Pacientes femininos que nao tem a doenca:",atributos.femininos_n_doenca)

    return atributos

# def doenca_por_escalao_etario():
    escaloes_etarios = []
    ## limite_maximo = max(myheart.idade)
    for i in range(30, 77, 5): 
        novo_escalao = "idade" + i + (i+4) + "s" # s indica presença de doenca
        escaloes_etarios.append(novo_escalao)
        novo_escalao = "idade" + i + (i+4) + "n" # n indica não presença de doenca
        escaloes_etarios.append(novo_escalao)
    atributos = distribution(escaloes_etarios)
    #dicionario = vars(atributos)
    for i in number_of_patients: 
        if (myheart.temDoenca[i] == 1):
            if (30 <= myheart.idade[i] or myheart.idade[i] <= 34):
                atributos.idade3034s = atributos.idade3034s + 1
            elif (35 <= myheart.idade[i] or myheart.idade[i] <= 39):
                atributos.idade3539s = atributos.idade3539s + 1
            elif (40 <= myheart.idade[i] or myheart.idade[i] <= 44):
                atributos.idade4044s = atributos.idade4044s + 1
            elif (45 <= myheart.idade[i] or myheart.idade[i] <= 49):
                atributos.idade4549s = atributos.idade4549s + 1
            elif (50 <= myheart.idade[i] or myheart.idade[i] <= 54):
                atributos.idade5054s = atributos.idade5054s + 1
            elif (55 <= myheart.idade[i] or myheart.idade[i] <= 59):
                atributos.idade5559s = atributos.idade5559s + 1
            elif (60 <= myheart.idade[i] or myheart.idade[i] <= 64):
                atributos.idade6064s = atributos.idade6064s + 1
            elif (65 <= myheart.idade[i] or myheart.idade[i] <= 69):
                atributos.idade6569s = atributos.idade6569s + 1
            elif (70 <= myheart.idade[i] or myheart.idade[i] <= 74):
                atributos.idade7074s = atributos.idade7074s + 1
            elif (75 <= myheart.idade[i] or myheart.idade[i] <= 79):
                atributos.idade7579s = atributos.idade7579s + 1
        else:
            if (30 <= myheart.idade[i] or myheart.idade[i] <= 34):
                atributos.idade3034n = atributos.idade3034n + 1
            elif (35 <= myheart.idade[i] or myheart.idade[i] <= 39):
                atributos.idade3539n = atributos.idade3539n + 1
            elif (40 <= myheart.idade[i] or myheart.idade[i] <= 44):
                atributos.idade4044n = atributos.idade4044n + 1
            elif (45 <= myheart.idade[i] or myheart.idade[i] <= 49):
                atributos.idade4549n = atributos.idade4549n + 1
            elif (50 <= myheart.idade[i] or myheart.idade[i] <= 54):
                atributos.idade5054n = atributos.idade5054n + 1
            elif (55 <= myheart.idade[i] or myheart.idade[i] <= 59):
                atributos.idade5559n = atributos.idade5559n + 1
            elif (60 <= myheart.idade[i] or myheart.idade[i] <= 64):
                atributos.idade6064n = atributos.idade6064n + 1
            elif (65 <= myheart.idade[i] or myheart.idade[i] <= 69):
                atributos.idade6569n = atributos.idade6569n + 1
            elif (70 <= myheart.idade[i] or myheart.idade[i] <= 74):
                atributos.idade7074n = atributos.idade7074n + 1
            elif (75 <= myheart.idade[i] or myheart.idade[i] <= 79):
                atributos.idade7579n = atributos.idade7579n + 1
    return atributos

# def doenca_por_colesterol(): # 85 minimo e 603 maximo
    niveis_coleesterol = []
    for i in range(85, 603, 10):
        novo_nivel = "colesterol" + i + (i + 9) + "s"
        niveis_coleesterol.append(novo_nivel)
        novo_nivel = "colesterol" + i + (i + 9) + "n"
        niveis_coleesterol.append(novo_nivel)
    atributos = distribution(niveis_coleesterol)

def tabela_por_distribuicao(dist: distribution):
    atributos = dist.__dict__.keys()
    valores = dist.__dict__.values()
    for i in atributos:
        print(atributos[i],end="\t")
    print("\n")
    for i in valores:
        print(valores[i],end="\t")
    print("\n")

def tabela_distribuicoes():
    dist_por_sexo = doenca_por_sexo()
#    dist_por_escalao_etario = doenca_por_escalao_etario()
#    dist_por_colesterol = doenca_por_colesterol()
    tabela_por_distribuicao(dist_por_sexo)
#    tabela_por_distribuicao(dist_por_escalao_etario)
#    tabela_por_distribuicao(dist_por_colesterol)

def main():
    file_to_module()
    atributos = doenca_por_sexo()
    tabela_por_distribuicao(atributos)
    print("Working as intended.")