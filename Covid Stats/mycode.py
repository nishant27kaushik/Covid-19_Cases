#Plotting Covid-19 Cases & Deaths using the Covid Lib
#Author Nishant Kaushik
#Date: 2020-07-15

from covid import Covid
from matplotlib import pyplot as plt 


covid = Covid()

active_cases = covid.get_total_active_cases()
total_deaths = covid.get_total_deaths()
confirmed_cases = covid.get_total_confirmed_cases()
mortality_rate = (total_deaths/confirmed_cases) * 100

print("Total Active Cases of Corona Virus: " + str(covid.get_total_active_cases()))
print("Total Confirmed Deaths: " + str(covid.get_total_deaths()))
print("Total Confirmed Cases: "+ str(covid.get_total_confirmed_cases()))
print("Mortality Rate: "+ str(int(mortality_rate)) +"%")

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

x_label = ['Active_Cases','Confirmed_Deaths','Confirmed_Cases']
y_label = [active_cases,total_deaths,confirmed_cases]

ax.set_ylabel ("in Millions")
plt.bar(x_label,y_label, color = ['blue','red','yellow'])


plt.show()

plt.bar(len(y_label),total_deaths, color = 'red')
plt.bar(len(y_label),active_cases,bottom = total_deaths, color = 'yellow')
plt.bar(len(y_label),confirmed_cases,bottom = active_cases, color = 'blue')

plt.legend(x_label,loc=10)
plt.show()