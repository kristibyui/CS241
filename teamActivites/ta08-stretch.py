# CS241 Team Activity 08 - Stretch

class Time:

    def __init__(self):
        self._seconds = 0
           
    def get_hours(self):
        return self._seconds // (60 * 60)

    def set_hours(self, hours):
        if hours < 0:
            self._seconds += 0
        elif hours > 23:
            self._seconds += 23 * (60 * 60)
        else:
            self._seconds += hours * (60 * 60)

    hours = property(get_hours, set_hours)

    def get_minutes(self):
        minutes_sec = self._seconds % (60 * 60)
        return minutes_sec // 60 
 
    def set_minutes(self, minutes):
        if minutes < 0:
            self._seconds += 0
        elif minutes > 59:
            self._seconds += 59 * 60
        else:
            self._seconds += minutes * 60

    minutes = property(get_minutes, set_minutes)

    def get_seconds(self):
        minutes_sec = self._seconds % (60 * 60)
        seconds = minutes_sec % 60
        return seconds 
 
    def set_seconds(self, seconds):
        if seconds < 0:
            self._seconds += 0
        elif seconds > 59:
            self._seconds += 59
        else:
            self._seconds += seconds

    seconds = property(get_seconds, set_seconds)

    @property
    def hours_simple(self):
        simple = self.hours % 12
        if simple == 0:
            return 12
        return simple 

    @property
    def period(self):
        if self.hours < 12:
            return "AM"
        else:
            return "PM"

def display(time):
    print("{}:{}:{}" .format(time.hours, time.minutes, time.seconds))
    print("{}:{}:{} {}" .format(time.hours_simple, time.minutes, time.seconds, time.period))
    print()

def main():
    time1 = Time()
    time1.hours = 8
    time1.minutes = 30
    time1.seconds = 10
    display(time1)
    time2 = Time()
    time2.hours = 24
    time2.minutes = -2
    time2.seconds = 70
    display(time2)
    time3 = Time()
    time3.hours = 0
    time3.minutes = 5
    time3.seconds = 10
    display(time3)
    time4 = Time()
    time4.hours = 12 
    time4.minutes = 5
    time4.seconds = 10
    display(time4)


if __name__ == "__main__":
    main()

    

