import matplotlib.pyplot as plt

def liner(hours, scores):
    
    plt.scatter(scores, hours)
    plt.xlabel("Hours")
    plt.ylabel("Score")
    plt.ylim(0, 100)
    plt.show()