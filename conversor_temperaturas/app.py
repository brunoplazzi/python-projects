import modulo

def main():

    temp = float(0.0)
    tipo_entrada = int(0)
    tipo_saida = int()
    temp_convertida = float(0.0)
    tipo_formatado_entrada = str("")
    tipo_formatado_saida = str("")

    temp, tipo_entrada, tipo_saida = modulo.f_input_temperatura()

    temp_convertida = modulo.f_converte_temperaturas(temp, tipo_entrada, tipo_saida)

    tipo_formatado_entrada = modulo.f_formata_tipo(tipo_entrada)
    tipo_formatado_saida = modulo.f_formata_tipo(tipo_saida)
    print("%.2f%s --> %.2f%s"%(temp, tipo_formatado_entrada, temp_convertida, tipo_formatado_saida))

if __name__ == "__main__":
    main()