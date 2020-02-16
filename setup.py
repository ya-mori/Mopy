import os

from setuptools import setup, Command, find_packages

"""setup.py best practice:
https://github.com/kennethreitz/setup.py/blob/master/setup.py
"""

NAME = "mopy"

REQUIRED = []

EXTRAS = dict(dev=["black==19.10b0.*", "coverage==4.5.*", "mypy==0.740.*"])


class SimpleCommand(Command):
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print(f"\033[1m{s}\033[0m")

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        raise NotImplementedError


class TestCommand(SimpleCommand):
    def run(self):
        self.status("Running formatter...")
        os.system("black . -l 120")
        self.status("Running type checker...")
        os.system(f"mypy {NAME}")
        self.status("Running test...")
        os.system(f"coverage run --source={NAME} -m unittest discover")
        os.system("rm -f .coverage.*")


setup(
    name=NAME,
    description="Simple tool to create mock data",
    url="",
    author="yohei.moriya",
    author_email="ppap.yohei.moriya@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    cmdclass=dict(test=TestCommand),
)
