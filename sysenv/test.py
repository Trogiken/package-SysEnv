import platform
import socket
import uuid
import re


def os():
    return platform.system()


def arch():
    return platform.machine()


def host():
    return socket.gethostname()


def ipv4():
    return socket.gethostbyname(socket.gethostname())


def mac():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))


def cpu():
    return platform.processor()
