from . import mean

def std(data):
    
    size = len(data)
    sum = 0
    avg = mean.average(data)
    
    for i in data:
        step_one = (i - avg)**2
        
        sum += step_one
    varience = sum / size
    
    stdVarience = varience**0.5
    
    return stdVarience    