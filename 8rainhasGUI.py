import pygame, time

class rainha:
    i = 0
    j = 0
    
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def ataca(self, i, j):
        if self.i == i or self.j == j:
            return True
        elif self.i + self.j == i + j or self.i-self.j == i - j:
            return True
        else:
            return False

rainhas = []
tab = [['*','*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*','*'],
       ['*','*','*','*','*','*','*','*']]

def posicaoLivre(i, j):
    interval = .04
    pintar(i, j, (0,255,0))
    for x in rainhas:
        if x.ataca(i,j):
            time.sleep(interval)
            pintar(i,j)
            return False
    time.sleep(interval)
    pintar(i,j)
    return True

def colocarRainha(i, j):
    rainhas.append(rainha(i,j))
    tab[i][j]='R'
    rainhaImg(i,j)
##    while True:
##        ev = pygame.event.wait()
##        if ev.type == pygame.KEYDOWN:
##            if ev.key == pygame.K_SPACE:
##                return
##        elif ev.type == pygame.QUIT:
##            pygame.quit()

def removerRainha(i, j):
    if i <= len(rainhas)-1:
        rainhas.pop(i)
        tab[i][j]='*'
    pintar(i,j)

def rainhaImg(i, j):
    img = pygame.image.load('rainha.png')
    img = pygame.transform.scale(img, (80,80))
    screen.blit(img, (j*80, i*80))
    pygame.display.update()

def preencherTab(i, j, backtrack):
    if not backtrack:
        if(posicaoLivre(i,j)):
            colocarRainha(i,j)
            if len(rainhas) == 8:
                return
            i+=1
            preencherTab(i, 0, False)
        else:
            j+=1
            if (j <= 7):
                preencherTab(i, j, False)
            else:
                i-=1
                preencherTab(rainhas[i].i, rainhas[i].j, True)
    else:
        removerRainha(i, j)
        j+=1
        if(j <= 7 and posicaoLivre(i,j)):
            colocarRainha(i,j)
            i+=1
            preencherTab(i, 0, False)
        else:
            j+=1
            if (j < 7):
                preencherTab(i, j, True)
            else:
                i-=1
                preencherTab(rainhas[i].i, rainhas[i].j, True)

def pintar(i, j, cor=""):
    colors = [(  0,  0,  0), #black
              (255,255,255)] #white
    if(i%2==0):
        pygame.draw.rect(screen, colors[j%2] if cor == "" else cor, [j*80, i*80, 80, 80])
    else:
        pygame.draw.rect(screen, colors[j%2==0] if cor == "" else cor, [j*80, i*80, 80, 80])
    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((640,640), pygame.FULLSCREEN)

pygame.display.set_caption("8Rainhas Demonstracao")

for i in range(8):
    for j in range(8):
        pintar(i,j)
pygame.display.update()

preencherTab(0, 0, False)

while True:
    ev = pygame.event.wait()
    if ev.type == pygame.MOUSEBUTTONDOWN:
        break

pygame.quit()
