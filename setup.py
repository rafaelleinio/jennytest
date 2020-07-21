from setuptools import find_packages, setup

__package_name__ = "jennytest"
__version__ = "0.2.9"
__repository_url__ = "https://github.com/rafaelleinio/jennytest"

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name=__package_name__,
    description="Data quality and profiling tool powered by Apache Spark.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=__version__,
    url=__repository_url__,
    packages=find_packages(
        exclude=["tests", "pipenv", "env", "venv", "htmlcov", ".pytest_cache"]
    ),
    license="MIT",
    author="Rafael Leinio",
    keywords="apache-spark pyspark data quality profiling",
    install_requires=requirements,
)
