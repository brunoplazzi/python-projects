import pygame

class Coracao:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cor = (255,0,0)
        self.pos_x = 300
        self.pos_y = 200
        self.tamanho_max = 80
        self.tamanho_min = 60
        self.velocidade = 0.02

    def pintar_coracao(self, tela):

        tamanho = self.tamanho * 0.8

        #bolas do coracao
        pygame.draw.circle(tela, self.cor, (self.pos_x - tamanho//2, self.pos_y), self.tamanho // 2, 0)
        pygame.draw.circle(tela, self.cor, (self.pos_x + tamanho//2, self.pos_y), self.tamanho // 2, 0)

        #pontinha do coracao
        pontos = [(self.pos_x - tamanho * 1.059, self.pos_y * 1.06),
                  (self.pos_x + tamanho * 1.059, self.pos_y * 1.06),
                  (self.pos_x, self.pos_y + self.tamanho * 1.2)]

        pygame.draw.polygon(tela, self.cor, pontos, 0)

    def pulsar(self):

        self.tamanho += self.velocidade
        if self.tamanho > self.tamanho_max:
            self.velocidade *= -1
        if self.tamanho < self.tamanho_min:
            self.velocidade *= -1

def main():

    VERDE = (0, 255, 0)
    PRETO = (0, 0, 0)
    tamanho = 70
    pygame.init()

    tela = pygame.display.set_mode((600,400),0)

    coracao = Coracao(tamanho)

    while True:

        #calcular regras

        coracao.pulsar()

        #pintar na tela

        tela.fill(PRETO)
        coracao.pintar_coracao(tela)
        pygame.display.update()

        #capturar eventos
        for e in pygame.event.get():
            if e.type== pygame.QUIT:
                exit()

if __name__=="__main__":
    main()