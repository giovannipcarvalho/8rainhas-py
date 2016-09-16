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
    for x in rainhas:
        if x.ataca(i,j):
            return False
    return True

def colocarRainha(i, j):
    rainhas.append(rainha(i,j))
    tab[i][j]='R'

def removerRainha(i, j):
    if i <= len(rainhas)-1:
        rainhas.pop(i)
        tab[i][j]='*'

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
            if (j < 7):
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

def printar():
    for n in tab:
        for k in n:
            print k,
        print ""

preencherTab(0, 0, False)
printar()
