import setuptools

setuptools.setup(
    name="job-search",
    version="1.0.0",
    description="A lightweight Python client for the Lattice Job Search API.",
    long_description="A lightweight Python client for the Lattice Job Search API.",
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
    py_modules = ["jobsearch"],
    package_dir = {'': 'jobs'},
    tests_require=['pytest'],
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
