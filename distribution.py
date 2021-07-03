#Importing neccessary modules
import random as r
import pandas as pd
import statistics as st
import plotly.figure_factory as ff

#Reading data from csv file
df   = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

#finding and printing mean
mean  = st.mean(data)
print("mean: ", mean)

#Plotting a graph
def graph(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["Reading time"], show_hist=False)
    fig.show()

#Finding the mean of the 30 sample data
def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex= r.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

#Repeating the above process 100 times
def setup():
    meanList = []
    for i in range(0,100):
        setOfMeans= randomSetOfMean(10)
        meanList.append(setOfMeans)
    graph(meanList)
    print("sampling mean: ", st.mean(meanList))

#Calling the function
setup()



