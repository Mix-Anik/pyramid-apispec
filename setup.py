from setuptools import find_packages
from setuptools import setup

REQUIRES = [
    "marshmallow>=3.0.0",
    "webargs>=6.0.0",
    "apispec>=4.0.0",
]

TEST_REQUIRES = ["pyramid>=1.3.0", "pytest", "pytest-cov", "WebTest", "prospector"]

DEV_REQUIRES = ["invoke", "sphinx", "pydata-sphinx-theme", "sphinx-issues", "wheel", "twine", "black[d]"]


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="pyramid-apispec",
    version="1.0.0-alpha",
    description="Build and document REST APIs with Pyramid and apispec",
    long_description=read("README.rst"),
    author="Mix-Anik, Joshua Carp",
    url="https://github.com/Mix-Anik/pyramid-apispec",
    packages=find_packages(exclude=("test*",)),
    package_dir={"pyramid_apispec": "pyramid_apispec"},
    include_package_data=True,
    install_requires=REQUIRES,
    extras_require={"dev": TEST_REQUIRES + DEV_REQUIRES, "testing": TEST_REQUIRES},
    license="MIT",
    zip_safe=False,
    keywords="pyramid marshmallow webargs apispec",
    python_requires=">=3.7",
    test_suite="tests",
    project_urls={
        "Bug Reports": "https://github.com/Mix-Anik/pyramid-apispec/issues",
        # 'Changelog': 'https://pyramid-apispec.readthedocs.io/en/latest/changelog.html',
    },
)
