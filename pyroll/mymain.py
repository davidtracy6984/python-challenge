# Import libraries
import os
import csv
       
# open the file and EXCLUDE THE HEADER after printing it so I can see it
csvpath = os.path.join('resources', 'pyproll.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # Read and print the Header
    
    
    #Get the total number of votes:
    #count the instances by candidate and put them into a dictionary or list
    #Get the first candidate name from the dictionary or list and count the instances for each name and store it 
    #Calculate the percent of vote
    #write the name and percent 
    candidate_name = ''
    cval = 0
    dict = {} 
    
    for row in csvreader:  
        cval +=1
        if str(row[2]) not in dict:
            dict[row[2]]=1
        else:
            dict[row[2]]+=1 

         
              
print('Financial Analysis')   
print('--------------------------------')
print('Total Votes: ' + str(cval))
maxval = 1
for key, value in dict.items():
        cand = ''
        cvalue = 0
        cpercent =0
        cand = key
        cvalue = value
        cpercent = (cvalue/cval *100)
        
        if value >maxval:
           maxval = value
           maxname = cand
        else:
            maxval = value
        print(cand + ': '+ str(cpercent)[:6] +'%  '+ str(cvalue))
        
        
print('Winner: ' + str(maxname) )

output_path = os.path.join('analysis', 'results.txt')     
with open(output_path, 'w') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow(['Financial Analysis'])   
                csvwriter.writerow(['--------------------------------'])  
                csvwriter.writerow(['Total Votes: ' + str(cval)]) 
                csvwriter.writerow(['Total: ' ])  
                csvwriter.writerow(['Average Change: ' ])  
                csvwriter.writerow(['Greatest Increase in Profits: ' ])  
                csvwriter.writerow(['Winner: ' +str(maxname)])  
