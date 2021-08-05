import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="automated-problem-generation-lib",
    author="Daniel Kosc",
    author_email="485652@mail.muni.cz",
    description="Random generator of selected variables",
    install_requires=['pyYAML', 'better_profanity'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.fi.muni.cz/kypolab/theses/kosc-automated-problem-generation",
    packages=setuptools.find_namespace_packages(include=['generator'], exclude=['tests']),
    package_dir={'generator': './generator'},
    package_data={'generator': ['./*.txt', './*.yml']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
