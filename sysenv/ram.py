import psutil
from a import get_size

svmem = psutil.virtual_memory()


class ram:
    @staticmethod
    def size():
        """Total memory in GB format"""
        return get_size(svmem.total)

    @staticmethod
    def open():
        """Available memory in GB format"""
        return get_size(svmem.available)

    @staticmethod
    def used():
        """Used memory in GB format"""
        return get_size(svmem.used)

    @staticmethod
    def perc_used():
        """Used memory in percentage format"""
        return svmem.percent
