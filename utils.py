import random
from typing import Union
from os import path as os_path, rename as os_rename
from PIL.Image import open as Image_open

def getImageFile(file_name):
    img = Image_open(os_path.join(os_path.dirname(__file__), "img", file_name))
    return img

def getKeyByValue(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def callFunctionIfCallable(function, *args):
    if callable(function) is True:
        function(*args)

def isEven(number):
    return number % 2 == 0

def makeEven(number, minus:bool=False):
    if minus is True:
        return number if isEven(number) else number - 1
    return number if isEven(number) else number + 1

def generatePercentageStringsList(start:int, end:int, step:int):
    strings = []
    for percent in range(start, end + 1, step):
        strings.append(f"{percent}%")
    return strings

def intToPctStr(value:int):
    return f"{value}%"

def floatToPctStr(value:float):
    return f"{int(value*100)}%"

def strPctToInt(value:str):
    return int(value.replace("%", ""))

def isUniqueStrings(unique_strings:Union[str, list], input_string:str, require=False):
    import re
    if isinstance(unique_strings, str):
        unique_strings = [unique_strings]
    patterns = [re.escape(s) for s in unique_strings]

    counts = [len(re.findall(pattern, input_string)) for pattern in patterns]

    if require is True:
        # If require is True, unique_strings must appear once
        return all(count == 1 for count in counts) and counts.count(1) == 2
    else:
        # If require is False, check if unique strings are used exactly once
        return all(count == 1 for count in counts)

# path先のweightフォルダがある場合にはそのフォルダ名をweightsに変更する
def renameWeightFolder(path):
    weight_path = os_path.join(path, "weight")
    if os_path.exists(weight_path):
        os_rename(weight_path, os_path.join(path, "weights"))

def splitList(lst:list, split_count:int, to_shuffle:bool=False):
    if to_shuffle is True:
        random.shuffle(lst)

    split_lists = []
    for i in range(0, len(lst), split_count):
        sub_list = lst[i:i+split_count]
        split_lists.append(sub_list)
    return split_lists