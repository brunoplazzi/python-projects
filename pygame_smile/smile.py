import pygame
import math

def main():

    AMARELO = (255, 255, 0)
    PRETO = (0, 0, 0)
    VELOCIDADE = 0.1
    pi = math.pi


    pygame.init()

    tela = pygame.display.set_mode((600, 400), 0)

    class Smile:

        def __init__(self, tamanho):
            self.tamanho = tamanho
            self.centro_x = 300
            self.centro_y = 200
            self.raio = int(tamanho / 2)
            self.vel_x = 0
            self.vel_y = 0

        def pintar(self, tela):
            #pinta o corpo do smile
            pygame.draw.circle(tela, AMARELO, (int(self.centro_x), int(self.centro_y)), self.raio, 0)

            #pinta a boca do smile
            boca_x = self.centro_x - self.raio * 0.8
            boca_y = self.centro_y - self.raio * 0.9
            boca_largura = self.tamanho * 0.8
            boca_altura = self.tamanho * 0.85
            posicao_boca = (boca_x, boca_y, boca_largura, boca_altura)

            pygame.draw.arc(tela, PRETO, posicao_boca, pi, pi*2, 5)

            #pinta olho do smile
            olho_xe = self.centro_x - self.raio / 2.5
            olho_ye = self.centro_y - self.raio / 2.5
            olho_xd = self.centro_x + self.raio / 2.5
            olho_yd = self.centro_y - self.raio / 2.5
            pygame.draw.circle(tela, PRETO,(olho_xe, olho_ye), self.tamanho /10, 0)
            pygame.draw.circle(tela, PRETO, (olho_xd, olho_yd), self.tamanho / 10, 0)

        def calcular_regras(self):
            self.centro_x += self.vel_x
            self.centro_y += self.vel_y

            if self.centro_x + self.raio > 600 or self.centro_x - self.raio < 0:
                self.vel_x = 0
            if self.centro_y + self.raio > 400 or self.centro_y - self.raio < 0:
                self.vel_y = 0


        def procesar_eventos(self, eventos):
            for e in eventos:
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RIGHT:
                        self.vel_x = VELOCIDADE
                    if e.key == pygame.K_LEFT:
                        self.vel_x = -VELOCIDADE
                    if e.key == pygame.K_UP:
                        self.vel_y = -VELOCIDADE
                    if e.key == pygame.K_DOWN:
                        self.vel_y = VELOCIDADE
                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_RIGHT:
                        self.vel_x = 0
                    elif e.key == pygame.K_LEFT:
                        self.vel_x = 0
                    elif e.key == pygame.K_UP:
                        self.vel_y = 0
                    elif e.key == pygame.K_DOWN:
                        self.vel_y = 0



    smile = Smile(80)

    while True:
        # calcular regras
        smile.calcular_regras()

        # pintar na tela
        tela.fill(PRETO)
        smile.pintar(tela)
        pygame.display.update()

        # capturar eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        smile.procesar_eventos(eventos)

if __name__ == "__main__":
    main()
