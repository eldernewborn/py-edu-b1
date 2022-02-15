"""
A race track where different kinds of vehicles can compete
"""


class RaceTrack:

    def __init__(self, track_len=100):
        self.contestants = set()
        self.winners = set()
        self.finishline = track_len

    def has_contestants(self):
        return bool(len(self.contestants))

    def has_anyone_won(self):
        return bool(len(self.winners))

    def load_contestants(self, cars):
        for car in cars:
            self.contestants.add(car)

    def time_step(self, time_step=1):
        if self.has_contestants():
            for a_car in self.contestants:
                a_car.tick()
                if a_car.location >= self.finishline:
                    self.winners.add(a_car)
        else:
            print("race track is empty, WTF? ")
