"""Chris Groshong: PyBank.

Python script for analyzing the financial records of your company. You will be provided with a financial dataset in this file: budget_data.csv. 
This dataset is composed of two columns, Date and Profit/Losses.

This script that analyzes the records to calculate each of the following:
> The total number of months included in the dataset.
> The net total amount of Profit/Losses over the entire period.
> The average of the changes in Profit/Losses over the entire period.
> The greatest increase in profits (date and amount) over the entire period.
> The greatest decrease in losses (date and amount) over the entire period.

"""

# Import the pathlib and csv library
from pathlib import Path
import csv
import pandas as pd

# Set the file path
csvpath = Path("C:/Users/miscg/zzz/UofM-VIRT-FIN-PT-03-2022-U-LOL/02-Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv")

#create an analysis dataframe for performing calculations
analysis_dataframe = pd.read_csv(csvpath)



##################
## PRINT HEADER ##
##################
print("Financial Analysis")
print("----------------------------")

##################
## TOTAL MONTHS ##
##################
#total number of months in dataset
months_total = len(analysis_dataframe)
print(f"Total Months:  {months_total}")

###########
## TOTAL ##
###########
#The net total amount of Profit/Losses over the entire period.
net_total = analysis_dataframe['Profit/Losses'].sum()
print(f"Net total amount of Profit/Losses over the entire period: $ {net_total:,.2f}")


####################
## AVERAGE CHANGE ##
####################
#The average of the changes in Profit/Losses over the entire period.
analysis_mean = analysis_dataframe['Profit/Losses'].mean()
print(f"Average of the changes in Profit/Losses over the entire period: $ {analysis_mean:,.2f}")

##################################
## GREATEST INCREASE IN PROFITS ##
##################################
#The greatest increase in profits (date and amount) over the entire period.
greatest_increase = analysis_dataframe['Profit/Losses'].max()

# find the location of the greatest increase in the dataframe
location_increase = analysis_dataframe.loc[analysis_dataframe['Profit/Losses'] == greatest_increase]

#set variables for greatest inscrease in dataframe for date and profit-losses at location
location_increase_date = location_increase.iat[0,0]
location_increase_profit_losses = location_increase.iat[0,1]

#print out results for greatest increase
print(f"Greatest increase in profits was on : {location_increase_date} for: $ {location_increase_profit_losses:,.2f}")

##################################
## GREATEST DECREASE IN PROFITS ##
##################################
#The greatest decrease in losses (date and amount) over the entire period.
greatest_decrease = analysis_dataframe['Profit/Losses'].min()

# find the location of the greatest decrease in the dataframe
location_decrease = analysis_dataframe.loc[analysis_dataframe['Profit/Losses'] == greatest_decrease]

#set variables for greatest decrease in dataframe for date and profit-losses at location
location_decrease_date = location_decrease.iat[0,0]
location_decrease_profit_losses = location_decrease.iat[0,1]

#print out results for greatest decrease
print(f"Greatest decrease in losses was on : {location_decrease_date} for: $ {location_decrease_profit_losses:,.2f}")

######################
## EXPORT TEXT FILE ##
######################
f = open("myfile.txt", "w")
f.write(f"Financial Analysis\n")
f.write(f"----------------------------\n")
f.write(f"Total Months:  {str(months_total)}\n")
f.write(f"Net total amount of Profit/Losses over the entire period: $ {net_total:,.2f}\n")
f.write(f"Average of the changes in Profit/Losses over the entire period: $ {analysis_mean:,.2f}\n")
f.write(f"Greatest increase in profits was on : {location_increase_date} for: $ {location_increase_profit_losses:,.2f}\n")
f.write(f"Greatest decrease in losses was on : {location_decrease_date} for: $ {location_decrease_profit_losses:,.2f}\n")
f.close()