class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.minute_f()
        self.hour_f()
        pass

    def __repr__(self):
        return '{self.__class__.__name__}({self.hour}, {self.minute})'.format(self=self)
        

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        self.minute += minutes
        self.minute_f()
        return str(self)

    def __sub__(self, minutes):
        self.minute -= minutes
        self.minute_f()
        return str(self)

    def minute_f(self):
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        self.hour_f()
            
    def hour_f(self):
        while self.hour < 0:
            self.hour += 24
            
        while self.hour >= 24:
            self.hour -= 24