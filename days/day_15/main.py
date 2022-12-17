import re
import time
from os.path import dirname
from pathlib import Path
from misc import read_day, submit_day, prettytime, Point


def parse_sensors(data):
    p = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    sensors = []
    for line in data:
        m = p.match(line)
        sensor = Point(int(m[1]), int(m[2]))
        beacon = Point(int(m[3]), int(m[4]))
        sensor_dist = sensor.man_dist(beacon)
        sensors.append((sensor, beacon, sensor_dist))
    return sensors


def execute_part1():
    input_file = "input.txt"
    # input_file = "test_input.txt"
    with open(Path(dirname(__file__)) / input_file, "r", encoding="utf-8") as f:
        data = f.read().split('\n')
    sensors = parse_sensors(data)

    y_line = 2_000_000
    # y_line = 10

    in_sensor_range = []
    beacons_in_line = set()
    no_sensor_points = set()
    for sensor, beacon, sensor_range in sensors:
        axis_dist = abs(sensor.y - y_line)
        x_range = sensor_range - axis_dist
        if x_range < 0:
            continue
        x_from = sensor.x - x_range
        x_to = sensor.x + x_range
        in_sensor_range.append([Point(x_from, y_line), Point(x_to, y_line)])
        if beacon.y == y_line:
            beacons_in_line.add(beacon.x)
        for i in range(x_from, x_to+1):
            if i == beacon.x or i in beacons_in_line:
                continue
            no_sensor_points.add(i)
    return len(no_sensor_points)


def execute_part2():
    # input_file = "input.txt"
    input_file = "test_input.txt"
    with open(Path(dirname(__file__)) / input_file, "r", encoding="utf-8") as f:
        data = f.read().split('\n')
    sensors = parse_sensors(data)

    y_min = 0
    y_max = 20
    # y_max = 4_000_000

    for y_line in range(y_min, y_max+1):
        unknown_points = set(range(y_min, y_max+1))
        for sensor, beacon, sensor_range in sensors:
            axis_dist = abs(sensor.y - y_line)
            x_range = sensor_range - axis_dist
            if x_range < 0:
                continue
            x_from = sensor.x - x_range
            x_to = sensor.x + x_range
            for i in range(max(x_from, 0), min(x_to, y_max)+1):
                if i in unknown_points:
                    unknown_points.remove(i)
        if len(unknown_points) > 0:
            return y_line + next(iter(unknown_points)) * 4_000_000


if __name__ == '__main__':
    read_day(15)
    tic = time.perf_counter()
    res1 = execute_part1()
    tac = time.perf_counter()
    res2 = execute_part2()
    toc = time.perf_counter()
    # submit_day(res1, 15, 1)
    # submit_day(res2, 15, 2)
    print(f"day 15 part 1 in {prettytime(tac - tic)}, answer: {res1}")
    print(f"day 15 part 2 in {prettytime(toc - tac)}, answer: {res2}")

# wrong answer: 108000000
# That's not the right answer; your answer is too low.  If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit.  Please wait one minute before trying again. (You guessed 108000000.) [Return to Day 15]
