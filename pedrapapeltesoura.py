import random

print("ola, bem vindo ao mini game da juju ")
opcoes = ["Pedra", "Papel", "Tesoura"]

while True:
    escolhausuario = input("escolha: pedra, papel ,tesoura ou sair ")
    escolhaComputador = random.choice(opcoes)
    print(escolhaComputador)

    if escolhausuario == escolhaComputador:
      print("empatou ")

    elif escolhausuario == "pedra" and escolhaComputador == "tesoura":
         print("voce ganhou ")

    elif escolhausuario == "pedra" and escolhaComputador == "papel":
        print("O computador venceu ")

    elif escolhausuario == "tesoura" and escolhaComputador == "pedra":
        print("o computador ganhou ")

    elif escolhausuario == "tesoura" and escolhaComputador == "papel":
        print("voce venceu ")

    elif escolhausuario == "papel" and escolhaComputador == "pedra":
        print("voce ganhou ")

    elif escolhausuario == "papel" and escolhaComputador == "tesoura":
        print("O computador venceu ")
else:
    print("obrigado po sua visita")




