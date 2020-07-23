'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    result = []

    for i in range(0, len(nums) - (k-1)):
        #populate empty array and find max val
        #max method
        current = i
        storage = []
        counter = 0
        #loop to fill in storage with current val and 
        #the next (k) values 
        while current + k - 1 < len(nums) and counter < k:
            storage.append(nums[i])
            counter += 1 
            highest_val = max(storage)
            i += 1
            
        result.append(highest_val)

        


    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
