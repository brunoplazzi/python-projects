import pygame

def main():

    VERMELHO = (255, 0, 0)
    PRETO = (0, 0, 0)

    pygame.init()

    tela = pygame.display.set_mode((1200, 600), 0)

    class Bolinha:

        def __init__(self, tamanho):
            self.tamanho = tamanho
            self.raio = self.tamanho // 2
            self.centro_x = 100
            self.centro_y = 100
            self.vel_x = 0.3
            self.vel_y = 0

        def pintar_bolinha(self, tela):

            pygame.draw.circle(tela, VERMELHO, (self.centro_x, self.centro_y), self.raio, 0)

        def calcular_regras(self):

            self.vel_y += 0.002
            self.centro_y += self.vel_y

            self.centro_x += self.vel_x


            if self.centro_y + self.raio > 600:
                self.centro_y = 600 - self.raio
                self.vel_y = - self.vel_y


            if self.centro_x + self.raio > 1200 or self.centro_x - self.raio < 0:
                self.vel_x *= -1

    bolinha = Bolinha(60)

    while True:

        #calcula regras

        bolinha.calcular_regras()

        #desenha na tela
        tela.fill(PRETO)
        bolinha.pintar_bolinha(tela)
        pygame.display.update()


        #captura de eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()

if __name__=="__main__":
    main()