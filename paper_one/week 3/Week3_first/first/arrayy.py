import numpy as np

def arrayFunction():
    
    array = np.array([1, 2, 3])
    
    return array

def arrayZero():
    
    array = np.zeros(5 , dtype=int)
    print(array)
    
    array_two = ((3, 3))
    print(array_two)
    
def arrayOnes():
    
    array = np.ones(5, dtype=int)
    print(array)
    
    array_two = np.ones((3,3))
    print(array_two)
    
def arrayEmpty():
    
    array = np.empty(5)
    print(array)
    
def arrayArange():
    
    array = np.arange(5)
    print(array)
    
    array_two = np.arange(0, 10, 2)
    print(array_two)

def arrayLinspace():
    
    array = np.linspace(0, 1, 5)
    print(array)

def arrayEye():
    
    array = np.eye(3)
    print(array)

def arrayFull():
    
    array = np.full((3, 3), 7)
    print(array)

def arrayRand():
   
   array = np.random.rand(2, 2)
   array = np.round(array, 2)
   print(array)

def arrayRandint():
    array = np.random.randint(1, 100, 10)
    print(array)