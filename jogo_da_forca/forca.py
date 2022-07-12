import mod

def main():

    loop_game = True
    palavra_resposta = ""
    tentativa = ""
    contador_tentativas = 6
    msg_final = ""

    print("***JOGO DA FORCA***")
    palavra_resposta = input("Digite a palavra do jogo: ").upper()
    palavra_canvas = mod.gera_pavavra_canvas(palavra_resposta)

    while(loop_game == True):

        print(palavra_canvas)
        print("TENTATIVAS RESTANTES: %d"%(contador_tentativas))
        tentativa = input("Qual é a letra? ").upper()

        if (tentativa in palavra_resposta):

            for i in range(len(palavra_canvas)):
                if(tentativa == palavra_resposta[i]):
                    palavra_canvas[i] = tentativa
        else:
            contador_tentativas -=1


        terminou, msg_final = mod.terminou(palavra_canvas, contador_tentativas)

        if(terminou):
            loop_game = False
            print(palavra_canvas)
            print(msg_final)
            print("FIM DO JOGO")

if __name__=="__main__":
    main()