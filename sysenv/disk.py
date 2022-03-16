import psutil
import os
import sys
from random import shuffle
from .a import get_size

try:
    from time import perf_counter as time
except ImportError:
    if sys.platform[:3] == 'win':
        from time import clock as time
    else:
        from time import time


class disk:
    #  https://github.com/thodnev/MonkeyTest
    @staticmethod
    def __write_test(location, block_size, blocks_count):
        f = os.open(f'{location}\\test00001x.txt', os.O_CREAT | os.O_WRONLY, 0o777)

        took = []
        for i in range(blocks_count):
            buff = os.urandom(block_size)
            start = time()
            os.write(f, buff)
            os.fsync(f)  # force write to disk
            t = time() - start
            took.append(t)

        os.close(f)
        return took

    #  https://github.com/thodnev/MonkeyTest
    @staticmethod
    def __read_test(location, block_size, blocks_count):
        f = os.open(f'{location}\\test00001x.txt', os.O_RDONLY, 0o777)
        # generate random read positions
        offsets = list(range(0, blocks_count * block_size, block_size))
        shuffle(offsets)

        took = []
        for i, offset in enumerate(offsets, 1):
            start = time()
            os.lseek(f, offset, os.SEEK_SET)  # set position
            buff = os.read(f, block_size)  # read from position
            t = time() - start
            if not buff:
                break  # if EOF reached
            took.append(t)

        os.close(f)
        return took

    @staticmethod
    def speed(location=f"{os.getcwd()}", write_mb=128, write_block_kb=1024, read_block_b=512):
        """
        Get disk speed in MB format
        :param location:
        :param write_mb:
        :param write_block_kb:
        :param read_block_b:
        :return: Dictionary
        """
        write_mb = write_mb
        write_block_kb = write_block_kb
        read_block_b = read_block_b
        wr_blocks = int(write_mb * 1024 / write_block_kb)
        rd_blocks = int(write_mb * 1024 * 1024 / read_block_b)
        write_results = disk.__write_test(location, 1024 * write_block_kb, wr_blocks)
        read_results = disk.__read_test(location, read_block_b, rd_blocks)
        os.remove(f"{location}\\test00001x.txt")
        return {'read': f'{(write_mb / sum(read_results)):.2f}',
                'write': f'{write_mb / sum(write_results):.2f}',
                'max_read': f'{read_block_b / (1024 * 1024 * min(read_results)):.2f}',
                'min_read': f'{read_block_b / (1024 * 1024 * max(read_results)):.2f}',
                'max_write': f'{write_block_kb / (1024 * min(write_results)):.2f}',
                'min_write': f'{write_block_kb / (1024 * max(write_results)):.2f}'
                }

    @staticmethod
    def list():
        """List devices"""
        partitions = psutil.disk_partitions()
        devices = []
        for partition in partitions:
            devices.append(partition.device)
        return devices

    @staticmethod
    def list_all(device=None):
        """
        List partition information
        :param device:
        :return: dict
        """
        raw_partitions = psutil.disk_partitions()
        partitions = []
        for partition in raw_partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            values = ['device', 'mountpoint', 'fstype', 'opts', 'maxfile', 'maxpath']
            dict_partition = {}
            index = 0
            for data in partition:
                dict_partition.update({f'{values[index]}': f'{data}'})
                index += 1
            dict_partition.update({'size': f'{get_size(usage.total)}',
                                   'used': f'{get_size(usage.used)}',
                                   'used_perc': f'{usage.percent}',
                                   'free': f'{get_size(usage.free)}'
                                   })
            partitions.append(dict_partition)

        if device:
            for partition in partitions:
                if partition['device'] == device:
                    return partition
            return None

        return partitions
