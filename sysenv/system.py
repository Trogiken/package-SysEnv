import platform
import socket
import uuid
import cpuinfo
import re


class system:
    @staticmethod
    def os():
        """Operating System"""
        return platform.system()

    @staticmethod
    def release():
        """OS Release"""
        return platform.release()

    @staticmethod
    def version():
        """OS Version"""
        return platform.version()

    @staticmethod
    def arch():
        """System architecture"""
        return platform.machine()

    @staticmethod
    def host():
        """Name of host"""
        return socket.gethostname()

    @staticmethod
    def ipv4():
        """v4 address"""
        return socket.gethostbyname(socket.gethostname())

    @staticmethod
    def ipv6():
        """v6 address"""
        result = socket.getaddrinfo(system.host(), 0, socket.AF_INET6)
        return result[0][4][0]

    @staticmethod
    def mac():
        """NIC Identifier"""
        return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

    @staticmethod
    def cpu_manu():
        """Processor Manufacturer"""
        return platform.processor()

    @staticmethod
    def cpu_info():
        """Processor Information"""
        return cpuinfo.get_cpu_info()['brand_raw']
