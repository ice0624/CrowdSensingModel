import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def parse_data(filepath):
    """
    Parses .txt file of taxi coordinates, where each line is in the format:
    taxi id, date time, longitude, latitude.

    Parameters
    ----------
    filepath: str
        filepath of the .txt file being parsed

    Returns
    -------
    coordinates: list
        list of coordinate pairs

    """

    longitude = []
    latitude = []
    coordinates = []

    # list will contain, in order, x_min, x_max, y_min and y-max
    boundaries = []

    data = pd.read_csv(filepath, names=['id', 'date and time', 'longitude', 'latitude'])

    for x in data['longitude']:
        longitude.append(x)
    for y in data['latitude']:
        latitude.append(y)

    x_min = min(longitude)
    x_max = max(longitude)
    y_min = min(latitude)
    y_max = max(latitude)

    boundaries.append(x_min)
    boundaries.append(x_max)
    boundaries.append(y_min)
    boundaries.append(y_max)

    for z in range(0, len(longitude)):
        coordinates.append([longitude[z], latitude[z]])

    return coordinates, boundaries

    # add_trajectory


# initialize worldview

trajectory_one = 'C:/Users/Ice Lin/.spyder-py3/1.txt'
t_one_coordinates, bounds = parse_data(trajectory_one)

x_min = bounds[0]
x_max = bounds[1]
y_min = bounds[2]
y_max = bounds[3]

print(str(x_min))
print(str(x_max))
print(str(y_min))
print(str(y_max))

trajectory_two = 'C:/Users/Ice Lin/.spyder-py3/10.txt'
t_two_coordinates, bounds_two = parse_data(trajectory_two)

trajectory_three = 'C:/Users/Ice Lin/.spyder-py3/100.txt'
t_three_coordinates, bounds_three = parse_data(trajectory_three)

# 100m distance is roughly .0009 degrees of latitude
# 100m distance is roughly .00117 degrees of longitude

plot_one = np.array(t_one_coordinates)
plt.xlim(bounds[0], bounds[1])
plt.ylim(bounds[2], bounds[3])
plt.xticks(np.arange(bounds[0], bounds[1], step=0.00117))
plt.yticks(np.arange(bounds[2], bounds[3], step=0.0009))

plot_two = np.array(t_two_coordinates)
plot_three = np.array(t_three_coordinates)

plt.scatter(plot_one[:, 0], plot_one[:, 1])

plt.scatter(plot_two[:, 0], plot_two[:, 1])
plt.scatter(plot_three[:, 0], plot_three[:, 1])

plt.plot(plot_one[:, 0], plot_one[:, 1], linewidth=1.0)

plt.plot(plot_two[:, 0], plot_two[:, 1], linewidth=1.0)
plt.plot(plot_three[:, 0], plot_three[:, 1], linewidth=1.0)

plt.xlabel('longitude')
plt.ylabel('latitude')
plt.grid(True)
