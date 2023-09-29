import re

from datetime import datetime

def findTech(filetxt):
    techniks = list()
    pattern = r'\d{4}'
    with open(filetxt, "r", encoding="UTF-8") as file:
        for item in file:
            found_date = ''.join(re.findall(pattern, item))
            if ((datetime.now().year) - int(found_date) > 20):
                techniks.append(item)

    for item in techniks:
        print(item)

findTech("info.txt")