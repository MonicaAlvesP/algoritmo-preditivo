# Previsão de Rendimento Final com Regressão Linear

Exercício de faculdade para entender, na prática, como funciona um **algoritmo preditivo**: um modelo que aprende um padrão a partir de dados conhecidos e usa esse padrão pra "adivinhar" um valor novo, ainda não visto.

## A ideia por trás do código

Pensa assim: eu tenho 10 alunos. De cada um eu sei a **nota da prova prévia**, a **frequência** e o **quanto participou de atividades**. Eu também sei qual foi o **rendimento final** de cada um desses 10 alunos (porque o curso já acabou pra eles).

A pergunta que o algoritmo responde é: *"existe uma relação matemática entre essas três informações e o rendimento final?"*

Se existir, eu posso pegar um aluno **novo**, saber só a nota prévia, frequência e participação dele, e prever qual vai ser o rendimento final, sem precisar esperar o curso acabar.

Isso é **regressão linear**: o modelo tenta encontrar uma fórmula do tipo

```
rendimento_final = a * nota_previa + b * frequencia + c * participacao + d
```

onde `a`, `b`, `c` e `d` são números que o algoritmo calcula sozinho, ajustando essa "receita" pra que ela bata o mais perto possível dos rendimentos finais reais que você já tem nos dados.

## O que cada parte do código faz

| Etapa | O que acontece |
|---|---|
| `dados` | A "tabela" com as informações dos 10 alunos (variáveis de entrada + resultado real) |
| `x` e `y` | `x` são as variáveis que usamos pra prever (nota, frequência, participação); `y` é o que queremos prever (rendimento final) |
| `train_test_split` | Separa os alunos em dois grupos: um pra **ensinar** o modelo, outro pra **testar** se ele aprendeu direito |
| `LinearRegression()` + `.fit()` | É o momento em que o modelo "estuda" os dados de treino e calcula a fórmula (os valores de a, b, c, d) |
| `.predict()` | O modelo usa a fórmula aprendida pra prever o rendimento dos alunos do grupo de teste — alunos que ele **não viu** durante o treino |
| `mean_squared_error` | Mede o quanto as previsões erraram em relação aos valores reais. Quanto **menor**, melhor o modelo |
| `plt.scatter(...)` | Gráfico comparando previsão vs. realidade. Se os pontos formassem uma linha reta diagonal perfeita, o modelo teria acertado tudo |

## Por que separar treino e teste?

Esse é o ponto mais importante do exercício. Se você ensinar o modelo com **todos** os dados e depois testar ele com os **mesmos** dados, é meio que dar a prova com o gabarito colado, ele vai "acertar" porque já viu a resposta, não porque aprendeu o padrão de verdade.

Por isso `train_test_split` separa uma fatia (aqui, 20%) que o modelo **nunca vê** durante o treino. Só assim dá pra saber se ele realmente aprendeu a generalizar, ou só decorou os exemplos.

## Como rodar
1. Certifique-se de ter o Python instalado e configurado no seu sistema.

2. Abra a pasta do projeto onde você clonou ou baixou este repositório.

3. Siga os comandos abaixo para criar um ambiente virtual, instalar as dependências e rodar o código:

> O ambiente virtual é uma forma de isolar as dependências do projeto, garantindo que as bibliotecas necessárias sejam instaladas sem afetar outras partes do seu sistema.

```bash
python -m venv venv
source venv/bin/activate  
# No Windows: venv\Scripts\activate
pip install scikit-learn matplotlib
python main.py
```

A saída no terminal mostra o erro quadrático médio (MSE), e uma janela abre com o gráfico de comparação.

___
