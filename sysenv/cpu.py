import psutil
cpufreq = psutil.cpu_freq()


class cpu:
    @staticmethod
    def cores():
        """Physical Cores"""
        return psutil.cpu_count(logical=False)

    @staticmethod
    def threads():
        """All Cores"""
        return psutil.cpu_count(logical=True)

    @staticmethod
    def freq_max():
        """Max Frequency"""
        return cpufreq.max

    @staticmethod
    def freq_min():
        """Minimum Frequency"""
        return cpufreq.min

    @staticmethod
    def freq_curr():
        """Current Frequency"""
        return cpufreq.current

    @staticmethod
    def used():
        """Percentage of CPU being used (Takes 1 second to complete)"""
        return psutil.cpu_percent(interval=1)

    @staticmethod
    def used_cores():
        """Percentage of each core's usage"""
        cores_usage = {}
        for number, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            number += 1
            cores_usage[number] = perc
        return cores_usage
