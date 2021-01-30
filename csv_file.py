import csv
import matplotlib.pyplot as plt
from datetime import datetime

file = 'CSV files/death_valley_2018_simple.csv'
with open(file) as f:
    reader = csv.reader(f)
    header = next(reader)
    for index, column in enumerate(header):
        print(index, column)
    Max_Temp, Min_Temp, dt = [], [], []
    for row in reader:
        dts = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            Max = int(row[4])
            Min = int(row[5])
        except ValueError:
            print(f'Missing data for {dt}')
        else:
            dt.append(dts)
            Max_Temp.append(Max)
            Min_Temp.append(Min)
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.plot(dt, Max_Temp, linewidth = 1, c = (0.9, 0.1, 0.2), alpha = 1)
plt.plot(dt, Min_Temp, linewidth = 1, c = (0.2, 0.1, 0.9), alpha = 1)
plt.title('Daily High Temperatures', fontsize = 24)
plt.fill_between(dt, Min_Temp, Max_Temp, facecolor = (0.2, 0.5, 0.3), alpha = 0.5)
plt.xlabel('', fontsize = 14)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize = 14)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.show()
# plt.savefig('max-min temp.jpeg', bbox_inches = 'tight')

