import string
import numpy as np
import redis
import pickle

class Array:

    def __init__(self, name: string, array: np.array) :
        self.name = string
        self.array = np.array

    def read(r, name: string):

        
        
        value = r.get(name)
        shape = r.get(name + "shape")
        
        shape_decoded = np.array(np.frombuffer(shape, dtype=int))
        decoded = np.array(np.frombuffer(value, dtype=int))
        reshaped = np.reshape(decoded, (shape_decoded))

        response = print(reshaped)
        return response

    def create(r, name: string, array: np.array):

        def toRedis(r,array,name):
            """Store given Numpy array 'a' in Redis under key 'n'"""
            shape = np.array(array.shape)
            encoded_shape = shape.tobytes()
            encoded = array.tobytes()

            # Store encoded data in Redis
            shape_array = r.set(name + "shape", encoded_shape)
            test_array = r.set(name, encoded)
            # Store array shape in Redis

            test_array = pickle.dumps(name, protocol=0)

            print(r.get(name + "shape"))
            return test_array

        toRedis(r, array, name)

        response = print(r.get('test_array'))


        return response

    def delete(r, name: string):

        r.delete(name)

        response = print("Array has been deleted")
        return response
