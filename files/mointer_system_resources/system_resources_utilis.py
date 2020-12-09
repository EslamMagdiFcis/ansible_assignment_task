#!/usr/bin/env python3

import sys
import os
import psutil

def disk_availiable_space_percentage():

    total = 0
    free = 0

    for part in psutil.disk_partitions(all=False):

        if os.name == 'nt':

            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue

        usage = psutil.disk_usage(part.mountpoint)
        total += usage.total
        free += usage.free

    
    disk_available_space_percentage = (free / total) * 100

    return round(disk_available_space_percentage, 2)

def free_memory_percentage():
    virtual_memory = psutil.virtual_memory()
    
    free_memory_percentage = (virtual_memory.free / virtual_memory.total) * 100

    return round(free_memory_percentage, 2)

def cpu_percentage():
    return psutil.cpu_percent()
