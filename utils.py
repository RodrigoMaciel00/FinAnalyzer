import pandas as pd

def calcular_sma(dados, periodo=20):
    return dados['Close'].rolling(window=periodo).mean()

def calcular_ema(dados, periodo=20):
    return dados['Close'].ewm(span=periodo, adjust=False).mean()

def calcular_rsi(dados, periodo=14):
    delta = dados['Close'].diff(1)
    ganho = delta.where(delta > 0, 0)
    perda = -delta.where(delta < 0, 0)

    ganho_medio = ganho.rolling(window=periodo).mean()
    perda_media = perda.rolling(window=periodo).mean()

    rs = ganho_medio / perda_media
    return 100 - (100 / (1 + rs))

def calcular_macd(dados):
    ema12 = calcular_ema(dados, 12)
    ema26 = calcular_ema(dados, 26)
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal
