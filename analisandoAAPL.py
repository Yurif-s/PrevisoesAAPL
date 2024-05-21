# importando bibliotecas
import yfinance as yf
import mplfinance as mpf

# Baixando os dados da ação da Apple
dados = yf.download('AAPL', start='2024-04-01', end='2024-05-21')

# Gerando o gráfico
mpf.plot(dados.head(60), type='candle', figsize=(16,8), volume=True, mav=(7,14), style='yahoo')
