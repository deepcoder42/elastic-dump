# Classification (U)

"""Program:  setup.py

    Description:  A setuptools based setup module.

"""

# Libraries and Global Variables

# Standard
import os
import setuptools

# Third-party

# Local
import version


# Read in long description from README file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f_hdlr:
    LONG_DESCRIPTION = f_hdlr.read()

setuptools.setup(
    name="Elastic_Dump",
    description="Elasticsearch database program for backing up databases.",
    author="deepcoder42",
    author_email="deepcoder42@gmail.com",
    url="https://github.com/deepcoder42/elastic-dump",
    version=version.__version__,
    platforms=["Linux"],
    long_description=LONG_DESCRIPTION,

    classifiers=[
        # Common Values:
        #  1 - Pre-Alpha
        #  2 - Alpha
        #  3 - Beta
        #  4 - Field
        #  5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Linux",
        "Operating System :: Linux :: Centos",
        "Operating System :: Linux :: Ubuntu",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Database",
        "Topic :: Database :: Elasticsearch",
        "Topic :: Database :: Elasticsearch :: 5.4.0",
        "Topic :: Database :: Elasticsearch :: 7.4.0",
        "Topic :: Database :: Elasticsearch :: 7.12.0"])
