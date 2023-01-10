from setuptools import find_packages, setup

setup(
    name="shared_asset_package",
    packages = find_packages(),
    install_requires=[
        "dagster"
    ]
)