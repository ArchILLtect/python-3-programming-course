import pickle
from Time import Time

myTime1 = Time(1, 2, 3)
out_file = open('data.txt', 'wb')
pickled_time = pickle.dump(myTime1, out_file)
out_file.close()

