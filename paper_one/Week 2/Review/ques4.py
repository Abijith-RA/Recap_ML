data = {"apple": 5, "banana": 2, "cherry": 7}

manipulated = dict(sorted(data.items(), key=lambda item: item[1]))

print(manipulated)