import psutil
from .a import get_size
#  TODO disk.speed(partitionName)


class disk:
    @staticmethod
    def list():
        partitions = psutil.disk_partitions()
        devices = []
        for partition in partitions:
            devices.append(partition.device)
        return devices

    @staticmethod
    def list_all():
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

        return partitions
