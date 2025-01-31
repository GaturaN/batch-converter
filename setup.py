from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in batch_converter/__init__.py
from batch_converter import __version__ as version

setup(
	name="batch_converter",
	version=version,
	description="Batch",
	author="dsa",
	author_email="dsa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
