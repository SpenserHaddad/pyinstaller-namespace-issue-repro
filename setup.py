from setuptools import setup, find_packages

setup(
    name="pyi_ns",
    version="0.0.1",
    description="Test PyInstaller Namespaces",
    packages=find_packages(include=["pyi_ns*"]),
    python_requires=">=3.7",
)
