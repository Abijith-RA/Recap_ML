ages = [18, 12, 15, 20, 22, 26]

def average(data):
    
    total = 0
    count = 0
    
    for num in data:
        
        total += num
        count += 1
        
        avg = total / count
    
    return avg
    
result = average(ages)
print(result)