import os
import csv

# Path defined
csvpath = os.path.join('','PyBank\Resources', 'budget_data.csv')

#File opened and header read, creates file handler
with open(csvpath, newline ='') as fh_budget_data:
    csvreader = csv.reader(fh_budget_data, delimiter=',')
    csv_header = next(csvreader)
#    print("Header is" + str(csv_header))

#   Instantiating variables, readig the first data and, preparing to start iteration
    rows = next(csvreader)
    Total_Months = 1
    Sum_Profit_Loss = int((rows[1]))
    Prior_month_Profit_Loss = int((rows[1]))
    Difference_in_Profit_Loss = Prior_month_Profit_Loss - int(rows[1])
    Prior_month_Profit_Loss = int(rows[1])
    sum_Difference_in_Profit_Loss = Difference_in_Profit_Loss
    Greatest_increase_Profit_Loss = Difference_in_Profit_Loss
    Greatest_increase_month_num = rows[0]
    Greatest_decrease_Profit_Loss = Difference_in_Profit_Loss
    Greatest_decrease_month_num = rows[0]
#    print(rows[0], rows[1], year, month_num, Difference_in_Profit_Loss)


#starting iterating through all records one by one from the file
    for rows in csvreader:
        Total_Months = Total_Months + 1
        Sum_Profit_Loss = Sum_Profit_Loss + int(rows[1])
        Difference_in_Profit_Loss = int(rows[1]) - Prior_month_Profit_Loss
        sum_Difference_in_Profit_Loss = sum_Difference_in_Profit_Loss + Difference_in_Profit_Loss
        Prior_month_Profit_Loss = int(rows[1])
#        print(rows[0], rows[1], year, month_num, Difference_in_Profit_Loss)

# calculation for gratest increase
        if Difference_in_Profit_Loss > Greatest_increase_Profit_Loss:
            Greatest_increase_Profit_Loss = Difference_in_Profit_Loss
            Greatest_increase_month_num = rows[0]

# calculation for gratest decrease    
        if Difference_in_Profit_Loss < Greatest_decrease_Profit_Loss:
            Greatest_decrease_Profit_Loss = Difference_in_Profit_Loss
            Greatest_decrease_month_num = rows[0]


# printing results to screen
print("---------------------------------------------------")
print("Financial Analysis")
print("---------------------------------------------------")
print("Total Months: " +str(Total_Months))
print("Total: $" + str(Sum_Profit_Loss))
#print(sum_Difference_in_Profit_Loss)
print("Average Change: $" + str("{:1.2f}".format((sum_Difference_in_Profit_Loss/(Total_Months-1)))))
print("Greatest Increase in Profits: " + str(Greatest_increase_month_num) +"  ($"+ str(Greatest_increase_Profit_Loss)+")")
#print ("Greatest_increase_month_num - " +str(Greatest_increase_month_num))
print("Greatest Decrease in Profits: " + str(Greatest_decrease_month_num) +"  ($" +str(Greatest_decrease_Profit_Loss)+")")
#print ("Greatest_decrease_month_num - " +str(Greatest_decrease_month_num))
print("---------------------------------------------------")

# opening the file to write the results
output_path = os.path.join("", "PyBank\Resources", "Financial_Analysis_Results.csv")
    # Open the file using to write the results
with open(output_path, 'w', newline='') as fh_Financial_Analysis_results:


# printing results to screen and Initialize csv.writer
    csvwriter = csv.writer(fh_Financial_Analysis_results)
    csvwriter.writerow(["---------------------------------------------------"])
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------------------------------"])
    csvwriter.writerow(["Total Months: " +str(Total_Months)])
    csvwriter.writerow(["Total: $" + str(Sum_Profit_Loss)])
    csvwriter.writerow(["Average Change: $" + str("{:1.2f}".format((sum_Difference_in_Profit_Loss/(Total_Months-1))))])
    csvwriter.writerow(["Greatest Increase in Profits: " + str(Greatest_increase_month_num) +"  ($"+ str(Greatest_increase_Profit_Loss)+")"])
    csvwriter.writerow(["Greatest Decrease in Profits: " + str(Greatest_decrease_month_num) +"  ($" +str(Greatest_decrease_Profit_Loss)+")"])
    csvwriter.writerow(["---------------------------------------------------"])
