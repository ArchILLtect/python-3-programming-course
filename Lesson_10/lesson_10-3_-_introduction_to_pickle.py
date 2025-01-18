import pickle
from Time import Time

myTime1 = Time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
print (pickled_time)

