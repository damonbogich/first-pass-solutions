'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr): 
    
    for i in range(0, len(arr) - 1):
        current = i #0

        #need to compare first index to the rest of the indices
        #while loop
        compare = i + 1
        searching = True
        # while_counter = 0
        while searching is True and compare <= len(arr):
            if compare == len(arr):
                return arr[current]
            else:
                if arr[current] == arr[compare]:
                    arr.pop(compare)
                    searching = False
                else:
                    compare += 1





if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")