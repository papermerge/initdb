import setuptools

setuptools.setup(
    name="initdb",
    version="0.1.0",
    description="Small package that creates a user"
    " and database owned by that user.",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)
