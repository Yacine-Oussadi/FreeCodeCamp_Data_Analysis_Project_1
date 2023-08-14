import numpy as np
    
def calculate(input_list: list):
    if len(input_list) != 9:
        raise ValueError("Input list must be of length = 9")
    else:
        matrix = np.reshape(np.array(input_list), (3,3))
        
        
        mean = []
        mean.append(list(np.mean(matrix, axis = 0))) #type: ignore
        mean.append(list(np.mean(matrix, axis = 1))) #type: ignore
        mean.append((np.mean(matrix))) #type: ignore

        variance = []
        variance.append(list(np.var(matrix, axis = 0))) #type: ignore
        variance.append(list(np.var(matrix, axis = 1))) #type: ignore
        variance.append((np.var(matrix))) #type: ignore
        
        standard_variation = []
        standard_variation.append(list(np.std(matrix, axis = 0))) #type: ignore
        standard_variation.append(list(np.std(matrix, axis = 1))) #type: ignore
        standard_variation.append((np.std(matrix))) #type: ignore
        
        maximum = []
        maximum.append(list(np.max(matrix, axis = 0))) 
        maximum.append(list(np.max(matrix, axis = 1)))
        maximum.append((np.max(matrix)))
        
        
        
        mimimum = []
        mimimum.append(list(np.min(matrix, axis = 0)))
        mimimum.append(list(np.min(matrix, axis = 1)))
        mimimum.append((np.min(matrix)))
        
       
        
        sumation = []
        sumation.append(list(np.sum(matrix, axis = 0)))
        sumation.append(list(np.sum(matrix, axis = 1)))
        sumation.append((np.sum(matrix)))
        
        calculations = {'mean' : mean, 
                      'variance' : variance,
                      'standard deviation' : standard_variation,
                      'max' : maximum,
                      'min' : mimimum,
                      'sum' : sumation}
        
        return calculations