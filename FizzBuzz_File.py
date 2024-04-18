import numpy as np
    
def FizzBuzz(start, finish):
    numvec = np.arange(start, finish)  
    objvec = np.array(numvec, dtype = object)  

    fizzbuzz = np.where((numvec % 3 == 0) & (numvec % 5 == 0), "fizzbuzz", objvec)  
    fizz = np.where((numvec % 3 == 0) & (numvec % 5 != 0), "fizz", fizzbuzz)  
    buzz = np.where((numvec % 5 == 0) & (numvec % 3 != 0), "buzz", fizz) 

    return buzz.tolist() 
