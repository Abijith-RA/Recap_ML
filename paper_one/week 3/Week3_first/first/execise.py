# elementwise = a * b              # [4 10 18] do
# dot = np.dot(a, b)                # 1*4 + 2*5 + 3*6 = 32
# comparison = (a == b)             # [False False False]
# are_equal = np.array_equal(a, b)  # False
import numpy as np

def solved():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    multipilication = a * b

    print(multipilication)

    print(np.dot(a, b))

    print(a == b)

    print(np.array_equal(a, b))
    
solved()    