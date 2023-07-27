from setuptools import setup, find_packages

setup(
    name="tangods_ads1015",
    version="0.0.1",
    description="Tango device server written in PyTango for an ADS1015 ADC using the i2c bus of a Raspberry Pi.",
    author="Martin Hennecke",
    author_email="hennecke@mbi-berlin.de",
    python_requires=">=3.6",
    entry_points={"console_scripts": ["ADS1015 = tangods_ads1015:main"]},
    license="MIT",
    packages=["tangods_ads1015"],
    install_requires=[
        "pytango",
        "ads1015",
    ],
    url="https://github.com/MBI-Div-b/pytango-ADS1015",
    keywords=[
        "tango device",
        "tango",
        "pytango",
        "ads1015",
    ],
)
