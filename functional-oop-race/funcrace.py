"""
simulating a car race using functional style
"""

from functools import partial


def car_location(a_vehicle, t):
    """
    :param a_vehicle:
    :param t:
    :return: current location based on speed
    """
    return a_vehicle[1]*t


def has_won(location, race_len):
    """
    Checks if the vehicle has won the race or not.
    :param location:
    :param race_len:
    :return:
    """
    return location > race_len


def simulate_till_win(vehicles_in_race, racetrack_len=100, time_steps=10):
    for t in range(time_steps):
        # calculate new location of cars
        loc_now = partial(car_location, t=t)
        locations = list(map(loc_now, vehicles_in_race))
        # locations [ 20,30,68,102,350,11,400]
        winners_loc = list(filter(lambda x: has_won(x, racetrack_len), locations))
        #           [ F,F,F,T,T,F,T]
        # filter    [102,350,400]

        if len(winners_loc) >= 3:  # enough winners ?
            winners = [(vehicles_in_race[winners_loc.index(x)][0], x) for x in winners_loc]
            return winners, t


if __name__ == '__main__':
    vehicles = [
        # Name, speed
        ("Beyynz", 2.0),
        ("BeeEmVe", 2.1),
        ("Peykan", 3.0),
        ("Jian", 4.0),
        ("CG125", 11.0)
    ]

    winners_list, wintime = simulate_till_win(vehicles, racetrack_len=100, time_steps=60)
    print(f"At time step {wintime} we had three winners:")
    print("\n".join([str(_) for _ in winners_list]))
