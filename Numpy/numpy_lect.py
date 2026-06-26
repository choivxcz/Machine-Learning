import numpy as np

def basics():
    print("Basics of Numpy Arrays")
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([[1, 2, 3], [2, 3, 4]])
    c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    #Getdimensions if 1D, 2D, 3D, and such
    print(a.ndim)
    print(b.ndim)
    print(c.ndim)
    #GetShape if 2x2, 3x3, and such
    print(a.shape)
    print(b.shape)
    print(c.shape)

    #GetType of data and its size in bytes
    print(a.dtype)
    print(b.dtype)
    print(c.dtype)

    #GetSize of the array, which is the total number of elements in the array
    print(a.size)
    print(b.size)
    print(c.size)
    print("end of basics")

print(basics())

def Accessing_Changing_specific_elements_rows_columns_etc():
    print("Accessing, Changing specific elements, rows, columns, etc.")
    a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
    
    #Get a specific element [row, column]
    print(a[0, 5], a[1, 6])
    #Get a specific row
    print (a[0, :], a[1, :])
    #Get a specific column
    print(a[:, 0], a[:, 1])
    #With slicing, get a specific part of the array [start:end:step]
    print(a[0, 2:7:3], a[1, 2:7:3])
    
    #try with 3D array
    print("3D array")
    b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(b[0, 0, 0], b[1, 1, 1]) 
    #replace
    b[:, 0, :] = [9, 9], [8, 8]
    print(b)
    print("end of Accessing_Changing_specific_elements_rows_columns_etc")
    
print(Accessing_Changing_specific_elements_rows_columns_etc())

def  Initializing_Different_Arrays_1s_0s_full_random_etc():
    print("Initializing Different Arrays")
    #All 0s matrix
    a = np.zeros((2, 3))
    print(a)
    #All 1s matrix
    b = np.ones((3, 4))
    print(b)
    #Any other number
    c = np.full((2, 2), 7)
    print(c)
    #Random decimal numbers between 0 and 1
    d = np.random.rand(2, 3)
    print(d)
    #Random integers between a specified range
    e = np.random.randint(1, 10, size=(3, 4))
    print(e)
    print("end of Initializing Different Arrays")

print(Initializing_Different_Arrays_1s_0s_full_random_etc())

def test():
    arrside = np.ones((5, 5))
    print(arrside)
    arrmid = np.zeros((3, 3))
    print(arrmid)
    arrmid[1, 1] = 9
    print(arrmid)
    arrside[1:4, 1:4] = arrmid
    print(arrside)
print(test())

def test1():
    arrside = np.ones((4, 4))
    print(arrside)
    arrcenter = np.zeros((2, 2))
    print(arrcenter)
    arrside[1:3, 1:3] = arrcenter
    print(arrside)
print(test1())

def test2():
    a = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])
    print(a)
    a[1, 1:4] = 0
    print(a)
print(test2())

def test3():
    a = np.random.randint(1, 100, size=(5, 5))
    print(a)
    print(a[2:5, 2:5])
print(test3())

def test4():
    arrside = np.zeros((5, 5))
    print(arrside)
    arrmid = np.full((3, 3), 5)
    print(arrmid)
    arrmid[1:2, 1:2] = 9
    print(arrmid)
    arrside[1:4, 1:4] = arrmid
    print(arrside)
print(test4())

#### Mathematical Operations ####
def mathematical_operations():
    print("Mathematical Operations")
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([6, 7, 8, 9, 10])
    
    #Element-wise addition
    print(a + b)
    #Element-wise subtraction
    print(a - b)
    #Element-wise multiplication
    print(a * b)
    #Element-wise division
    print(a / b)
    
    #Mathematical functions
    print(np.sqrt(a))  # Square root
    print(np.exp(a))   # Exponential
    print(np.log(a))   # Natural logarithm
    print(np.sin(a))   # Sine function
    print(np.cos(a))   # Cosine function
    print("end of Mathematical Operations")
print(mathematical_operations())