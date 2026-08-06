import matplotlib.pyplot as plot

data = {
    "Name": ["Asha", "Rahul", "Meera", "Arun", "Neha"],
    "Marks": [78, 65, 92, 55, 85]
}

plot.bar(data["Name"], data["Marks"], color = "grey", edgecolor = "black")
plot.ylim(0, 100)
plot.show()
