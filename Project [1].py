# Khaled AlSaleh 212402570
# Anas Abdrabbuh 212462285


# Importing the needed modules to use its functions:
from random import *
import thinkstats2
import thinkplot
import pandas


class Part1(object):
    def __init__(self,name):
        if name == 'fortw':
            self.name = 1
        if name == 'dryw':
            self.name = 2
        if name == 'sweetw':
            self.name = 3
        if name == 'red':
            self.name = 4
        if name == 'rose':
            self.name = 5
        if name == 'spark':
            self.name = 6

    def plotHistogram(self,x):
        '''
        Write a code which plots the histogram of total sales
        of 6 different categories of wine from 1980-1995.
        (You can use plot function from thinkstat2 library to plot the histogram)
        '''
        hist = thinkstats2.Hist(x)
        thinkplot.Hist(hist)
        thinkplot.Show(xlabel='Categories', ylabel='Sales')

    def plotCategory(self, start, end):
        '''
        Write a code which takes name of a category,
        start year and end year as arguments and plot the histogram
        of yearly total sales of wine for this category.
        (Sales in Data are monthly , you may convert them to yearly)
        '''
        global index2, index1, total
        name = self.name
        DatetoIndex = [(1980,1),(1981,2),(1982,3),(1983,4),(1984,5),(1985,6),(1986,7),(1987,8),(1988,9),(1989,10),(1990,11),(1991,12),(1992,13),(1993,14),(1994,15),(1995,16)]
        PlotCategory = {}
        for x,y in DatetoIndex:
            if x == start:
                index1 = y
        for x,y in DatetoIndex:
            if x == end:
                index2 = y
        Counter = 1
        for i in AllWines[name][index1:index2]:
            PlotCategory[Counter] = i
            Counter += 1
        self.plotHistogram(PlotCategory)
        return PlotCategory

    def findOutlier(self, CategoryHistogram):
        '''
        which takes histogram that you create in plotCategory() method
        as an argument and return the largest and smallest value for specific category.
        '''
        print("The largest value for this category's histogram is: %d" % max(CategoryHistogram.values()))
        print("The smallest value for this category's histogram is: %d" % min(CategoryHistogram.values()))

    def mean(self):
        '''
        which finds the mean of specific category.
        (Also do not use any built-in function to find mean for the dataset).
        '''
        name = self.name
        Mean = TotalSales[name] / float(Length-1)
        print("The Mean is:", Mean)
        return Mean

    def variance(self):
        '''
        which takes a category as an argument
        and finds variance and standard deviation for this category.
        (Do not use any built-in function to find variance and standard deviation.
        To implement variance you can use formula in your book page 23 below
        and standard deviation is simply square root of variance)
        '''
        Data = [int(i) for i in Raw[self.name]]
        Mean = self.mean()
        Deviations = [(x - Mean) ** 2 for x in Data]
        Variance = sum(Deviations) / len(Data)
        print("The Variance is: ", Variance)
        print("The Standard Deviation is: ", Variance ** 0.5)





class Part2(object):
    def generate(self):
        '''
        which generates 1000 random numbers between 0 and 1.
        Then plot these numbers by using PMF AND CDF.
        (Comments their outputs and put your comments in your report with plots.)
        '''
        Randomness = {}
        for i in range(1000):
            random_number = uniform(0,1)
            Randomness[i] = random_number

        # PMF Plotting
        pmf = thinkstats2.Hist(Randomness)
        thinkplot.Hist(pmf)
        thinkplot.Show()

        # CDF Plotting
        cdf = thinkstats2.Cdf(Randomness)
        thinkplot.Cdf(cdf)
        thinkplot.Show()

    def PMF(self, Integers):
        '''
        that get a list of integers ([1,2,3,4,5,6]) and randomly choose a number until 4 comes up.
        X denote the number of random selection.
        Find the probability mass function of X and draw the histogram.
        '''
        Probabilities = { Integer : 0 for Integer in Integers }
        while True:
            X = choice(Integers)
            if X == 4:
                Probabilities[4] += 1
                break
            else:
                Probabilities[X] += 1

        pmf = thinkstats2.Hist(Probabilities)
        thinkplot.Hist(pmf)
        thinkplot.Show(yscale='linear')

    def CDF(self, Integers):
        '''
        which finds the cumulative distribution
        of the previous question and show it graphically.
        '''
        Probabilities = {Integer: 0 for Integer in Integers}
        while True:
            X = choice(Integers)
            if X == 4:
                Probabilities[4] += 1
                break
            else:
                Probabilities[X] += 1

        cdf = thinkstats2.Cdf(Probabilities)
        thinkplot.Cdf(cdf)
        thinkplot.Show()

    def findDefective(self):
        '''
        which takes a file and get randomly 3 parts from this file
        until all 3 parts are defective and all defective parts have part id greater than 10.
        Let X denote the number of random selections.
        Find both the probability mass function and cumulative distribution of X
        and draw the histogram for PMF and graph for CDF.
        For CDF, find percentiles and percentile ranks
        '''
        df = pandas.read_csv('Book2.csv')
        Probabilities = {index+1: 0 for index in range(len(df))}
        counter = 0
        while True:
            counter += 1
            X = sample(range(0, (len(df)-1)), 3)
            if df.loc[X[0]]['PART'] == df.loc[X[1]]['PART'] == df.loc[X[2]]['PART'] == 'D' and df.loc[X[0]]['PART_ID'] & df.loc[X[1]]['PART_ID'] & df.loc[X[2]]['PART_ID'] >= 10:
                for x in X:
                    Probabilities[x+1] += 1
                break
            else:
                for x in X:
                    Probabilities[x+1] += 1

        # Plotting PMF
        pmf = thinkstats2.Hist(Probabilities)
        thinkplot.Hist(pmf)
        thinkplot.Show(yscale='linear')

        # Plotting CDF
        cdf = thinkstats2.Cdf(Probabilities)
        thinkplot.Cdf(cdf)
        thinkplot.Show()

        print('The Percentiles are:', cdf.Percentiles(X))
        print('The Percentile Ranks are:', cdf.PercentileRanks(X))


