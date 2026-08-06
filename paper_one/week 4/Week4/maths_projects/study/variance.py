from . import mean

ages = [18, 12, 15, 20, 22, 26]

def varian(data):
    
    size = len(data)
    sum = 0
    avg = mean.average(data)
    print(avg)
    
    for i in data:
        sum_of_mean_value = (i - avg)**2
        
        sum += sum_of_mean_value
        
    var = sum / size
    
    return var
        
        