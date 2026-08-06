#3 number argu in funtion largest

def largest_number(a,b,c):
    if a > b and a > c:
        print("largest number is ",a)
    elif b > a and b > c:
        print("largest number is ",b)
    else:
        print("largest number is", c)    
    
print(largest_number(100, 20, 30))    