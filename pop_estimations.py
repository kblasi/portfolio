'''
loads and provides access to census population estimates
These populations are not correct, just made a random list of data in order to run this program
Program includes data from 2010-2018 in United States, Alabama, and Alaska
'''
#open file
pop_file = open("populations.txt")

#read content into list of lines (returns list of strings that are 1 line in the file)
pop_file_records = pop_file.readlines()

#read first line with metadata (string of first line with headers)
metadata_line = pop_file_records[0]

#this is a list of strings containing each of the headers in the first line
metadata_items = metadata_line.split(",")

#create dictionary of state records (High level dictionary)
pop_dict = {}

#each interation goes through a different state or geography
for line_index in range(1, len(pop_file_records)):
    #create dictionary to keep track of population by year
    pop_years = {}
    
    #split the record about a geography into a list
    record_list = pop_file_records[line_index].split(",")
    
    #get the name of the geography
    geography = record_list[0]
    
    #this iterates through each year of a population
    for index in range(1, len(record_list)):
        #add the values to the inside dictionary
        pop_years[eval(metadata_items[index])] = eval(record_list[index])
        
    #add the record to the population dictionary (higher level dictionary)
    pop_dict[geography] = pop_years

#
#user interaction
#

#set up a boolean that says whether the user is still asking about states
asking_about_states = True

while asking_about_states:
    state = input("Type name of state or enter to exit: ")
    
    if state == "":
        asking_about_states = False
        
    elif not(state in pop_dict):
        #tell them they didn't enter a state correctly
        print( state + " is not in our database.")
    else:
        #if we are here, they entered a state that's in pop dict
        
        #ask them about a year of data
        
        #set up boolean to ask about year
        asking_about_years = True
        
        while asking_about_years:
            year = input("Type year or enter to go back to states: ")
            
            if year == "":
                asking_about_years = False
            elif not(eval(year) in pop_dict[state]):
                #year not in dict for state
                print("We don't have data for " + year + " for " + state + '.')
            else:
                #we have correctly entered year we have data for
                print("The population of " + state + " in " + year + " was " + str(pop_dict[state][eval(year)]))