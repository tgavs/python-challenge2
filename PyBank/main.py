# PyBank Solution

#import libraries

import os
import csv

# define lists to build

months=[]
profit_losses=[]
index=[]
shift=[] # moves the profit_losses data from the position n to the n+1
change=[] # to calculate the change between profit_losses and shifht

#control variable

i=0

# data path to read
rd_path= os.path.join('Resources','budget_data.csv')

#read data

with open(rd_path) as raw_data:

    reader=csv.reader(raw_data)

    header=next(reader)


# build data frame
    for row in reader:

        profit_losses.append(float(row[1]))
        months.append(row[0])
        index.append(i)    
        i+=1


# build the shifted profit column to calculate changes
# it will pass the element n to the possition n+1
# thats why the shift list starts in cero
    shift.append(0)

    for j in range(0,len(profit_losses)-1):

        shift.append(profit_losses[j])  

# calculates the change for each profit row vs the previous one
    for i in index:

        change.append(profit_losses[i]-shift[i])

#the first row is set to cero because the first element has no previous element to compare
    change[0]=0

      
#calculate statistics

    totalmonths= len(months)
    totalp_l = sum(profit_losses)
    av_change= sum(change)/(len(change)-1) #the average should not take into account the first element
    maxlist_value= max(change)
    maxlist_date=months[change.index(max(change))]
    minlist_value=min(change)
    minlist_date=months[change.index(min(change))]

#Print in terminal


    print('Financial Analysis')

    print('-------------------------------------')

    print(f'Total Months:  {totalmonths}')
    print(f'Total:  ${totalp_l:,.2f}')
    print(f'Average Change:  ${av_change:,.2f}')
    print(f'Greatest Increase in Profits: {maxlist_date }  ${maxlist_value:,.2f}')
    print(f'Greatest Decrease in Profits: {minlist_date }  ${minlist_value:,.2f}')


#Print the report in .txt

    report=open('PyBankReport.txt','w')

    report.write('Financial Analysis\n')

    report.write('-------------------------------------\n')

    report.write(f'Total Months:  {totalmonths}\n')
    report.write(f'Total:  ${totalp_l:,.2f}\n')
    report.write(f'Average Change:  ${av_change:,.2f}\n')
    report.write(f'Greatest Increase in Profits: {maxlist_date }  ${maxlist_value:,.2f}\n')
    report.write(f'Greatest Decrease in Profits: {minlist_date }  ${minlist_value:,.2f}\n')
  
    report.close()