### =============================================================================================================== ###
#                                 Some needed operations and modifications
### =============================================================================================================== ###


file = open('wine.txt', 'r') # Importing the file data
AllWines={} # Creating a dictionary to match all the columns' variables with its category key
Flag = True # A flag for an if condition

## This loop summarizes many tasks:
# Filtering the text line from the additional characters like: \t
# Adding the values to its category to the dictionary
for line in file:
    Filtered = line.strip().split('\t')
    if Flag:
        for i in range(1,len(Filtered)):
            AllWines.setdefault((i),[])
        Flag = False
    for i in range(1,len(Filtered)):
        AllWines[i].append(Filtered[i])


Length = len(AllWines[1]) # Keeping in a variable the length of the sales monthly

CategorySum = [] # Creating a list to have tht total sum for every category
for each in AllWines:
    list_of_wines = AllWines[each] # Adding the keys and values of every category to a list
    # Converting the elements to integers since they are imported from a text file as strings
    # sum them up then add them to the list after getting rid of the first element which is the category
    CategorySum.append(sum(map(lambda x: int(x),list_of_wines[1:])))

TotalSales = {} # Linking back every total category sales to its category
for i in range(len(CategorySum)):
    TotalSales[i+1] = CategorySum[i]

for i in AllWines: # Pop the unneeded first line which is a text
    ToPop = AllWines.get(i).pop(0)
Raw = AllWines.copy() # Copying the raw elements

#Yearly = []
Counter = 1 # To go through the dictionary keys
for a in AllWines:
    Yearly = []
    for j in AllWines[a]:
        Yearly.append(int(j))
    AllWines[a]=Yearly
    l = AllWines.get(Counter) # Taking the values of every category
    for i in range(len(l)): # Looping through every element to convert it to integer
        l[i] = int(l[i])
    # Summing every 12 element because every element represented in months
    # So every 12 months will give us 1 year, and so on till 15 years and 7 months in total

for x in AllWines:
    Sum_list = []
    for y in range(0, len(AllWines[x]), 12):

        Summed = sum(AllWines[x][y:y+12])
        Sum_list.append(Summed)
    AllWines[x] = Sum_list


"""
### =============================================================================================================== ###
#                                              The Project Answers
### =============================================================================================================== ###
#
#
# ***** The First Answer of Part1 *****
# part = Part1('red')
# part.plotHistogram(TotalSales)
#
#
# ***** The Second Answer of Part1 *****
# part = Part1('red')
# part.plotCategory(1980,1995)
#
#
# ***** The Third Answer of Part1 *****
# part = Part1('red')
# part.findOutlier(part.plotCategory(1980,1995))
#
#
# ***** The Fourth Answer of Part1 *****
# part = Part1('rose')
# part.mean()
#
#
# ***** The Fifth Answer of Part1 *****
# part = Part1('rose')
# part.variance()
#
#
### =============================================================================================================== ###
# ***** The First Answer of Part2 *****
# Part2().generate()
#
#
# ***** The Second Answer of Part2 *****
# Part2().PMF([1,2,3,4,5,6])
#
#
# ***** The Third Answer of Part2 *****
# Part2().CDF([1,2,3,4,5,6])
#
#
# ***** The Fourth Answer of Part2 *****
# Part2().findDefective()
#
#
### =============================================================================================================== ###
"""

