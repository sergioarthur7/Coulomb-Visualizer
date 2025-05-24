# ⚡ Coulomb Visualizer

Simulador Interativo da Força Elétrica baseado na **Lei de Coulomb**.

---

## 📚 Informações Iniciais

- **Escola:** EEEP Padre João Bosco de Lima  
- **Disciplina:** Física - Turma 3 Informática  
- **Professor:** Danilo  
- **Alunos:**
  - Douglas Lacerda - Nº 10  
  - Sérgio Arthur - Nº 40  
- **Tema:** Simulador Interativo da Força Elétrica (Lei de Coulomb)  
- **Data de Entrega:** _25/05/2025_

---

## ⚙️ Funcionamento do Programa

O **Coulomb Visualizer** foi desenvolvido em **Python** com o objetivo de simular e visualizar a força elétrica entre duas cargas puntiformes com base na **Lei de Coulomb**:

**F = k * |q₁ * q₂| / d²**

### Funcionalidades principais:

- Entrada interativa dos valores das cargas
- Cálculo automático da força elétrica para distâncias entre **0,1 m** e **5,0 m**
- Geração de gráfico representando a força em função da distância
- Exibição dos valores calculados
- Salvamento automático do gráfico em uma pasta específica

---

## 📈 Observações sobre o Comportamento da Força Elétrica

A força elétrica entre duas cargas:

- **Aumenta rapidamente** ao **diminuir a distância**
- **Diminui aceleradamente** ao **aumentar a distância**

O gráfico gerado ilustra essa **relação inversamente proporcional ao quadrado da distância**.

---

## 🧠 Dificuldades Encontradas e Soluções

Durante o desenvolvimento do simulador, enfrentamos e resolvemos os seguintes desafios:

- Validação personalizada das entradas do usuário
- Limpeza automática do terminal para melhorar a usabilidade
- Criação automática de pastas para organização dos gráficos gerados
- Interpretação gráfica da relação **força vs. distância**

---

## ✅ Considerações Finais

Este projeto foi essencial para reforçar o entendimento da **Lei de Coulomb** e demonstrar, de forma prática, como a **programação pode ser aplicada no estudo da Física**.

---

## 💻 Tecnologias Utilizadas

- Python 3
- [Numpy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- Módulo nativo `os`

### Instalação das Bibliotecas

```bash
python -m pip install numpy matplotlib
