distances = [2, 5, 8, 10, 15]

def average(data):
    
    
    size = len(data)
    total = 0
    
    
    for num in data: #dont use (size)
        
        total += num
        
        avg = total / size
        
    return avg    


result = average(distances)

print(result)