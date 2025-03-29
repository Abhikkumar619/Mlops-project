import setuptools

import setuptools

__version__="0.0.0"
AUTHOR_NAME="Abhikkumar619"
AUTHOR_EMAIL="abisheky194@gmail.com"
REPO_NAME="MLOPS-PROJECT"
SRC_REPO="src"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_NAME,
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)