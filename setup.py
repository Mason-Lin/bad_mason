from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='bad_mason',
    version='1.0.1',
    author='Bad Mason',
    author_email='pizza.0117@gmail.com',
    description='fake get useful data but do something evil',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Mason-Lin/bad_mason',
    packages=find_packages(),
    package_data={'bad_mason': ['datahelper.zip']},
    incude_package_data=True,
    install_requires=['requires'],
    entry_points={
        'console_scripts': [
            'bad_mason=bad_mason:main'
        ],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
