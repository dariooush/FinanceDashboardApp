import streamlit as st
import yfinance as yf
import pandas as pd

st.markdown('<iframe src="https://embed.lottiefiles.com/animation/99448"></iframe>', unsafe_allow_html=True)

st.title('Mohseni Finance Dashboard')

crypto_symbol_list = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'USDC-USD', 'BNB-USD', 'HEX-USD', 'XRP-USD', 'ADA-USD',
                      'SOL-USD', 'BUSD-USD', 'DOGE-USD', 'DOT-USD', 'AVAX-USD', 'WBTC-USD', 'STETH-USD', 'WTRX-USD',
                      'SHIB-USD', 'TRX-USD', 'DAI-USD', 'MATIC-USD', 'CRO-USD', 'LTC-USD', 'NEAR-USD', 'LEO-USD',
                      'FTT-USD', 'YOUC-USD', 'BCH-USD', 'UNI1-USD', 'LINK-USD', 'XLM-USD', 'ATOM-USD', 'BTCB-USD',
                      'ALGO-USD', 'FLOW-USD', 'XMR-USD', 'ETC-USD', 'APE3-USD', 'MANA-USD', 'HBAR-USD', 'VET-USD',
                      'EGLD-USD', 'ICP-USD', 'UST-USD', 'TONCOIN-USD', 'FIL-USD', 'SAND-USD', 'XTZ-USD', 'ZEC-USD',
                      'DFI-USD', 'WBNB-USD', 'LUNA1-USD']

tickers = (crypto_symbol_list)

dropDown = st.multiselect('Pick your assets', tickers)
startDate = st.date_input('Start Date', value=pd.to_datetime('2022-01-01'))
endDate = st.date_input('End Date', value=pd.to_datetime('today'))


def relativeReturn(df):
    rel = df.pct_change()
    cumret = (1 + rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


if len(dropDown) > 0:
    # df = yf.download(dropDown, startDate, endDate)['Adj Close']
    df = relativeReturn(yf.download(dropDown, startDate, endDate)['Adj Close'])
    st.subheader(f'Returns of {format(dropDown)}')
    st.line_chart(df)
