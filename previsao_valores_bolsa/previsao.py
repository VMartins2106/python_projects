import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date

def carregar_dados(ticker, dt_inicial, dt_final):
    df = yf.Ticker(ticker).history(start= dt_inicial.strftime("%Y-%m-%d"), 
    end= dt_final.strftime("%Y-%m-%d"))
    return df

def prever_dados(df, periodo):
    df.reset_index(inplace=True)

    df = df.loc[:,['Date', 'Close']]
    df['Date'] = df['Date'].dt.tz_localize(None)
    df.rename(columns={"Date": "ds", 'Close': "y"}, inplace=True)

    modelo = Prophet()
    modelo.fit(df)

    datas_futuras = modelo.make_future_dataframe(periods=int(periodo) * 30)
    previsoes = modelo.predict(datas_futuras)

    return modelo, previsoes

lista_tickers = ["PETR4.SA","AMZN","MGLU3.SA",
    "BBAS3.SA", "BBD","GOOG","MSFT","TSLA","WBD"
]

tickers = {
    "PETR4.SA": "Petrobras",
    "AMZN": "Amazon",
    "MGLU3.SA": "Magazine Luiza",
    "BBAS3.SA": "Banco do Brasil",
    "BBD": "Banco do Bradesco",
    "GOOG": "Google",
    "APPL": "Apple",
    "MSFT": "Microsoft",
    "TSLA": "Tesla",
    "WBD": "Warner Bros"
}

st.markdown("""
# Análise preditiva
### Prevendo valor de ações na bolsa de valores
""")

st.image("logo.jpg")

with st.sidebar:
    st.header("Menu")
    ticker = st.selectbox("Selecione a ação: ", lista_tickers)
    dt_inicial = st.date_input("Data inicial", value=date(2020,1,1))
    dt_final = st.date_input("Data inicial")
    meses = st.number_input("Meses de previsão", 1, 24, 6)

dados = carregar_dados(ticker, dt_inicial, dt_final)

if dados.shape[0] != 0:

    st.header(f"Dados da ação - {tickers[ticker]}")

    st.dataframe(data=dados, width=700, height=300, use_container_width=False)

    st.subheader("Variação do período")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dados.index, y=dados['Close'], name="Open"))
    st.plotly_chart(fig)

    if meses == 1:
        st.header(f"Previsão para o próximo {meses} mês")
    elif meses != 1:
        st.header(f"Previsão para os próximos {meses} meses")

    modelo, previsoes = prever_dados(dados,meses)
    fig = plot_plotly(modelo, previsoes, xlabel="período", ylabel="valor",figsize=(800, 600))
    st.plotly_chart(fig)

else:
    st.warning("Nenhum dado encontrado no período selecionado")