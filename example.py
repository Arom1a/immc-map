from PIL import Image
from read_map import *
Image.MAX_IMAGE_PIXELS = None

get_region(["40N", "30N", "110E", "120E"], "landscan-global-2022-colorized.tif").show()
    # The first parameter is in format of a list in sequence of [latitude_1, latitude_2, longitude_1, longitude_2]
    # e.g.: coordinate = ["40N", "30N", "110E", "120E"]
    # This method will return a PIL.Image.Image object

print(get_point(["35N", "115E"], "landscan-global-2022-colorized.tif"))
    # The first parameter is in format of list in sequence of [latitude, longitude]
    # e.g.: coordinate = ["35N", "115E"]
    # This method will return the color infomation of the coordinate
