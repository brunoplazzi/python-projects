def gera_pavavra_canvas(palavra_resposta):
    canvas = []
    espaco = "_"

    for letra in palavra_resposta:
        canvas.append(espaco)

    return canvas

def terminou(palavra_canvas, contador_tentativas):
    terminou = True
    msg = "VOCÊ VENCEU!"

    for i in range(len(palavra_canvas)):
        if (palavra_canvas[i] == "_"):
            terminou = False

    if (contador_tentativas == 0):
        terminou = True
        msg = "TENTATIVAS ESGOTADAS!"

    return terminou, msg
