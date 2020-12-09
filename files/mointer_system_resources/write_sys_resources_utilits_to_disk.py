#!/usr/bin/env python3

from os import path

from system_resources_utilis import (
                                        cpu_percentage,
                                        disk_availiable_space_percentage,
                                        free_memory_percentage
                                    )
from write_csvfile import write_value

dir_path = '/opt/'

write_value(path.join(dir_path, 'CPU.csv'), cpu_percentage())
write_value(path.join(dir_path, 'MEM.csv'), free_memory_percentage())
write_value(path.join(dir_path, 'DISK.csv'), disk_availiable_space_percentage())
