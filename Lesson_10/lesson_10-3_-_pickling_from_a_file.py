# Part 1:
import pickle
from Time import Time
myTime1 = Time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
unpickled_time = pickle.loads(pickled_time)
unpickled_time.print_time()

# Part 2:
import pickle
from Time import Time

in_file = open('data.txt', 'rb')

unpickled_time = pickle.load(in_file)

unpickled_time.print_time()
