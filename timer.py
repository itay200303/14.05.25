import datetime

class Timer:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.started_at = datetime.datetime.now()

    def __str__(self):
        return f"Timer '{self.name}' set for {self.duration} minutes (started at: {self.started_at.strftime('%H:%M:%S')})"

    def __repr__(self):
        return f"Timer('{self.name}', {self.duration})"

    def __del__(self):
        print(f"Goodbye from timer '{self.name}'!")

timer1 = Timer('Workout', 45)
timer2 = Timer('Cooking', 30)

timer1.paused = False

timers = [timer1, timer2]
print([repr(timer) for timer in timers])

del timer1.paused

del timer1
