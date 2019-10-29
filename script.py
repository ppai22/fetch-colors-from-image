import cv2
import pandas as pd
from sklearn.cluster import KMeans
from math import sqrt


def fetch_pixels(file):
    """Method returns RGB values for every pixel in the input image file"""
    # Reads image using Open-CV
    image = cv2.imread(file)
    # Finds the height and width of the image in pixels
    height, width = image.shape[:2]
    rgb_list = []
    # Finds the RGB values of each pixel in the image
    for x in range(width):
        for y in range(height):
            pixel = list()
            # R value
            pixel.append(image[y, x, 2])
            # G value
            pixel.append(image[y, x, 1])
            # B value
            pixel.append(image[y, x, 0])
            rgb_list.append(pixel)
    # Returns list of all RGB values
    return rgb_list


def fetch_cluster_centers(file_name, k):
    """Method returns the major colours in the image by performing K-Means clustering on the rgb values of the pixels"""
    # Fetch RGB values for all pixels in the image
    rgb = fetch_pixels(file_name)
    # Convert to dataframe to be used in SciKitLearn
    df = pd.DataFrame(rgb)
    # Defining the clustering model
    cluster_model = KMeans(n_clusters=k)
    cluster_model.fit(df)
    # Centroids of the clusters
    cluster_centers = cluster_model.cluster_centers_
    new_cluster_centers = []
    # Rounding off the centroid values to nearest integer
    for center in cluster_centers:
        new_center = []
        for value in center:
            new_center.append(int(round(value)))
        new_cluster_centers.append(new_center)
    return new_cluster_centers


def dist(p1, p2):
    """Method returns the Euclidean distance between two points (RGB tuples)"""
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


def fetch_colors():
    """Method returns dict of colours and RGB tuples for available colours in CSS3"""
    # CSV file containing colour names and RGB values for 864 recognized colour names
    filename = r'colors.csv'
    columns = ['color', 'name', 'hex', 'r', 'g', 'b']
    data = pd.read_csv(filename, names=columns)
    color_dict = {}
    # Separating out the colour names and RGB values to lists
    colors = data.loc[:, 'name'].to_list()
    r = data.loc[:, 'r'].to_list()
    g = data.loc[:, 'g'].to_list()
    b = data.loc[:, 'b'].to_list()
    rgb_list = list(zip(r, g, b))
    # Creating a look-up table with colour names and corresponding RGB values
    for i in range(len(colors)):
        color_dict[colors[i]] = rgb_list[i]
    return color_dict


def fetch_nearest_color(rgb_color):
    """Method fetches the nearest colour to the input RGB value and returns the name from available CSS3 colours"""
    # Fetches look-u[ table
    colors = fetch_colors()
    # Initializing the colour and distance to that of Amber because I like Amber :p
    dis = dist(rgb_color, colors['Amber'])
    color = 'Amber'
    # Iterating over every colour in the look-up table and finding the closest colour to the input RGB value
    for color_name, rgb_value in colors.items():
        if dist(rgb_color, rgb_value) < dis:
            dis = dist(rgb_color, rgb_value)
            color = color_name
    # Returning the nearest colour
    return color


if __name__ == '__main__':
    # Path to image in JPEG format
    image_file = r'test_image.jpg'
    # Number of colours the script has to fetch
    no_of_colors = 4
    # Fetch the RGB values of colours after clustering
    major_colors = fetch_cluster_centers(image_file, no_of_colors)
    # Print name of nearest available colour in CSS3 list
    for item in major_colors:
        print(fetch_nearest_color(item), tuple(item))
