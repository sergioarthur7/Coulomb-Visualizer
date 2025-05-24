# Relatório de Física - Simulador da Lei de Coulomb

## Informações Iniciais

- **Escola:** EEEP Padre João Bosco de Lima  
- **Disciplina:** Física - Turma 3 Informática  
- **Professor:** Danilo  
- **Alunos:**
  - Douglas Lacerda - Nº 10  
  - Sérgio Arthur - Nº 40  
- **Tema:** Simulador Interativo da Força Elétrica (Lei de Coulomb)  
- **Data:** _(inserir data da entrega)_

---

## 1. Funcionamento do Programa

O programa desenvolvido em **Python** tem como objetivo simular e visualizar a força elétrica entre duas cargas puntiformes com base na **Lei de Coulomb**:

\[
F = k \cdot \frac{{|q_1 \cdot q_2|}}{{d^2}}
\]

### Funcionalidades principais:

- Entrada interativa dos valores das cargas
- Cálculo automático da força elétrica para distâncias entre **0,1 m** e **5,0 m**
- Geração de gráfico
- Exibição de valores específicos
- Salvamento automático do gráfico

---

## 2. Observações sobre o Comportamento da Força Elétrica

A força elétrica é **inversamente proporcional ao quadrado da distância** entre as cargas:

- Ao **diminuir a distância**, a força **aumenta rapidamente**
- Ao **aumentar a distância**, a força **diminui de forma acelerada**

O gráfico gerado demonstra essa relação com clareza.

---

## 3. Dificuldades Encontradas e Soluções

Durante o desenvolvimento, enfrentamos alguns desafios:

- Validação de entrada com função personalizada
- Limpeza automática do terminal
- Criação automática de pasta para salvar os gráficos
- Interpretação gráfica da relação força × distância

---

## 4. Considerações Finais

Este trabalho reforçou o entendimento da **Lei de Coulomb**, destacando o impacto da **distância** na força elétrica.

Além disso, aproximou os alunos da aplicação prática da **programação na Física**.

---

## 5. Tecnologias Utilizadas

- Python 3
- Numpy
- Matplotlib
- OS (módulo nativo)

### Instalação das Bibliotecas:

```bash
python -m pip install numpy matplotlib
