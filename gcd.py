'''
This program will have two different functions to determine the greatest
common divisior. The naive_gcd function takes two integers and uses the smallest
to start finding the gcd. If that candidate gcd isn't correct, we will subtract
one until we find the right answer. In the second function, euclidean_gcd, we
use the euclidean method where the difference is considered in finding the gcd.
Both functions' iteration counts are kept track of in order to see the efficiency of
the equations.
'''
#Author: Katie Blasi

def naive_gcd(integer1, integer2):
    #find min and max of the integers
    x = min(integer1, integer2)
    y = max(integer1, integer2)
    #create answer variable
    answer=0
    #new empty list to add answers to
    new_list=[]
    #create candidate gcd with smaller integer
    candidate_gcd = x
    #variable to count interations
    count_loops=0
    #iterate while the num is greater than zero
    while candidate_gcd>0:
        #if both numbers are divisible by candidate
        if y % candidate_gcd == 0 and x % candidate_gcd == 0:
            #assign that number to the answer variable
            answer = candidate_gcd
            #add to count loop num
            count_loops+=1
            #append answer and count to the answer list
            new_list.append(answer)
            new_list.append(count_loops)
            #return the answer
            return new_list
        #if it doesn't divide right, subtract 1 from candidate and add to count
        else:
            count_loops+=1
            candidate_gcd-=1    


   
def euclidean_gcd(integer1,integer2):
    #empty list to add answers to
    answer_list=[]
    #count for loop process
    count=0
    #difference variable
    difference = 0
    
    #get the bigger and smaller numbers
    bigger_num = max(integer1, integer2)
    smaller_num = min(integer1, integer2)
    
    #take the absolute value of each integer
    integer1 = abs(bigger_num)
    integer2 = abs(smaller_num)
    
    #go thro while the integers don't equal each other until they do
    if integer1 > integer2:
        while integer1 != integer2:
            #find the difference of the 2
            difference = abs(integer1 - integer2)
            #add to count loops
            count+=1
            #assign the integer to the variable
            integer1 = integer2
            #assign the difference to the other variable
            integer2 = difference
        #add the gcd and the count to the list
        answer_list = [integer1 , count]
    
    #if the numbers are equal
    elif integer1 == integer2:
        #add the num and count to the list
        answer_list = [integer1, 0]
        
    #return the answer list
    return answer_list