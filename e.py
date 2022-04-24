import csv
import random
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df=pd.read_csv('s.csv')
data=df['math score'].tolist()
mean=statistics.mean(data)
standardDeviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)
print(mean)
print(median)
print(mode)
print(standardDeviation)
first_standard_deviation_start,first_standard_deviation_end=mean-standardDeviation,mean+standardDeviation
second_standard_deviation_start,second_standard_deviation_end=mean-(2*standardDeviation),mean+(2*standardDeviation)
third_standard_deviation_start,third_standard_deviation_end=mean-(3*standardDeviation),mean+(3*standardDeviation)

fig=ff.create_distplot([data],["result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='mean'))
fig.add_trace(go.Scatter(x=[first_standard_deviation_start,first_standard_deviation_start],y=[0,0.17],mode='lines',name='standardDeviation1'))
fig.add_trace(go.Scatter(x=[first_standard_deviation_end,first_standard_deviation_end],y=[0,0.17],mode='lines',name='standardDeviation1'))
fig.add_trace(go.Scatter(x=[second_standard_deviation_start,second_standard_deviation_start],y=[0,0.17],mode='lines',name='standardDeviation2'))
fig.add_trace(go.Scatter(x=[second_standard_deviation_end,second_standard_deviation_end],y=[0,0.17],mode='lines',name='standardDeviation2'))

fig.show()
list_of_data_within_1_standardDeviation=[result for result in data if result>first_standard_deviation_start and result<first_standard_deviation_end]
list_of_data_within_2_standardDeviation=[result for result in data if result>second_standard_deviation_start and result<second_standard_deviation_end]
list_of_data_within_3_standardDeviation=[result for result in data if result>second_standard_deviation_start and result<third_standard_deviation_end]

print(len(list_of_data_within_1_standardDeviation)*100/len(data))
print(len(list_of_data_within_2_standardDeviation)*100/len(data))
print(len(list_of_data_within_3_standardDeviation)*100/len(data))
