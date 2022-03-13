import platform
import socket
import uuid
import psutil
import wmi
import re


def os():
    """Operating System"""
    return platform.system()


def arch():
    """System architecture"""
    return platform.machine()


def host():
    """Name of host"""
    return socket.gethostname()


def ipv4():
    """v4 address"""
    return socket.gethostbyname(socket.gethostname())


def ipv6():
    """v6 address"""
    return socket.AF_INET6


def mac():
    """NIC Identifier"""
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))


def cpu():
    """Processor Manufacturer"""
    return platform.processor()


def gpu():
    computer = wmi.WMI()
    gpu_info = computer.Win32_VideoController()[0].name
    return gpu_info


def ram():
    """Memory in GB format"""
    return str(round(psutil.virtual_memory().total / (1024.0 ** 3)))
