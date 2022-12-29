import streamlit  as st
import yfinance as yf
import plotly.graph_objs as go

def get_ticker_data(ticker_symbol, data_period, data_interval):
    ticker_data = yf.download(tickers=ticker_symbol, period=data_period, interval=data_interval)

    if len(ticker_data) == 0:
        st.write('Tidak dapat mendapatkan data ticker. Mohon untuk cek kembali entitas saham atau periode waktu yang diberikan')
    else:
        ticker_data.index = ticker_data.index.strftime("%d-%m-$Y %H:%M")
    return ticker_data

def plot_candle_chart(ticker_data):
    candle_fig = go.Figure()
    candle_fig.add_trace(
        go.Candlestick(
            x=ticker_data.index,
            open = ticker_data['Open'],
            close = ticker_data['Close'],
            low = ticker_data['Low'],
            high = ticker_data['High'],
            name= 'Market Data'
        )
    )
    candle_fig.update_layout(
            height=800,
    )
    st.write(candle_fig)