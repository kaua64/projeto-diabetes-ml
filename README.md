# Projeto de Previsão de Diabetes com Machine Learning

## Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de Machine Learning com o objetivo de aplicar técnicas de aprendizado supervisionado na previsão de diabetes.

A partir de informações clínicas dos pacientes, o modelo é capaz de estimar se um paciente possui ou não diabetes, utilizando algoritmos de classificação disponíveis na biblioteca Scikit-Learn.

## Dataset Utilizado

Foi utilizado o dataset "Pima Indians Diabetes Database", amplamente utilizado em estudos acadêmicos de Machine Learning.

O conjunto de dados possui informações como:

- Número de gestações
- Nível de glicose
- Pressão arterial
- Espessura da pele
- Insulina
- Índice de Massa Corporal (BMI)
- Histórico familiar relacionado ao diabetes
- Idade
- Diagnóstico de diabetes

## Objetivo

O objetivo do projeto é prever a presença de diabetes em pacientes com base nas características presentes no dataset.

## Tecnologias Utilizadas

- Python
- Pandas
- Scikit-Learn

## Etapas Desenvolvidas

### 1. Estruturação do Projeto

Inicialmente foi criada a estrutura do projeto contendo:

- Dataset
- Arquivo principal da aplicação
- Arquivo de dependências
- Documentação

### 2. Leitura dos Dados

Os dados foram carregados utilizando a biblioteca Pandas para possibilitar a análise e o treinamento dos modelos.

### 3. Análise Exploratória

Foi realizada uma análise inicial para compreender melhor o conjunto de dados, verificando:

- Quantidade de registros
- Tipos de dados
- Estatísticas descritivas
- Distribuição dos pacientes com e sem diabetes

### 4. Treinamento dos Modelos

O dataset foi dividido em:

- 80% para treinamento
- 20% para testes

Foram avaliados três algoritmos supervisionados:

- Regressão Logística
- Árvore de Decisão
- Random Forest

### 5. Avaliação dos Resultados

Os modelos foram avaliados utilizando a métrica de acurácia.

| Modelo | Acurácia |
|----------|----------|
| Regressão Logística | 74,68% |
| Árvore de Decisão | 74,68% |
| Random Forest | 72,08% |

## Conclusão

Os resultados demonstraram que os modelos de Regressão Logística e Árvore de Decisão apresentaram o melhor desempenho para este conjunto de dados, alcançando uma acurácia de 74,68%.

O projeto permitiu aplicar na prática conceitos importantes de Machine Learning supervisionado, desde a preparação dos dados até a avaliação dos modelos treinados.

## Autor

Kauã