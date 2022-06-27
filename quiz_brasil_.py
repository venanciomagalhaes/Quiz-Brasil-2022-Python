def menu():
    print("""
----------------------------- Seja Bem vindo ao Quiz Brasil! -----------------------------


Orientações:

1 - Serão apresentadas 10 pergutas sobre história geral do Brasil. 
Dessas questões, 8 são do tipo objetiva, contendo 4 opções de respostas, 
sendo apenas uma delas a verdadeira. 

2 - Uma vez respondida, não será possível retornar para a questão. 

3 -  A cada resposta correta um ponto será computado e no fim você será
receberá um Títulos abaixo: 

    Imperador(a) -------------------------------------------------------- \t10 acertos
    Duque(sa) ----------------------------------------------------------- \t7 a 9 acertos
    Marquês(a) ---------------------------------------------------------- \t6 acertos
    Conde(ssa) ---------------------------------------------------------- \t3 a 5 acertos
    Visconde(ssa) ------------------------------------------------------- \t0 a 2 acertos

""")



def quizBrasil():
    amarelo = '\033[1;33m'
    vermelho = '\033[1;31m'
    verde = '\033[1;32m'
    reset = '\033[0;0m	'

    menu()

    pontos = 0

    perguntas = {'Pergunta1': 'Questão 1 - Em qual ano foi declarada a  Independência do Brasil?\n\n'
                              'A) 1820\nB) 1822\nC) 1824\nD) Nenhuma das anteriores\n',
                 'Pergunta2': 'Questão 2 - Em qual ano foi declarada a abolição da escravatura em solo nacional?\n\n'
                              'A) 1886\nB) 1887\nC) 1888\nD) 1889\n',
                 'Pergunta3': 'Questão 3 - Оѕ Аtоѕ Іnѕtіtuсіоnаіѕ, implementados sob a Ditadura Militar fоrаm еlаbоrаdоѕ раrа\n'
                              'quе оѕ mіlіtаrеѕ tіvеѕѕеm um mаіоr dоmínіо ѕоbrе tоdо о сеnárіо brаѕіlеіrо, аѕѕіm dеtіnhаm dе\n'
                              'роdеrеѕ quе nãо ѕеrіаm lіmіtаdоѕ реlа Соnѕtіtuіçãо Вrаѕіlеіrа. Quаl fоі Аtо Іnѕtіtuсіоnаl quе\n'
                              'саuѕоu mаіоr іmрасtо nо Вrаѕіl?\n\n'
                              'A) Ato Institucional nº 2\nB) Ato Institucional nº 3\nC) Ato Institucional nº 4\nD) Ato Institucional nº 5\n',
                 'Pergunta4': 'Questão 4 - А аbеrturа роlítіса fоі umа fоrmа dе іnісіаr о рrосеѕѕо dе trаnѕіçãо еntrе о gоvеrnо dіtаdоr е \n'
                              'о gоvеrnо dеmосrátісо brаѕіlеіrо, асоntесеu dе fоrmа lеntа е grаduаl раrа quе оѕ dіrеіtоѕ рudеѕѕеm rеіntеgrаr\n'
                              'mіlіtаrеѕ е сіvіѕ nо mеѕmо сеnárіо nасіоnаl. Quаl fоі а Lеі quе mudоu о сеnárіо nасіоnаl?\n\n'
                              'A) Lei de Salvação\nB) Lei de Liberdade\nC) Lei de Anistia\nD) Lei do Perdão\n',
                 'Pergunta5': 'Questão 5 - Quеm fоі о рrеѕіdеntе quе аѕѕumіu о роdеr, а раrtіr dа Rеvоluçãо dе 1930?\n\n'
                              'A) Flоrіаnо Реіхоtо\nB) Gеtúlіо Vаrgаѕ\nC) Fеrnаndо Неnrіquе\nD) Rоdrіguеz Аlvеѕ\n',
                 'Pergunta6': 'Questão 6 - Em que ano Dom João VI veio para o Brasil?\n\n'
                              'A) 1800\nB) 1808\nC) 1822\nD) 1922',
                 'Pergunta7': 'Questão 7 - Complete: ao chegar no Brasil, Dom João VI fez a abertura dos portos, acabando com o ___.\n\n'
                              'Dica: duas palavras.\n',
                 'Pergunta8': 'Questão 8 - Na época em que Dom João VI e sua família vieram para o Brasil, quem era o imperador da França?\n\n'
                              'Dica: pequena estatura (Obs: a acentuação será considerada)\n',
                 'Pergunta9': 'Questão 9 - Соmо fоі сhаmаdо о gоlре quе fаzіа а аntесіраçãо dа mаіоrіdаdе dе Dоm Реdrо ІІ, fаzеndо\n'
                              'соm quе еlе соmаndаѕѕе о Вrаѕіl ѕеm ѕеr mаіоr dе іdаdе?\n\n'
                              'A) Gоlре јоvіаl\nB) Gоlре dа mаіоrіdаdе\nC) Rеvоluçãо dе 1830\nD) Gоlре dо rеіnаdо јоvіаl\n',
                 'Pergunta10': 'Questão 10 - Famoso riacho em cujas margens fora proclamada a Independência do Brasil por Dom Pedro I:\n\n'
                               'A) Tietê\nB) Pardino\nC) Rio Doce\nD) Ipiranga\n'}

    respostas = {'Resposta1': 'B',
                 'Resposta2': 'C',
                 'Resposta3': 'D',
                 'Resposta4': 'C',
                 'Resposta5': 'B',
                 'Resposta6': 'B',
                 'Resposta7': 'PACTOCOLONIAL',
                 'Resposta8': 'NAPOLEÃOBONAPARTE',
                 'Resposta9': 'B',
                 'Resposta10': 'D',
                 }

    contador = 0
    for pergunta in perguntas.values():
        contador += 1

        print(pergunta)

        resposta = input('Insira aqui a sua resposta: ').upper().strip()
        print('\n')

        if pergunta == perguntas['Pergunta7'] or pergunta == perguntas['Pergunta8']:

            while not resposta.isalpha():
                resposta = input('Insira aqui a sua resposta: ').upper().replace(' ', '')
                print('\n')

        else:

            while not resposta.isalpha() or resposta.isspace() or resposta not in ['A', 'B', 'C', 'D']:
                resposta = input('Insira aqui a sua resposta: ').upper().replace(' ', '')
                print('\n')

        if resposta == respostas[f'Resposta{contador}']:
            pontos += 1

    print('SEU RESULTADO:\n')

    if pontos == 10:
        print(f'{verde}Parabéns!!! Você é um(a) Imperador(a) quando o assunto é História do Brasil!{reset}')
        print(f'Total de acertos: {pontos}\n')
    elif pontos >= 7:
        print(f'{verde}Parabéns!!! Você é um(a) Duque(sa) quando o assunto é História do Brasil!{reset}')
        print(f'Total de acertos: {pontos}\n')
    elif pontos == 6:
        print(f'{amarelo}Parabéns!!! Você é um(a) Marquês(a) quando o assunto é História do Brasil!{reset}')
        print(f'Total de acertos: {pontos}\n')
    elif pontos >= 3 and pontos <= 5:
        print(f'{amarelo}Não dasanime!!!  Você é um(a) Conde(ssa) quando o assunto é História do Brasil!{reset}')
        print(f'Total de acertos: {pontos}\n')
    else:
        print(
            f'{vermelho}Parece que você ainda tem muito o que aprender para um(a) Visconde(ssa) em História do Brasil!{reset}')
        print(f'Total de acertos: {pontos}\n')


quizBrasil()
