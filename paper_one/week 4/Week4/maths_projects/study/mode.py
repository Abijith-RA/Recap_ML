num = [10, 20, 20, 40, 50, 20, 10]


def frequency(data):
    
    max_count = 0
    size = len(data)
    mode = None
    
    for i in range(size):
        
        count = 0
        
        for j in range(size):
            if data[i] == data[j]:
                count += 1
                
        if max_count < count:
            
            max_count = count
            mode = data[i]
           
    print(mode)             
    
frequency(num)