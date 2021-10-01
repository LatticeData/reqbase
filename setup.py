import setuptools

setuptools.setup(
    name="job-search",
    version="1.0.0",
    description="The comprehensive job postings and requisitions aggregator.",
    long_description="The comprehensive job search API, powered by Indeed, Simply Hired, Lawjobs.",
    long_description_content_type="text/markdown",
    url="https://lattice.dev/products/job-search",
    project_urls={
        "Source": "https://github.com/LatticeData/job-search",
        "Documentation" : "https://github.com/LatticeData/job-search#readme",
        "Bug Reports" : "https://github.com/LatticeData/job-search/issues",
        "Get your key" : "https://rapidapi.com/lattice-data-lattice-data-default/api/job-search4/",
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
