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

    data = pd.read_csv(filepath, names = ['id', 'date and time', 'longitude', 'latitude'])

    for x in data['longitude']:
        longitude.append(x)
    for y in data['latitude']:
        latitude.append(y)
    for z in range(0, len(longitude)):
        coordinates.append([longitude[z], latitude[z]])

    return coordinates



test = 'C:/Users/Ice Lin/.spyder-py3/test.txt'
coordinate_test = parse_data(test)
print(coordinate_test)

to_plot = np.array(coordinate_test)
plt.scatter(to_plot[:,0], to_plot[:,1], alpha=1.0, edgecolors='b')
plt.xlabel('longitude')
plt.ylabel('latitude')
