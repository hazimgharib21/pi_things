#!/usr/bin/python3

import psutil
from psutil._common import bytes2human
import time

try:
    while True:
        time.sleep(1)

        # Collect Data
        # CPU
        cpu_usage = psutil.cpu_percent(interval=None, percpu=False)
        cpu_freq_cur = psutil.cpu_freq().current
        cpu_freq_min = psutil.cpu_freq().min
        cpu_freq_max = psutil.cpu_freq().max
        # Memory
        memory_usage = psutil.virtual_memory().percent
        memory_avail = bytes2human(psutil.virtual_memory().available)
        memory_total = bytes2human(psutil.virtual_memory().total)
        memory_used = bytes2human(psutil.virtual_memory().used)
        # Swap
        swap_usage = psutil.swap_memory().percent
        swap_total = bytes2human(psutil.swap_memory().total)
        swap_free = bytes2human(psutil.swap_memory().free)
        swap_used = bytes2human(psutil.swap_memory().used)
        # Disk Usage

        # Disk Partition
        disk_data = psutil.disk_partitions()

        # Network
        network = psutil.net_io_counters(pernic=True)

        # Print
        print("CPU Usage : " + str(cpu_usage) + "%")
        print("CPU Frequency")
        print("\tCurrent : " + str(cpu_freq_cur))
        print("\tMin : " + str(cpu_freq_min))
        print("\tMax : " + str(cpu_freq_max))
        print("Memory")
        print("\tUsage : " + str(memory_usage) + "%")
        print("\tUsed : " + str(memory_used))
        print("\tAvailable : " + str(memory_avail))
        print("\tTotal : " + str(memory_total))
        print("Swap")
        print("\tUsage :" + str(swap_usage) + "%")
        print("\tUsed : " + str(swap_used))
        print("\tFree : " + str(swap_free))
        print("\tTotal : " + str(swap_total))
        print("Disk Usage")
        print("Disk Partition")
        for data in disk_data:
            print(data.device)
            print("\tMount : " + str(data.mountpoint))
            print("\tType : " + str(data.fstype))
            if data.opts == 'cdrom' or data.fstype == '':
                continue
            disk_usage = psutil.disk_usage(data.mountpoint)
            print("\tUsage : " + str(disk_usage.percent))
            print("\tUsed : " + str(bytes2human(disk_usage.used)))
            print("\tFree : " + str(bytes2human(disk_usage.free)))
            print("\tTotal : " + str(bytes2human(disk_usage.total)))
        print("Network")
        for item in network:
            print(item)
            print("\tByte Sent : " + str(bytes2human(network[item].bytes_sent)))
            print("\tByte Receive : " + str(bytes2human(network[item].bytes_recv)))
        print()

except Exception as error:
    print(error)
