from setuptools import setup

setup(
    name="bcv-exchange-rates",
    version="1.0.0",
    author="Carlos J. Ramirez",
    author_email="cramirez@mediabros.com",
    description="A python module to get exchange rates from bcv.org.ve",
    packages=["bcv-exchange-rates"],
    install_requires=["requests", "beautifulsoup4", "a2wsgi"],
    zip_safe=False
)
