import pandas as pd
import datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt

BASED_URL="https://www.24h.com.vn/gia-vang-hom-nay-c425.html?ngaythang="

START_DATE = date(2024,1,1)
TODAY = date.today()

target_day = START_DATE
text = "Ngày,Giá mua,Giá bán\n"
while target_day <= TODAY:
    URL = BASED_URL + target_day.strftime("%Y-%m-%d")
    tables = pd.read_html(URL)
    gold_table = tables[2]
    text += f"{target_day},{str(gold_table[1][0]).split()[0].replace(",","")},{str(gold_table[2][0]).split()[0].replace(",","")}\n"
    target_day = (target_day + timedelta(days=1))

file_name = "temp.csv"
with open(file_name,"w") as file:
    file.write(text)

file.close()

df = pd.read_csv(file_name)

# Plot the data
plt.figure(figsize=(12, 10))
plt.title("Gold Price Chart - By HoanTran")
plt.plot(df['Ngày'], df['Giá mua'], label='Giá mua')
plt.plot(df['Ngày'], df['Giá bán'], label='Giá bán')
plt.xlabel('Ngày')
plt.ylabel('Giá')

plt.title(f'Giá vàng SJC từ {START_DATE}')
plt.legend()
plt.grid(False)
plt.show()



