'''
This program takes a csv file with population data in Iowa from 2010-2018 and
puts it into a dictionary. It then prompts the user to input the desired key
which is the year, and it will print out the population. If the user enters
an empty string, the program will exit. If the user enters invalid key, it will
explain the directions and prompt them again. 
'''
#Author: Katie Blasi

pop_file = open("PEP_2018_PEPANNRES.csv")

#read the line of the file
pop_file_records = pop_file.readlines()


#go thro each line of different state
for pop_record in pop_file_records:
    
    #create dictionary to put key and values in
    pop_years={}
    
    #split the populations into a list by each comma
    record_list = pop_record.split(',')
    
    #first year of data is 2010
    curr_year = 2010
    
    #iterate through the list of data
    for index in range(len(record_list)):
        #set the dictionary key to the corresponding data value
        pop_years[str(curr_year)] = eval(record_list[index])
        
        #update the year
        curr_year+=1

#welcome print statements and directions       
print("Welcome to the Iowa Population Retriever")
print("Enter year between 2010 and 2018 to get Iowa's population that year")
print("Press enter to exit")
user_input = input("Enter year: ")


#loop with conditions
entering_years = True
while entering_years:
    #if entered year is in the keys
    if user_input in pop_years:
        #print and prompt again
        print(pop_years[user_input])
        user_input = input("Enter year: ")
    
    #if user enters empty string
    elif user_input == '':
        print("Thank you for using our service")
        #change condition to false and print thanks
        entering_years = False
        
    
    #else (input not in key)
    else:
        #print directions and prompt again
        print("Enter year between 2010 and 2018 to get Iowa's population that year")
        print("Press enter to exit")
        user_input = input("Enter year: ")
         
#close the file    
pop_file.close()