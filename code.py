from os import stat
from typing import Counter
import pandas as pd 
import plotly.figure_factory as  ff
import csv 
import statistics
import random 
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].to_list()

mean = statistics.mean(data)
stdv_deviation = statistics.stdev(data)
print("Mean of Population:-", mean)
print("Standard Devation Of Population :-", stdv_deviation)

def random_set_of_mean(counter) :
    dataset=[]
    for i in range (0,counter) :
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    
    mean =statistics.mean(dataset)
    return(mean)

mean_list = []
for i in range (0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

smean = statistics.mean(mean_list)
se=  statistics.stdev(mean_list)
print("Mean of Sampling Distribution :-", smean)
print("Standard devation of Sample Distribution:-",se)

first_std_deviation_start, first_std_deviation_end = smean-se, smean+se
second_std_deviation_start, second_std_deviation_end = smean-(2*se), smean+(2*se)
third_std_deviation_start, third_std_deviation_end = smean-(3*se), smean+(3*se)

sdf = pd .read_csv("data1.csv")
sdata = sdf["Math_score"].tolist()

mean1 = statistics.mean(sdata)



print("Mean 1 :-",mean1)


z_score =(mean1-smean)/se
print(z_score)


# fig = ff.create_distplot([mean_list],["MathScore"],show_hist= False)
# fig.add_trace(go.Scatter(x=[smean, smean], y=[0, 0.17], mode="lines", name="MEAN"))
# fig.add_trace(go.Scatter(x=[mean1, mean1], y=[0, 0.17], mode="lines", name="MEAN"))


 
 
# fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 Start"))
# fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
# fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
# fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
# fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

# fig.show()


