# Data Analysis - PMF & CDF
In this project, I have 2 types of data (```wine.txt``` and ```Book2.csv```). I have explored each one of them and applied statistical analysis as it's explained in below sections. The goal of this project is to understand the given data and learn how to utilize it for data analysis.


<br>

## Getting Started
This project is divided into two major parts according to the two different data files. But before we dig in, it's important to point out that there are required essential library packages that the project will not work without it. These packages are:

### Dependencies
- [ThinkStats2 by Prof. Allen B. Downey](https://github.com/AllenDowney/ThinkStats2). <br>
   _Note: The link's repository is downloadable as ThinkStats2 package. You can find also his book as a guideline reference._
- [Matplotlib](https://github.com/matplotlib/matplotlib)
- [NumPy](https://github.com/numpy/numpy)
- [Pandas](https://github.com/pandas-dev/pandas/)
- [SciPy](https://github.com/scipy/scipy)


<br>

## Usage
At the bottom of the Python file, there are the calling commands sorted chronologically regarding each functon respectively, but they are commented. You may run whichever function/method you would like to witness by uncommenting them.

### Part [ 1 ]
In this part, I used the data in the file ```wine.txt``` which is monthly sales of Australian wine by category, in thousands of litres, from January 1980 until July 1995. The categories are fortified white, dry white, sweet white, red, rose, and sparkling ecnoded by ```fortw```, ```dryw```, ```sweetw```, ```red```, ```rose```, ```spark``` respectively. The overall goal is simply to examine sales of Australian wine over 15 years periof from 1980-1995 and distribution of variables in this data.

<br>

#### Methods
- **plotHistogram( )** <br>
This method plots the histogram of total sales of 6 different categories of wine from 1980-1995.

- **plotCategory( )** <br>
This method takes name of a category, start year and end year as arguments and plot the histogram of yearly total sales of wine for this category.

- **findOutlier( )** <br>
This method takes the created histogram in **plotCategory( )** as an argument and return the largest and smallest value for specific category.

- **mean( )** <br>
This method finds the mean of specific category.

- **variance( )** <br>
This method takes a category as an argument and find variance and standard deviation for this category.


<br>

##
### Part [ 2 ]
In this part, I used the data in the file ```Book2.csv```. The file contains 25 parts and 10 of them are non-defective. The overall goal here is simply to understand Probability Mass Function (PMF) and Cumulative Distribution Function (CDF).

<br>

#### Methods
- **generate( )** <br>
This method generates 1000 random numbers between 0 and 1. Then plot these numbers by using PMF AND CDF.

- **PMF( )** <br>
This method takes a list of integers (```[1,2,3,4,5,6]```) as an argument and randomly choose a number until 4 comes up. Then, finding the probability mass function and plotting the histogram.

- **CDF( )** <br>
This method finds the cumulative distribution function of the previous method and shows it graphically.

- **findDefective( )** <br>
This method which takes the data from ```Book2.csv``` file and gets randomly 3 parts from this file until all 3 parts are defective and all defective parts have part id greater than 10. Then, finds both the probability mass function and cumulative distribution function and plots the histogram for PMF and graph for CDF. Finally, it finds the percentiles and percentile ranks for CDF.


<br>

## Screenshots
Below screeshot samples of PMF and CDF plots examples:


<br>
<p>
   <em>PMF Example</em>
   <br><br>
   <img style="max-width: 100%;height: 450px;" src="/screenshots/pmf.png" alt>
</p>



<br>

<p>
   <em>CDF Example</em>
   <br><br>
   <img style="max-width: 100%;height: 450px;" src="/screenshots/cdf.png" alt>
</p>
  
  
  
  
  
