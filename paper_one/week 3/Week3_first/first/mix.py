import numpy as np

def dataType():
    
    arr_a = np.array([1, 2, 3])

    print(arr_a.dtype)

    arr_b = np.array([1, "h", 1.2])

    print(arr_b.dtype)

    arr_c = np.array([1, 2.2, 2, 6])

    print(arr_c.dtype)
    
    arr_d = np.array(["abi", "Achu", "ara"])
    
    print(arr_d.dtype)