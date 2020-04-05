# Import libraries
import os
import csv


smallval = 0
bigval = 0
bigdate = ''
smalldate = ''
maxchange = 0
minchange = 0


# open the file and EXCLUDE THE HEADER after printing it so I can see it
csvpath = os.path.join('resources', 'bank.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # Read and print the Header
    mycount = 0 # Set a counter for the number of months/records not including the header
    myvalue = 0
    avgchange = 0
    firstrow = next(csvreader)
    begchange = int(firstrow[1])
    minchange = int(firstrow[1])
    
    
    
    for row in csvreader:  # Read and print each row of data after the header
        mycount = mycount + 1 # Set a counter for the number of months/records not including the header

        myvalue += int(row[1]) # Add up the values across the entire data set

        runchange = int(row[1]) - begchange # first time this should be 0
       
        avgchange = avgchange + runchange
               
       

        if runchange  > maxchange:
            maxchange =  runchange
            bigdate = str(row[0])
           
        if runchange < minchange:
            minchange = runchange
            smalldate = str(row[0])
        
        begchange = int(row[1]) #reset to the current value for the next loop   

output_path = os.path.join('analysis', 'results.txt')     
with open(output_path, 'w') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow(['Financial Analysis'])   
                csvwriter.writerow(['--------------------------------'])  
                csvwriter.writerow(['Total Months: ' + str(mycount)]) 
                csvwriter.writerow(['Total: ' + str(myvalue)])  
                csvwriter.writerow(['Average Change: ' + str(avgchange)])  
                csvwriter.writerow(['Greatest Increase in Profits: ' + str(bigdate) + ' ('+ str(maxchange) + ')'])  
                csvwriter.writerow(['Greatest Decrease in Profits: ' + str(smalldate) + ' ('+ str(minchange) + ')'])                  
                
avgchange = (avgchange/85)
avgchange = round(avgchange, 2)     
print('Financial Analysis')   
print('--------------------------------')
print('Total Months: ' + str(mycount))
print('Total: ' + str(myvalue))
print('Average Change: ' + str(avgchange))
print('Greatest Increase in Profits: ' + str(bigdate) + ' ('+ str(maxchange) + ')')
print('Greatest Decrease in Profits: ' + str(smalldate) + ' ('+ str(minchange) + ')')

            

