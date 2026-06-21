import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

dados = {
    'nota_previa': [7.5, 8.0, 6.0, 9.0, 5.5, 8.5, 7.0, 6.5, 9.5, 5.0],
    'frequencia': [85, 90, 80, 95, 75, 92, 88, 83, 97, 70],
    'participacao_atividades': [3, 4, 2, 5, 1, 4, 3, 3, 5, 2],
    'rendimento_final': [8.0, 9.5, 7.0, 10.0, 6.5, 9.0, 8.5, 7.5, 10.0, 6.0]
}


x = [[dados['nota_previa'][i], dados['frequencia'][i], dados['participacao_atividades'][i]]
     for i in range(len(dados['nota_previa']))]
y = dados['rendimento_final']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(x_train, y_train)

previsoes = modelo.predict(x_test)
mse = mean_squared_error(y_test, previsoes)

print(f"Erro quadrático médio: {mse:.2f}")

plt.scatter(y_test, previsoes)
plt.xlabel('Valores reais')
plt.ylabel('Previsões')
plt.title('Comparação entre valores reais e previsões')
plt.show()
