'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    #store length of array in variable
    input_length = len(arr)

    if input_length < 3:
        arr = arr[::-1]
        return arr

    else:
        storage = []
        for i in range(0, len(arr)):
            if i == 0: 
                # we then want to multiply the rest of the values together
                product = 1
                for j in range(i + 1, input_length):
                    # multiply each value until loop is done
                    next_val = arr[j]
                    product = product * next_val
                # set value of current index to product
                storage.append(product)
            
            else: #probably just an else statement
                compare_index = i - 1
                product = 1
                while compare_index >= 0:
                    product = product * arr[compare_index]
                    compare_index -= 1 

                for j in range(i + 1, input_length):
                    next_val = arr[j]
                    product = product * next_val

                storage.append(product)
        

    return storage


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
