import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from prophet import Prophet

# baixando os dados da Apple do yahoo
dados = yf.download('AAPL', start='2020-01-01', end='2024-12-31', progress=False)
dados = dados.reset_index()
dados_treino = dados[dados['Date'] < '2023-12-31']
dados_teste = dados[dados['Date'] >= '2023-12-31']
dados_prophet_treino = dados_treino[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})

# estabelendo os dados treino
modelo = Prophet(weekly_seasonality=True, #type: ignore
                 yearly_seasonality=True,  #type: ignore
                 daily_seasonality=False)  #type: ignore
modelo.add_country_holidays(country_name='US')
modelo.fit(dados_prophet_treino)

# definindo a previsao
futuro = modelo.make_future_dataframe(periods=450)
previsao = modelo.predict(futuro)

# desenhando o gráfico
plt.figure(figsize=(14, 8))
plt.plot(dados_treino['Date'], dados_treino['Close'], label='Dados de Treino', color='blue')
plt.plot(dados_teste['Date'], dados_teste['Close'], label='Dados Reais(Teste)', color='green')
plt.plot(previsao['ds'], previsao['yhat'], label='Previsão', color='orange', linestyle='--')
plt.axvline(dados_treino['Date'].max(), color='red', linestyle='--', label='Início da Previsão')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.title('Previsão de Preço de Fechamento vs Dados Reais')
plt.legend()
plt.savefig("Previsão_AAPL.png", dpi = 300)
plt.show()
