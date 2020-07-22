'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    zero_container = []
    non_zero_container = []
    
    for i in range(0, len(arr)):
        
        #if array at current index = 0 
        #remove it and put it into a new array
        if arr[i] == 0:
            zero_container.append(arr[i])
        else:
            non_zero_container.append(arr[i])
    #append zero container numbers to arr
    if len(zero_container) > 0:
        for i in zero_container:
            non_zero_container.append(i)
            arr = non_zero_container
    
    return arr


  


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")