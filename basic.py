import streamlit  as st
import plotly.graph_objs as go
import util

if __name__ == '__main__':
    ticker_symbol = st.sidebar.text_input(
        "Mohon masukkan entitas saham", 'MSFT'
    )
    data_period = st.sidebar.text_input('Period', '10d')
    data_interval = st.sidebar.radio('Interval', ['15m', '30m', '1h', '1d', '5d'])

    st.header = ticker_symbol

    ticker_data = util.get_ticker_data(ticker_symbol, data_period, data_interval)

    util.plot_candle_chart(ticker_data)