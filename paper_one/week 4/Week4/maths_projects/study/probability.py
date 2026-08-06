
def prob(favaroble,total_outcome):
    
    probability = favaroble / total_outcome
    
    return probability

def prob_dict(data):
    
    total = 0
    
    for value in data.values():
        total += value
        
    print("Total = ",total)
    
    for key, value in data.items():
        print("color :", key)
        print("count :", value)
        favorable = value
        total_is = total
        
        proability = favorable / total_is
        
        print(f"probability of {key} = {proability:.2f}")
    
inputdata = {"red": 20, "black": 15, "blue": 10}    
# prob_dict(inputdata)

def prob_ind(probility_one, probaility_two):
    
    both_head = probility_one * probaility_two
    
    return both_head

# print(prob_ind(0.5,0.5))



