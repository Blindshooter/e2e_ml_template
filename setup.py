from setuptools import setup, find_packages

def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()[:-1]


setup(name = "mlproject",
        version = "0.1",
        packages = find_packages(),
        install_requires = get_requirements(),)