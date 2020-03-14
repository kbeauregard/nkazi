import setuptools
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="nkazi",
    version="0.0.1",
    author="Kyle Beauregard",
    author_email="kylembeauregard@gmail.com",
    description="Python feature flag throttling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kbeauregard/{{ project_name }}",
    license="MIT",
    packages=setuptools.find_packages(
        include=["nkazi*",], exclude=["nkazi/tests"]
    ),
    py_modules=["nkazi.__init__",],
    keywords=["throttle", "feature", "flag"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
