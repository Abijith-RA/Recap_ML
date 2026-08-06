list = [10, 20, 50, 80, 30, 40, 9, 90]

def median(data):
    
    size = len(data)
    
    for i in range(size):
        
        for j in range(i+1, size):
            
            if data[i] > data[j]:
                
                data[i], data[j] = data[j], data[i]
    
    print(data)
    
    mid_index = size // 2
    
    if(size % 2 == 0):
        
        mid1 = mid_index
        mid2 = mid_index -1
        
        median = (data[mid1] + data[mid2]) / 2
        
    else:
        
        median = data[mid_index]    
        
    print(median)
    
print(median(list))    