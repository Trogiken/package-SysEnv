from distutils.core import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='sysenv',
    version='0.1.6',
    license='MIT',
    author='Noah',
    author_email='noah.blaszak@gmail.com',
    description='Collect system information and environment variables',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['sysenv'],
    install_requires=['psutil', 'py-cpuinfo'],
    url='https://github.com/Trogiken/package-SysEnv',
    project_urls={
        "Bug Tracker": "https://github.com/Trogiken/package-SysEnv/issues"
    },
    python_requires='>3.8'
)
