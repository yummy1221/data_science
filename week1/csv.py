#!/usr/bin/python3

## Sample for reading csv file
import csv

with open('course1_downloads/mpg.csv') as csvfile:
	mpg = list(csv.DictReader(csvfile)) # mpg is a list of dictionary


## time series data analysis
dtnow = datetime.datetime.fromtimestamp(time.time())
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second

today = datetime.date.today()
delta = datetime.timedelta(days = 100)
today - delta

## map(function, iterable, ...)
# python functional programming
store1 = [10, 11, 12.34, 2.34]
store2 = [9, 11.1, 12.34, 2.01]
cheapest = map(min, store1, store2)
# cheapest is a map object

## lambda function: python way of creating an anonymous function
# only single line, limited than normal functions
my_func = lambda a,b,c : a + b
my_func(2,9)

## list comprehensions
# compact/condense format and fast as well
lst1 = []
for number in range(0, 100):
	if number % 2 == 0:
		lst1.append(number)
lst2 = [number for number in range(0, 100) if number % 2 == 0]

times_tables = [i * j for i in range(10) for j in range(10)]


## package Numpy
# arrays and matrices

# sudo apt-get install python3-pip
# sudo pip3 install numpy
