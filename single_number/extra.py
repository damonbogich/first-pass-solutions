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
        arr == storage

    return arr

inin = [1,2,3,4]
product_of_all_other_numbers(inin)