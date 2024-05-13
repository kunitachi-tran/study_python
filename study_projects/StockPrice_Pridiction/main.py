custom_css = """
<style>
/* Center align all content */
.centered {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
</style>
"""

from vnstock3 import Vnstock
import streamlit as st
from datetime import date, timedelta

from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

TODAY = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
START = "2015-01-01"

# Create a section with centered alignment
st.markdown('<div class="centered-section">', unsafe_allow_html=True)
st.title("Ứng dụng dự đoán giá cổ phiếu")
st.markdown(custom_css, unsafe_allow_html=True)

stock_list = ("VCB", "BID", "CTG", "ACB", "TCB", "MBB", "VPB", "VIB", "TPB", "HCM","SSI","SHS","VCI", "VND", "HPG", "HSG", "NKG", "MWG", "DGW", "MSN", "FPT", "DGC")

selected_stocks = st.selectbox(label="Hãy chọn cổ phiếu nào: ", options=stock_list)

n_years = st.slider("Năm dự đoán:", 1, 4)
period = n_years * 365

stock = Vnstock().stock(symbol='VN30F1M', source='VCI')

@st.cache_data
def load_data(ticker):
    data = stock.quote.history(symbol=ticker,start=START, end=TODAY)
    return data

data_load_state = st.text("Đang tải dữ liệu...")
data = load_data(selected_stocks)
data_load_state = st.text("Đã tải dữ liệu xong!")

st.subheader("Dữ liệu gốc")
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["time"], y=data["open"], name="Mở cửa"))
    fig.add_trace(go.Scatter(x=data["time"], y=data["close"], name="Đóng cửa"))
    fig.layout.update(title_text=f"Đồ thị giá cổ phiếu {selected_stocks}", xaxis_rangeslider_visible=True, width=1000, height=1000)
    st.plotly_chart(fig)

plot_raw_data()

#Forcasting
df_train = data[["time", "close"]]
df_train = df_train.rename(columns={"time": "ds", "close": "y"})

m = Prophet()
m.fit(df=df_train)
future = m.make_future_dataframe(periods=period)
forcast = m.predict(future)

st.subheader("Dữ liệu dự báo")
st.write(forcast.tail())

#st.subheader(f"Dự báo giá tương lai của cổ phiếu: {selected_stocks}")
forcasting_fig = plot_plotly(m, forcast, trend=True, figsize=(1000, 1000))
forcasting_fig.layout.update(title_text=f"Đồ thị dự báo giá cổ phiếu {selected_stocks}")
#st.plotly_chart(forcasting_fig, use_container_width=False, width=800, height=800)
st.plotly_chart(forcasting_fig, width=1500, height=1200)

st.write("Phần dự báo")
forcasting_fig2 = m.plot_components(forcast)
#st.write(forcasting_fig2, use_container_width=False, width=800, height=800)
st.write(forcasting_fig2)


# Close the centered section
st.markdown('</div>', unsafe_allow_html=True)
