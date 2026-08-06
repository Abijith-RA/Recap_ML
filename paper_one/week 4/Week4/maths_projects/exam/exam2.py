outcome = [1, 2, 3, 4, 5, 6]

total = len(outcome)

favorable = 0

for num in outcome:
    if num > 4:
        favorable += 1
        
probability = favorable / total
percentage = probability * 100

print(f"{probability:.2f}")
print(f"{percentage:.2f}%")