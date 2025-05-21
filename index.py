import numpy as np
import matplotlib.pyplot as plt

# Constante eletrostática de Coulomb
k = 8.99e9  # N·m²/C²

while True:
    print("\n--- Cálculo da Força Elétrica entre Duas Cargas ---")

    # Entrada do usuário
    try:
        q1 = float(input("Digite o valor da carga q1 (em Coulombs): "))
        q2 = float(input("Digite o valor da carga q2 (em Coulombs): "))
    except ValueError:
        print("Entrada inválida! Por favor, digite valores numéricos.")
        continue

    # Geração das distâncias de 0.1 m até 5.0 m com passo de 0.1 m
    distancias = np.arange(0.1, 5.1, 0.1)

    # Cálculo da força elétrica para cada distância
    forcas = k * abs(q1 * q2) / distancias**2

    # Plotando o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(distancias, forcas, color='blue', label='Força Elétrica (F)')
    plt.title('Força Elétrica entre Duas Cargas em Função da Distância')
    plt.xlabel('Distância (m)')
    plt.ylabel('Força Elétrica (N)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Exibindo os valores específicos
    print("\nForça elétrica em distâncias específicas:")
    for d in [0.1, 0.5, 1.0, 2.0, 5.0]:
        F = k * abs(q1 * q2) / d**2
        print(f"Distância: {d:.1f} m -> Força: {F:.2e} N")

    print("\nGráfico fechado. Reiniciando...\n")
