# -*- coding: UTF-8 -*-
"""Chris Groshong: PyRamen.

Python script for analyzing the analyze how well your business did on a per-product basis 
in order to better understand which products are doing well, which are doing poorly, 
and, ultimately, which products may need to be removed or changed.

Read the data in,performate data manipulations
01-count: the total quantity for each ramen type
02-revenue: the total revenue for each ramen type
03-cogs: the total cost of goods sold for each ramen type
04-profit: the total profit for each ramen type

loop through sales and perform analysis

Write out the contents of the report dictionary to a text file. 
The report should output each ramen type as the keys and
01-count, 02-revenue, 03-cogs, and 04-profit metrics as the values for every ramen.

"""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path("C:/Users/miscg/zzz/python-homework/PyRamenBank/Resources/menu_data.csv")
sales_filepath = Path("C:/Users/miscg/zzz/python-homework/PyRamenBank/Resources/sales_data.csv")

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
# Open the csv file as an object
with open(menu_filepath, "r") as csvfile_m:
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader_m = csv.reader(csvfile_m, delimiter=",")
    
    ## REVIEW THIS IS SKIPPING FIRST ROW OF DATA ##
    ## TEMP REMOVED FOR MVP2                     ##
    # Read the header row first (skip this step if there is no header)
    # csv_header = next(csvreader_m)
        
    # Read each row of data after the header
    for row in csvreader_m:
        menu = list(csvreader_m)

# @TODO: Read in the sales data into the sales list
with open(sales_filepath, "r") as csvfile_s:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader_s = csv.reader(csvfile_s, delimiter=",")
    
    ## REVIEW THIS IS SKIPPING FIRST ROW OF DATA ##
    ## TEMP REMOVED FOR MVP2                     ##
    # Read the header row first (skip this step if there is no header)
    # csv_header = next(csvreader_s)
        
    # Read each row of data after the header
    for row in csvreader_s:
        sales = list(csvreader_s)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object

    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    Line_Item_ID
    Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
for items in sales:
     row_count += 1
        
#validate for loop went through sales, should be 74124
row_count

    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)
