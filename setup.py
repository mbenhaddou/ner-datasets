import setuptools

from entities_data.version import __version__

with open('README.rst', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="ner-dataset",
    version=__version__,
    author="Mohamed Ben Haddou",
    author_email="mbenhaddou@mentis.io",
    include_package_data=True,
    description="Various Ner dataset for multiple domains and languages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    url="",
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.json', '*.npy', '*.db'],
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        'Development Status :: 4 - Beta',
    ],
    python_requires='>=3.0',
)
