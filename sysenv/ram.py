import psutil
from .a import get_size

svmem = psutil.virtual_memory()


class ram:
    @staticmethod
    def size():
        """Total memory in GB format"""
        return get_size(svmem.total)

    @staticmethod
    def free():
        """Available memory in GB format"""
        return get_size(svmem.available)

    @staticmethod
    def used():
        """Used memory in GB format"""
        return get_size(svmem.used)

    @staticmethod
    def used_perc():
        """Used memory in percentage format"""
        return svmem.percent
