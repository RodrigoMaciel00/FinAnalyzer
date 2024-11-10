import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from utils import calcular_sma, calcular_ema, calcular_rsi, calcular_macd


def obter_dados_acao(ticker, periodo='1y'):
    try:
        print(f"Baixando dados para {ticker}...")
        dados = yf.download(ticker, period=periodo)

        if dados.empty:
            print(f"Nenhum dado encontrado para o símbolo '{ticker}'. Verifique se está correto.")
            return None
        return dados
    except Exception as e:
        print(f"Erro ao baixar dados: {e}")
        return None


def plotar_graficos(dados, ticker):

    dados['SMA20'] = calcular_sma(dados)
    dados['EMA20'] = calcular_ema(dados)
    dados['RSI'] = calcular_rsi(dados)
    dados['MACD'], dados['Signal'] = calcular_macd(dados)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

    ax1.plot(dados['Close'], label='Preço de Fechamento')
    ax1.plot(dados['SMA20'], label='SMA 20')
    ax1.plot(dados['EMA20'], label='EMA 20')
    ax1.set_title(f'Preço de Fechamento e Médias Móveis - {ticker}')
    ax1.legend()
    ax1.grid()

    ax2.plot(dados['RSI'], label='RSI', color='purple')
    ax2.axhline(70, linestyle='--', alpha=0.5, color='red')
    ax2.axhline(30, linestyle='--', alpha=0.5, color='green')
    ax2.set_title('Índice de Força Relativa (RSI)')
    ax2.legend()
    ax2.grid()

    ax3.plot(dados['MACD'], label='MACD', color='blue')
    ax3.plot(dados['Signal'], label='Signal Line', color='orange')
    ax3.set_title('MACD (Moving Average Convergence Divergence)')
    ax3.legend()
    ax3.grid()

    plt.tight_layout()
    plt.show()


ticker = input("Digite o símbolo da ação (por exemplo, AAPL para Apple): ").upper()
dados = obter_dados_acao(ticker)

if dados is not None:
    plotar_graficos(dados, ticker)
else:
    print("Erro ao obter dados. O programa será encerrado.")
