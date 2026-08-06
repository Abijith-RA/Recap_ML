import mean

Ages = [10, 1, 3, 7, 11, 14, 34, 52, 18, 13]

mean.average(Ages)

def middle_number(data):
    
    size = len(data)
    
    for i in range(size):
        
        for j in range(i + 1,size):
            if data[i] > data[j]:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp        
    print("sorted values :",data)
    
    if (size % 2 != 0):     
            middle_index = (size) // 2
            median = data[middle_index]
            print(median)
    else:
        middle_index = (size) // 2
        middle_one = middle_index
        middle_two = middle_index - 1
        
        median = (data[middle_one] + data[middle_two]) // 2
        
        print(median)
    
middle_number(Ages)                
