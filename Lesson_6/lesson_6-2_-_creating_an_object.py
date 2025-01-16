class Time:
    """ Blueprint for a Time object"""
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print (self.hour, ":", self.minute, ":", self.second)

myTime1 = Time()
myTime1.print_time()
print("-" * 80)

myTime1.set_time(1, 2, 3)
myTime1.print_time()
