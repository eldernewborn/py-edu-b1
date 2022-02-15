"""
Simulating car races the in the OOP way
"""
from vehicles import Car, Motorbike
from racetrack import RaceTrack


def main():
    benz = Car("Beyynz", speed=2)
    bmw = Car("BeeEmVe", speed=2.1)
    peykan = Car("Peykan", speed=3.0)
    jyan = Car("Jyan", speed=4.0)
    gowje = Motorbike("CG125", speed=11.0)
    kawazaki = Motorbike(name="K-Ninja", speed=15.0)
    kawazaki_30 = Motorbike(name="K-Ninja", speed=15.0, t_angle=30)


    pist = RaceTrack(len=10)
    contestants = [benz, bmw, peykan, jyan, gowje]
    pist.load_contestants(contestants)

    for t in range(100):
        pist.time_step()
        if len(pist.winners) >= 3:
            print(pist.winners)
            break
