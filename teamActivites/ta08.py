# CS241 Team Activity 08

class Time:

    def __init__(self):
        self._hours = 0
        self._minutes = 0
        self._seconds = 0
           
    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        if hours < 0:
            self._hours = 0
        elif hours > 23:
            self._hours = 23 
        else:
            self._hours = hours

    hours = property(get_hours, set_hours)

    def get_minutes(self):
        return self._minutes
 
    def set_minutes(self, minutes):
        if minutes < 0:
            self._minutes = 0
        elif minutes > 59:
            self._minutes = 59
        else:
            self._minutes = minutes

    minutes = property(get_minutes, set_minutes)

    def get_seconds(self):
        return self._seconds
 
    def set_seconds(self, seconds):
        if seconds < 0:
            self._seconds = 0
        elif seconds > 59:
            self._seconds = 59
        else:
            self._seconds = seconds

    seconds = property(get_seconds, set_seconds)

def display(time):
    #print("{}:{}:{}" .format(time.get_hours(), time.get_minutes(), time.get_seconds()))
    print("{}:{}:{}" .format(time.hours, time.minutes, time.seconds))
    print()

def main():
    time1 = Time()
    #time1.set_hours(8)
    #time1.set_minutes(30)
    #time1.set_seconds(10)
    time1.hours = 8
    time1.minutes = 30
    time1.seconds = 10
    display(time1)
    time2 = Time()
    #time2.set_hours(24)
    #time2.set_minutes(-2)
    #time2.set_seconds(70)
    time2.hours = 24
    time2.minutes = -2
    time2.seconds = 70
    display(time2)
    time3 = Time()
    #time3.set_hours(0)
    #time3.set_minutes(5)
    #time3.set_seconds(10)
    time3.hours = 0
    time3.minutes = 5
    time3.seconds = 10
    display(time3)
    time4 = Time()
    #time4.set_hours(12)
    #time4.set_minutes(5)
    #time4.set_seconds(10)
    time4.hours = 12 
    time4.minutes = 5
    time4.seconds = 10
    display(time4)


if __name__ == "__main__":
    main()

    

