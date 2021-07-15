import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="LatticeStockDataClient",
    version="0.0.5",

    description="An API for gathering RapidAPI stock info",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="ashkon@lattice.dev",

    package_dir={
        "": "./lib",
        "latticestockdataclient":"./lib/latticestockdataclient",
        "latticestockdataclient.util":"./lib/latticestockdataclient/util",
        "latticestockdataclient.data":"./lib/latticestockdataclient/data",
        "latticestockdataclient.data.stock":"./lib/latticestockdataclient/data/stock",
    },
    packages=setuptools.find_packages(where="lib"),

    install_requires=[
        'pytest',
        'requests',
        'cachetools',
        'bson',
        'pandas'
    ],
    tests_require=['pytest'],

    python_requires=">=3.9",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)