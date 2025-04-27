#Esse código é um jogo simples de adivinhação de animais.
#O jogador pensa em um animal e o programa tenta adivinhar qual é, fazendo perguntas.
#O jogo vai perguntar se o animal gosta de bananas, se sim, o jogo vai adivinhar que o animal é um macaco
#Se não, o jogo vai perguntar qual animal o jogador pensou e qual pergunta ele faria para diferenciar os dois animais.
#esse primeiro codigo é sobre a pergunta base que o jogo vai ter...

perguntas = [ ['Seu animal gosta de bananas', 'macaco'] ]

#esse segundo codigo é o loop do jogo, onde o jogador vai responder as perguntas e o jogo vai tentar adivinhar o animal que ele pensou.
while True:
    print('Pense em um animal...')

    #esse loop vai fazer as perguntas para o jogador e vai esperar a resposta dele.
    #se o jogador responder sim, o jogo vai adivinhar que o animal é um macaco, isso serve para as proximas perguntas também.
    acertou = False
    for pergunta in perguntas:
        resposta = input(f'{pergunta[0]} (s/n): ')
        if resposta.lower() == 's':
            print(f'Você pensou em {pergunta[1]}!')
            acertou = True
            break

    #se o jogador não acertou, o jogo vai perguntar qual animal ele pensou e qual pergunta ele faria para diferenciar os dois animais.
    #o jogo vai adicionar essa nova pergunta e animal na lista de perguntas.
    if not acertou: 
        animal = input('Desisto! Em qual animal você pensou? ')
        novapergunta = input('Qual pergunta você faria para diferenciar esse animal? ')
        
        # Adiciona a nova pergunta e o animal na lista de perguntas
        perguntas.append([ novapergunta, animal])

        # Pergunta para o jogador se ele gostaria de jogar novamente
        querjogarnovamente = input('Quer jogar novamente? (s/n): ')
        if querjogarnovamente.lower() != 's':
            print('Ok! Foi bom jogar com você!')
            break
