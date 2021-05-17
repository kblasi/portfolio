'''
We'll take two matrices with the same dimensions, add them, and return the result
'''
 #do it this way or use range function?
def matrix_addition(a, b):
    ' a and b are two dimensional matrices with the same dimensions '
   
    #initialize the sum of a and b to be a copy of a
    sum_of_matrices = a.copy()
    
    #assuming we have two in same dimensions
    for i in range(len(a)):
        for j in range(len(a[0])):
            sum_of_matrices[i][j] = a[i][j] + b[i][j]
    
    return sum_of_matrices

def matrix_addition2(a,b):
    sum_of_matrices = a.copy()
    
    i = 0
    
    for curr_list in a:
        j = 0
        for curr_number in curr_list:
            sum_of_matrices[i][j] = a[i][j] + b[i][j]
            j+=1
        i+=1
    return sum_of_matrices

#while loop matrices (unessecarily hard)
def matrix_addition3(a,b):
    sum_of_matrices = a.copy()
    
    i = 0
    
    while i < len(a):
        j = 0
        while j < len(a[0]):
            sum_of_matrices[i][j] = a[i][j] + b[i][j]
            j+=1
        i+=1
    return sum_of_matrices