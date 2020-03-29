from math import sqrt

ax = float(input('Insira a abcissa do ponto A:'))
ay = float(input('Insira a ordenada do ponto A:'))

bx = float(input('Insira a abcissa do ponto B:'))
by = float(input('Insira a ordenada do ponto B:'))

abDistancia = sqrt((ax - bx)**2) + ((ay + by)**2)
print('A distancia entre A e B é:', abDistancia)
