#recebe os inputs, valida e retorna seus valores
def f_input_temperatura():

    temp = float(input("Digite a temperatura: "))
    tipo_entrada = int(input("A temperatura está em: [1]CELSIUS [2]FAHRENHEIT [3]KELVIN\n"))

    while(tipo_entrada < 1 or tipo_entrada > 3):
        print("VALOR INVALIDO! DIGITE UMAS DAS OPÇÕES FORNECIDAS")
        tipo_entrada = int(input("A temperatura está em:: [1]CELSIUS [2]FAHRENHEIT [3]KELVIN\n"))

    tipo_saida = int(input("Deseja saber a temperatura em: [1]CELSIUS [2]FAHRENHEIT [3]KELVIN\n"))

    while (tipo_saida < 1 or tipo_saida > 3):
        print("VALOR INVALIDO! DIGITE UMAS DAS OPÇÕES FORNECIDAS")
        tipo_saida = int(input("Deseja saber a temperatura em: [1]CELSIUS [2]FAHRENHEIT [3]KELVIN\n"))

    return temp, tipo_entrada, tipo_saida


#recebe um valor float que representa a temp em celsius e retorna um float da temp em fahrenheit.
def f_cel_to_fah(temp):

    c = temp
    f = ((9*c)+160)/5

    return f

#recebe um valor que representa a temp em fahrenheit e retorna um float da temp em celsius
def f_fah_to_cel(temp):

    f = temp
    c = (5*(f-32))/9

    return c

#recebe valor em celsius e converte em kelvin
def f_cel_to_kel(temp):
    c = temp
    k = c + 273
    return k

#recebe valor em kelvin e converte em celsius
def f_kel_to_cel(temp):
    k = temp
    c = k - 273
    return c

def f_formata_tipo(tipo):
    t = tipo
    tipo_format = str("")

    if(t == 1):
        tipo_format = "°C"
    if(t == 2):
        tipo_format = "°F"
    if(t == 3):
        tipo_format = "K"

    return tipo_format

def f_converte_temperaturas(temp, tipo_in, tipo_out):

    t_in = tipo_in
    t_out = tipo_out
    temp_inicial = temp
    temp_final = float(0.0)

    if(t_in == 1):
        if(t_out == 2):
            temp_final = f_cel_to_fah(temp_inicial)
        elif(t_out == 3):
            temp_final = f_cel_to_kel(temp_inicial)
        else:
            temp_final = temp_inicial

    if(t_in == 2):
        if(t_out == 1):
            temp_final = f_fah_to_cel(temp_inicial)
        elif(t_out == 3):
            temp_final = f_fah_to_cel(temp_inicial)
            temp_final = f_cel_to_kel(temp_final)
        else:
            temp_final = temp_inicial

    if(t_in == 3):
        if(t_out == 1):
            temp_final = f_kel_to_cel(temp_inicial)
        elif(t_out == 2):
            temp_final = f_kel_to_cel(temp_inicial)
            temp_final = f_cel_to_fah(temp_final)
        else:
            temp_final = temp_inicial

    return temp_final