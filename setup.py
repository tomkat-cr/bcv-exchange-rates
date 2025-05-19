from setuptools import setup

setup(
    name="bcv-exchange-rates",
    version="1.1.0",
    author="Carlos J. Ramirez",
    author_email="tomkat_cr@yahoo.com",
    description="Mediabros Currency Exchange API series / Venezuelan Bolivares"
                " (BCV)",
    packages=["bcv_exchange_rates"],
    install_requires=[
        "beautifulsoup4",
        "requests",
    ],
    zip_safe=False
)
