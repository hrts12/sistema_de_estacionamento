#SISTEMA DE ESTACIONAMENTO
import os
from datetime import datetime #importaçao da biblioteca datetime ao codigo

vagas = 20
placas = [None] * vagas
hora_entrada = [None] * vagas
carros = 0
valor_minuto = 0.2
lucro = 0
cond = True
historico = []

def limpar_terminal(): #funçao criada para limpar terminal
    if(os.name == 'nt'):
        os.system('cls')

while(cond):
    opcao = input("\nDigite uma das opções abaixo:\n \n 1 para adicionar um carro\n 2 para deletar um carro\n 3 para encerrar o dia\n 4 para exibir os carros no estacionamento\n 5 para exibir o historico\n (clique V para voltar)\n \nDigite aqui: ")
    if(opcao == "1"):
        if(carros < vagas):
            limpar_terminal()
            placa = input("\nDigite a placa do carro: ")
            if(placa.lower() == "v"):
                limpar_terminal()
                continue
            elif(placa in placas):
                limpar_terminal()
                print("Não permitimos placas iguais")
                continue
            else:
                placas[carros] = placa
                hora_entrada[carros] = datetime.now()
                carros += 1
                limpar_terminal()
        else:
            print("\nO estacionamento está lotado")

    elif(opcao == "2" and carros > 0):
        limpar_terminal()
        rep1 = True
        while(rep1):
            tolerancia = input("\nO carro está estacionado há mais de 20 minutos? Digite (S) para sim e (N) para não: ").lower()
            if(tolerancia == "v"):
                limpar_terminal()
                rep1 = False
                continue 
            elif(tolerancia == "s"):
                rep1 = False
                placa = input("\nDigite a placa do carro a ser removido: ")
                if(placa == "v"):
                    limpar_terminal()
                    rep1 = False
                    continue 
                elif(placa not in placas):
                    limpar_terminal()
                    print("Placa inexistente, repita o processo")
                    continue
                for i in range(carros):
                    if(placas[i] == placa):
                        hora_saida = datetime.now()
                        hora_saida_digitada = input("Digite a hora de saída do carro (formato 24 horas, exemplo: 14:30): ") #sistema que adiciona o datetime ao codigo
                        if(hora_saida_digitada.lower() == "v"):
                            limpar_terminal()
                            rep1 = False
                            continue
                        if(':' not in hora_saida_digitada):
                            limpar_terminal()
                            print("Formato de hora inválido, repita o processo")
                            continue

                        try:
                            hora_saida_horas, hora_saida_minutos = map(int, hora_saida_digitada.split(':'))
                            if(hora_saida_horas > 24 or hora_saida_horas < 0 or hora_saida_minutos >= 60 or hora_saida_minutos < 0): #sistema para estipular o tempo em numeros de horas e dias
                                raise ValueError
                        except ValueError:
                            limpar_terminal()
                            print("Hora inválida, repita o processo")
                            continue
                        hora_saida = hora_saida.replace(hour=hora_saida_horas, minute = hora_saida_minutos, second = 0, microsecond = 0) #calcula a quantia de horas que o carros ficou no estacionamento
                        horas_total = (hora_saida - hora_entrada[i]).total_seconds() / 3600
                        valor_pagar = valor_minuto * horas_total * 59
                        limpar_terminal()

                        rep2 = True
                        while(rep2):
                            confirmacao = input(f"\nValor a pagar para o carro de placa {placas[i]} é de {valor_pagar:.2f} reais (clique C para confirmar o valor): ").lower()
                            if(confirmacao == "v"):
                                limpar_terminal()
                                rep1  = False
                                rep2 = False
                                continue 
                            elif(confirmacao == "c"):
                                lucro += valor_pagar
                                placas.pop(i)
                                hora_entrada.pop(i)
                                carros -= 1
                                rep1 = False
                                rep2 = False
                                limpar_terminal()
                                if(len(historico) >= 10): #guarda a placa do carro a sair no sistema
                                    historico.pop(0)
                                historico.append(placa)
                            else: 
                                limpar_terminal()
                                rep2 = True

            elif(tolerancia == "n"):
                rep1 = False
                placa = input("\nDigite a placa do carro a ser removido: ")
                if(placa == "v"):
                    limpar_terminal()
                    rep1 = False
                    continue 
                elif(placa not in placas):
                    limpar_terminal()
                    print("Placa inexistente, repita o processo")
                    continue
                for i in range(carros):
                    if(placas[i] == placa):
                        placas.pop(i)
                        hora_entrada.pop(i)
                        carros -= 1
                        limpar_terminal()

                        if(len(historico) >= 10): #guarda a placa do carro a sair no sistema
                            historico.pop(0)
                        historico.append(placa)
            else:
                limpar_terminal()
                rep1 = True

    elif(opcao == "3"):
        limpar_terminal()
        print("Dia encerrado")
        print(f"O total de carros no estacionamento é de {carros} e o lucro do dia foi de {lucro:.2f}")
        rep3 = True
        while(rep3):
            proximo_dia = input("\nVocê deseja abrir o estacionamento novamente? Digite (S) para sim, (N) para não e (V) para voltar: ").lower()
            if(proximo_dia == "v"):
                limpar_terminal()
                rep3 = False
                continue
            if(proximo_dia == "s"):
                limpar_terminal()
                rep3 = False
                continue
            elif(proximo_dia == "n"):
                limpar_terminal()
                rep3 = False
                cond = False
            else:
                limpar_terminal()
            
    elif(opcao == "4"):
        limpar_terminal() #exibe a quantia de carros atualmento no estacionamento
        print(placas[:carros])

    elif(opcao == "5"):
        limpar_terminal()
        print("Histórico das últimas 10 placas que deixaram o estacionamento: ")
        if(len(historico) > 0):
            for item in historico[-10:]: #pega no sistema e exibe as placas no estacionamento
                print({item})
        else:
            print("0")

    elif(opcao.lower() == "v"):
        limpar_terminal()
        continue

    else:
        limpar_terminal()
        print("Opção inválida, digite uma das opções novamente")