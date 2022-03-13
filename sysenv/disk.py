import psutil


class disk:
    @staticmethod
    def list():
        partitions = psutil.disk_partitions()
        devices = []
        for partition in partitions:
            devices.append(partition.device)
        return devices

    @staticmethod
    def list_all():  # TODO (Line 97 of test32) Add [size, used, free, percentage] to each partition
        partitions = psutil.disk_partitions()
        print(partitions)
        print()
        for partition in partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
        return partitions
