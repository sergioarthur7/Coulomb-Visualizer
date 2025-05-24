import numpy as np #importa funções matemática
import matplotlib.pyplot as plt #Importa a biblioteca de plotagem de gráfico
import os #importa funções do Sistema Operacional

k = 8.99e9  # Constante eletrostática N·m²/C²

nome = input(str("Qual o seu nome? "))

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear') #função responsável por limpar o terminar toda vez que o programa for reiniciado

def vnumero(valor):  #verifica se o valor digitado é um valor númerio que pode ser convertido para decimal
    try:
        float(valor)
        return True
    except:   #caso não for ele retorna False (erro).
        return False

limpar()
print(f"Bem vindo {nome}!")

if not os.path.exists('graficos'):
    os.makedirs('graficos')


while True:
    print("\n--- Cálculo da Força Elétrica entre Duas Cargas ---")

    q1_entrada = input("Digite o valor da carga q1 (em Coulombs): ") # Pede valor 1
    q2_entrada = input("Digite o valor da carga q2 (em Coulombs): ") # Pede valor 2

    if vnumero(q1_entrada) and vnumero(q2_entrada): #se o valor 1 e valor 2  forem números...
        q1 = float(q1_entrada) # Converta valor 1 para decimal
        q2 = float(q2_entrada) # Converta valor 2 para decimal

        # Usa a biblioteca matemática para gerar as distâncias de 0.1 m até 5.0 m com passo de 0.1 m
        distancias = np.arange(0.1, 5.1, 0.1)

        # Calcula a força elétrica para cada distância guardada na váriavel "distancia"
        forcas = k * abs(q1 * q2) / distancias**2

        # Plota o gráfico na tela
        plt.figure(figsize=(10, 6)) 
        plt.plot(distancias, forcas, color='black', label='Força Elétrica (F)')
        plt.title('Força Elétrica entre Duas Cargas em Função da Distância')
        plt.xlabel('Distância (m)')
        plt.ylabel('Força Elétrica (N)')
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        nome_arquivo = f"graficos/forca_{q1}_{q2}.png" # Salva o gráfico dentro da pasta "graficos"
        plt.savefig(nome_arquivo)
        plt.show()

        limpar()

        # Exibindo os valores específicos das distâncias escolhidas
        print("\nForça elétrica em distâncias específicas:")
        for d in [0.1, 0.5, 1.0, 2.0, 5.0]:
            F = k * abs(q1 * q2) / d**2
            print(f"Distância: {d:.1f} m -> Força: {F:.2e} N")

        print("\nGráfico fechado. Reiniciando...\n")

    else:
        print("\nEntrada inválida! Por favor, digite valores numéricos reais para as cargas.")
