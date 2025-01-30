def adivinhacao():
    print("Executando Jogo de Adivinhação")
    alvo = 25
    chances = 5
    acertou = False

    while chances > 0 and not acertou:
        try:
            chute = int(input("Digite um número inteiro entre 0 e 100 - "))
            chances-=1

            if chute == alvo:
                print("Parabéns! Adivinhou o número!")
                acetou = True
            else:
                if chute > alvo:
                    print("Não acertou!O número é menor que o seu palpite")
                else:
                    print("Não acertoumas. O número é maior que o seu palpite")
                

        except:
            print("Tente Novamente!")

    if not acertou:
        print("Que pena, o número era - ", + alvo)

def jokenpo():
    print("Executando Jogo de Jokenpo")
    import random

    print("Vamos jogar?")

    print("""
    pedra
        
    papel
        
    tesoura
        """)

    suaEscolha = input("Jogador - Escolha pedra, papel ou tesoura: ")
    minhaEscolha = random.choice(["pedra", "papel", "tesoura"])
    if suaEscolha == "pedra":
        if minhaEscolha == "tesoura":
            print("Jogador ganhou! Computador escolheu ", minhaEscolha)
        elif minhaEscolha == "papel":
            print("Jogador perdeu! Computador escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
    elif suaEscolha == "papel":
        if minhaEscolha == "tesoura":
            print("Jogador perdeu! Computador escolheu ", minhaEscolha)
        elif minhaEscolha == "pedra":
            print("Jogador ganhou! Computador escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
    elif suaEscolha == "tesoura":
        if minhaEscolha == "papel":
            print("Jogador ganhou! Computador escolheu ", minhaEscolha)
        elif minhaEscolha == "pedra":
            print("Jogador perdeu! Computador escolheu ", minhaEscolha)
        else:
            print("Empate! Ambos escolheram ", minhaEscolha)
    else:
        print("Algo deu errado!")
        
def quizz():
    print("Executando Jogo de Perguntas e Respostas")

    print("Vamos Começar? Quero ver se você é bom em matemática! Vou te dar três chances.")
    chance = 0
    pontos = 0
    while chance < 3:
        perguntas = ['1 - Qual é a soma de 37 + 26?', '2 - Qual é o resultado de  13 X 17?', '3 - Quanto é 56 - 18?']
        respostas = ["63" , "221" , "38"]
        if pontos == (len(perguntas)*10):
            print(f"Parabéns!! Acertou todas as perguntas e fez {pontos}!!")
            break
        for i in range(len(perguntas)):
            print(perguntas[i])
            respostaUsuario = str(input("Responda: "))
            
            if respostaUsuario != respostas[i]:
                if chance < 3:
                    chance += 1
                    pontos = 0
                    print(f"Perdeu a {chance}ª chance!")
                
                break
            else:
                pontos += 10

    if chance >= 3:
        print("Que pena! Precisamos revisar os estudos!")
        try:
            revisarQuestao = "s"
            questao = 0
            while revisarQuestao == "s":
                revisarQuestao = input("Quer saber a resposta de alguma questão? s/n? ")
                if revisarQuestao == "s":
                    questao = int(input("Informe o número da questão: ")) -1
                    for i in perguntas:
                        if i == perguntas[questao]:
                            print(perguntas[questao] + " : " + respostas[questao])
                else:
                    print("Até a próxima!!")
        except:
            print("Não entendi! Mas você pode começar novamente! Boa sorte!")
            
executando = True

while executando:

    print("""
        
        XBOX series S
        
        Escolha seu Jogo:
        
    1 - Adivinhação
        
    2 - Jokenpo
        
    3 - Perguntas e Respostas
        
    0 - Sair""")

    escolha = input("Escolha seu jogo: ")

    if escolha == "0":
        print("Até a próxima!!")
        executando = False
    elif escolha == "1":
        adivinhacao()
    elif escolha == "2":
        jokenpo()
    elif escolha == "3":
        quizz()
    else:
        print("Opção Inválida")
