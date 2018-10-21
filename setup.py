import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "testing_test",
    # update version whenever you create a new release
    version = "{{version}}",
    author = "jrmerz",
    description = ("This is a test, this is only a test"),
    license = "MIT",
    keywords = "",
    url = "http://localhost:3000/package/2c51363e-c7f6-4102-b072-d7c1348d8871",
    packages=[
        'testing_test',
        'testing_test.main'
    ],
    package_data={
      'testing_test' : ['resources/*']
    },
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
)