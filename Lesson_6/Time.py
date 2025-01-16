class Time:
    """ Blueprint for a Time object"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)

    def tick(self, seconds = 1):
        self.set_second(self.get_second() + seconds)

    def set_hour(self, hour):
        self.__hour = hour

    def get_hour(self):
        return self.__hour

    def set_minute(self, minutes):
        if minutes >= 60:
            addedHours = minutes // 60
            newMinutes = minutes % 60
            self.set_hour(self.get_hour() + addedHours)
            self.set_minute(newMinutes)
        else:
            self.__minute = minutes

    def get_minute(self):
        return self.__minute

    def set_second(self, seconds):
        if seconds >= 60:
            addedMins = seconds // 60
            newSeconds = seconds % 60
            self.set_minute(self.get_minute() + addedMins)
            self.set_second(newSeconds)
        else:
            self.__second = seconds

    def get_second(self):
        return self.__second
