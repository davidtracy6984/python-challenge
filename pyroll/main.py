# Import libraries
import os
import csv
       
# open the file and EXCLUDE THE HEADER after printing it so I can see it
csvpath = os.path.join('resources', 'pyproll.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) # Read and print the Header
    
    cval = 0
    dict = {} 
    
    for row in csvreader:  
        cval +=1
        if str(row[2]) not in dict:
            dict[row[2]]=1
        else:
            dict[row[2]]+=1 

# print the result to the terminal
              
print('Electin Results')   
print('--------------------------------')
print('Total Votes: ' + str(cval))
print('--------------------------------')
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
        print(cand + ': '+ str(cpercent)[:6] +'%  '+ str(cval))
print('Winner: ' + str(maxname) )

# Write the results to a csv file

output_path = os.path.join('analysis', 'results.txt')     
with open(output_path, 'w') as csvfile:
                csvwriter = csv.writer(csvfile, delimiter=',')
                csvwriter.writerow(['Election Results'])   
                csvwriter.writerow(['--------------------------------'])  
                csvwriter.writerow(['Total Votes: ' + str(cval)]) 
                csvwriter.writerow(['--------------------------------'])  
                for key, value in dict.items():
                    cand = ''
                    cvalue = 0
                    cpercent =0
                    cand = key
                    cvalue = value
                    cpercent = (cvalue/cval *100)
                    csvwriter.writerow(str(cand) + ':'+ str(cpercent)[:6] +'%' + str(cval))
                  
                csvwriter.writerow(['Winner: ' + maxname])
              