import csv
from datetime import datetime

import matplotlib.pyplot as plt

"""将代码默认字体改为思源黑体，解决matplotlib对中文支持的问题"""
plt.rcParams["font.family"] = "Source Han Sans SC"

plt.style.use("Solarize_Light2")

filename = 'BOOK Python-Crash-Course\P2 data visualization\sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # 从文件中获取日期、最高温度和最低温度
    dates, highs, lows= [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# 根据最低温度和最高温度绘制图形
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
ax.set_title("2018年每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("温度(F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
