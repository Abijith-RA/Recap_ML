list = [1, 2, 3]

result =[num**2 if num % 2 == 0 else num**3 for num in list]

print(result)