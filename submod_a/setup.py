from setuptools import setup, find_namespace_packages


setup(
    name="submod-a",
    version="0.0.1",
    description="Submodule A under namespace package subpackages",
    url="https://usva-gheprod01.bose.com/BoseGHE/atlas-backend-dataio",
    author="Spenser Haddad",
    author_email="spenser.haddad@gmail.com",
    packages=find_namespace_packages(),
    python_requires=">=3.7",
)
