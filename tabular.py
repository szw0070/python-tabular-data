#! /usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def make_dataframe_all():
    dataframe = pd.read_csv("iris.csv") #uses panda to import csv as a dataframe
    x = dataframe.petal_length_cm #defines x using column of dataframe
    y = dataframe.sepal_length_cm #defines y using column of dataframe
    return dataframe

"""
regression = stats.linregress(x, y) #uses scipy to runs regression on x and y
slope = regression.slope #defines variable "slope"
intercept = regression.intercept #defines variable "intercept"
plt.scatter(x, y, label = 'Data') #creates scatterplot using x and y
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
#adds regression line to scatterplot
plt.xlabel("Petal length (cm)") #adds x label
plt.ylabel("Sepal length (cm)") #adds y label
plt.legend() #adds a legend
plt.savefig("petal_v_sepal_length_regress.png") #saves the figure as a png
quit()
"""


#Write code that runs linear regression/makes plot on each iris species separately.
#run code, end results is 3 plots are created

#separate dataframe into 3 dataframes based on species
#species = Iris_setosa Iris_virginica Iris_versicolor
#species is 5th column
#dataframe.species #accesses the species column



#run regression as normal



def test():
    list = [['test1', 1],['test2',2],['test1',5],['test2',6]]
    print(list)
    df = pd.DataFrame(list,columns = ['test','number'])
    print(df)
    df1 = df[df['test'] == 'test1']
    print(df1)


if __name__ == "__main__":
    def setosa():
#use function that makes dataframe with all data to make a variable called dataframe
        df = make_dataframe_all()
    #print(df)
#split dataframe into just setosa species data
        df2 = df[df['species'] == 'Iris_setosa']
    #print(df2)
        x = df2.petal_length_cm #defines x using column of dataframe
        y = df2.sepal_length_cm #defines y using column of dataframe
        regression = stats.linregress(x, y) #uses scipy to runs regression on x and y
        slope = regression.slope #defines variable "slope"
        intercept = regression.intercept #defines variable "intercept"
        plt.scatter(x, y, label = 'Iris setosa') #creates scatterplot using x and y
        plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    #adds regression line to scatterplot
        plt.xlabel("Petal length (cm)") #adds x label
        plt.ylabel("Sepal length (cm)") #adds y label
        #plt.legend() #adds a legend
        #plt.savefig("petal_v_sepal_length_regress_Setosa.png") #saves the figure as a png


    def virginica():
#use function that makes dataframe with all data to make a variable called dataframe
        df = make_dataframe_all()
    #print(df)
#split dataframe into just virginica species data
        df3 = df[df['species'] == 'Iris_virginica']
    #print(df2)
        x3 = df3.petal_length_cm #defines x using column of dataframe
        y3 = df3.sepal_length_cm #defines y using column of dataframe
        regression = stats.linregress(x3, y3) #uses scipy to runs regression on x and y
        slope = regression.slope #defines variable "slope"
        intercept = regression.intercept #defines variable "intercept"
        plt.scatter(x3, y3, label = 'Iris virginica') #creates scatterplot using x and y
        plt.plot(x3, slope * x3 + intercept, color = "orange", label = 'Fitted line')
    #adds regression line to scatterplot
        plt.xlabel("Petal length (cm)") #adds x label
        plt.ylabel("Sepal length (cm)") #adds y label
        #plt.legend() #adds a legend
        #plt.savefig("petal_v_sepal_length_regress_Virginica.png") #saves the figure as a png

    def versicolor():
#use function that makes dataframe with all data to make a variable called dataframe
        df = make_dataframe_all()
    #print(df)
#split dataframe into just verisicolor species data
        df4 = df[df['species'] == 'Iris_versicolor']
    #print(df2)
        x4 = df4.petal_length_cm #defines x using column of dataframe
        y4 = df4.sepal_length_cm #defines y using column of dataframe
        regression = stats.linregress(x4, y4) #uses scipy to runs regression on x and y
        slope = regression.slope #defines variable "slope"
        intercept = regression.intercept #defines variable "intercept"
        plt.scatter(x4, y4, label = 'Iris versicolor') #creates scatterplot using x and y
        plt.plot(x4, slope * x4 + intercept, color = "orange", label = 'Fitted line')
    #adds regression line to scatterplot
        plt.xlabel("Petal length (cm)") #adds x label
        plt.ylabel("Sepal length (cm)") #adds y label
        plt.legend() #adds a legend
        plt.savefig("petal_v_sepal_length_regress_bySpecies.png") #saves the figure as a png


setosa()
virginica()
versicolor()
#test()