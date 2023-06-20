import json
import numpy as np



def load_JSON(path=None):
    '''
    :param path: (str) path name the .json file is located at.
    :return data: Dictionary-like with the following attributes:
                unrotated_data : {ndarray} of shape (12000, 2)
                rotated_data : {ndarray} of shape (12000, 2)
    '''
    if path is None:
        raise ValueError('Please input path name')

    with open(path) as json_file:
        data = json.load(json_file)

    for key in PLB.keys():
        data[key]  = np.array(data[key])
    return data




def objective_function():
    '''
    :param input: (input type)
    :return data: (return type)
    '''
    return None


def get_Jacobian():
    '''
    :param input: (input type)
    :return data: (return type)
    '''
    return None
