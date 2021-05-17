'''
This program will open a cvs file and read the numbers of population in the 
United States. The numbers will be assigned to a string and turned into integers.
Next, it will iterate through the numbers, finding the percent increase
in the consecutive years. It will keep track of the minimum and the maximum increases.
The average of all the percent increases will be found at the end.
All of the calculations will be printed to the screen and rounded to two decimals.
'''
#Author: Katie Blasi

#open the designated file
population_file = open("populationbycountry19802010millions.csv")
#assign file contents to variable contents
contents = population_file.read()

#create empty list for numbers
num_list=[]
#split the numbers at the commas
num_list = contents.split(',')
#convert the strings into floats within the list
for i in range(len(num_list)):
    num_list[i] = float(num_list[i])

#start 2 counts to keep track of indices
count1 = 0
count2 = 1
#create empty list to append the % increase for each
percent_increase_list = []

#while the 2nd number is still in the range of the list
while count2 <= len(num_list)-1:
    #first num is determined with count 1
    first_num = num_list[count1]
    
    #second num is determined with count2
    second_num = num_list[count2]
    
    #find the difference of the 2 numbers
    difference = (second_num - first_num)
    
    #use percent increase formula
    percent_increase = (difference / first_num) * 100
    
    #append the number to the list
    percent_increase_list.append(percent_increase)
    #add to both of the counts in order to go to next set of nums in the list
    count1+=1
    count2+=1

#find the min, max, and mean of the data    
minimum = min(percent_increase_list)  
maximum = max(percent_increase_list)
mean = sum(percent_increase_list) / len(percent_increase_list)

#print answers rounded to 2 decimal places
print( "Minimum = " +str(round(minimum,2)) + "%")
print("Maximum = " +str(round(maximum,2))+ "%")
print("Mean = " +str(round(mean,2))+ "%")

#close the file
population_file.close()