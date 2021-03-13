#Day 2 Project: Tip Calculator
"""
Calcular a gorjeta que deve ser paga por um grupo de amigos 
"""
print("Bem Vindos ao Tip Calculator")
total = float(input("Qual o valor total da conta? "))
porcentagem = int(input("Deseja pagar 10 12 ou 15 % de gorgeta? ")) * 0.01
pessoas = int(input("Quantas pessoas estão dividindo a conta? "))
print(f"O valor a ser pago por pessoa é R$ {(total/pessoas)+((total/pessoas)*porcentagem):.2f}")