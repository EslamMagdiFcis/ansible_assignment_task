#!/usr/bin/env python3

import csv
from datetime import datetime


def write_value(file_path, value):

    with open(file_path, mode='a+') as file:

        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([datetime.now(), value])
