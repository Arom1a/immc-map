from PIL import Image


def get_region(coordinate, file_name):
    # In format of a list in sequence of [latitude_1, latitude_2, longitude_1, longitude_2]
    # e.g.: coordinate = ["40N", "30N", "110E", "120E"]
    # This method will return a PIL.Image.Image object

    coordinate_tmp = [0, 0, 0, 0]
    for i in range(2):
        if coordinate[i][-1] == "N":
            coordinate_tmp[i] = 0.5 - float(coordinate[i][:-1]) / 180
        elif coordinate[i][-1] == "S":
            coordinate_tmp[i] = 0.5 + float(coordinate[i][:-1]) / 180
        else:
            coordinate_tmp[i] = 0.5
    for i in range(2):
        i += 2
        if coordinate[i][-1] == "W":
            coordinate_tmp[i] = 17 / 36 - float(coordinate[i][:-1]) / 360
            if coordinate_tmp[i] < 1:
                coordinate_tmp[i] += 1
        elif coordinate[i][-1] == "E":
            coordinate_tmp[i] = 17 / 36 + float(coordinate[i][:-1]) / 360
        else:
            coordinate_tmp[i] = 17 / 36

    rectangle = [0, 0, 0, 0]

    with Image.open(file_name) as img:
        rectangle[0] = min(coordinate_tmp[0], coordinate_tmp[1]) * img.width
        rectangle[1] = min(coordinate_tmp[2], coordinate_tmp[3]) * img.height
        rectangle[2] = max(coordinate_tmp[0], coordinate_tmp[1]) * img.width
        rectangle[3] = max(coordinate_tmp[2], coordinate_tmp[3]) * img.height

        return img.crop(rectangle)


def get_point(coordinate, file_name):
    # In format of list in sequence of [latitude, longitude]
    # e.g.: coordinate = ["35N", "115E"]
    # This method will return the color infomation of the coordinate

    coordinate_tmp = [0, 0]
    for i in range(1):
        if coordinate[i][-1] == "N":
            coordinate_tmp[i] = 0.5 - float(coordinate[i][:-1]) / 180
        elif coordinate[i][-1] == "S":
            coordinate_tmp[i] = 0.5 + float(coordinate[i][:-1]) / 180
        else:
            coordinate_tmp[i] = 0.5
    for i in range(1):
        i += 1
        if coordinate[i][-1] == "W":
            coordinate_tmp[i] = 17 / 36 - float(coordinate[i][:-1]) / 360
            if coordinate_tmp[i] < 1:
                coordinate_tmp[i] += 1
        elif coordinate[i][-1] == "E":
            coordinate_tmp[i] = 17 / 36 + float(coordinate[i][:-1]) / 360
        else:
            coordinate_tmp[i] = 17 / 36

    with Image.open(file_name) as img:
        # coordinate_debug = [coordinate_tmp[0] + 3500, coordinate_tmp[1] + 3507, coordinate_tmp[0] + 3501, coordinate_tmp[1] + 3508]
        # This is for testing, with coordinate = ["35N", "115E"]
        # coordinate_tmp[0] += 3500
        # coordinate_tmp[1] += 3508

        return img.getpixel(coordinate_tmp)
