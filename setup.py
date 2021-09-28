import setuptools

setuptools.setup(
    name="lattice-stocks-data",
    version="1.1.0",
    description="Comprehensive stock market data sourced from Yahoo Finance and a variety of other sources in one clean package.",
    long_description="Comprehensive stock market data sourced from Yahoo Finance and a variety of other sources in one clean package. Provided data types include basic company information, real-time price information, financial statements, news coverage, stock similarity metrics, valuation metrics, and economic indicators.",
    long_description_content_type="text/markdown",
    url="https://lattice.dev/products/stock-market-data",
    project_urls={
        "Source": "https://github.com/LatticeData/lattice-stocks-data",
        "Documentation" : "https://github.com/LatticeData/lattice-stocks-data/blob/master/README.md#Usage",
        "Bug Reports" : "https://github.com/LatticeData/lattice-stocks-data/issues",
        "Get your key" : "https://rapidapi.com/lattice-data-lattice-data-default/api/stock-market-data/",
    },
    author='Lattice',
    author_email="ashkon@lattice.dev",
    packages=setuptools.find_packages(exclude=['tests', '.circleci']),
    tests_require=['pytest'],
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
