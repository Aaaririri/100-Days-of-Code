# Day 3: Treasure Island
"""
O objetivo é criar uma série de escolhas para o usuário, ate que o mesmo encontre o tesouro
"""
print("Bem Vindo a Ilha do Tesouro\nSua missao é encontrar o tesouro")
direction = input("Tem uma bifuraçao no seu caminho voce segue 'Direita' ou 'Esquerda': ")
if direction == 'Esquerda':
    path = input("Tem um lago a sua frente deseja 'Nadar' ou 'Esperar': ")
    if path == 'Esperar':
        door = input("Existem 3 portas a sua frente voce segue pela 'Vermelha','Amarela' ou 'Azul': ")
        if door == 'Amarela':
            print("Voce chegou a sala do tesouro, meus parabens!!!! YOU WIN")
        elif door == 'Vermelha':
            print("O chao e lava!!!")
        elif door == 'Azul':
            print("Voce acaba de ser engolido por um monstro das profundezas :( Game Over ")
        else:
            print("Isso não se faz, Game Over")
    elif path == 'Nadar':
        print("A correnteza e muito forte, nao da pra escapar!!! Game Over")
    else:
       print("Isso não se faz, Game Over")  
elif direction == 'Direita':
    print("Escolheste um caminho amaldicoado, a perdiçao lhe aguarda na floresta proibida, onde nunca escaparas, Game Over")
else:
    print("Isso não se faz, Game Over")       