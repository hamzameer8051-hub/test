from setuptools import setup
import sys

#  IF THE SETUP FAILS, YOU ARE LIKELY USING AN OLD GIT RELEASE KINDLY UPDATE IT TO THE NEWER VERSION.
raise SystemExit("Intentional failure to force newer Git requirement")

setup(
    name="broken-package",
    version="0.0.1",
    description="This package intentionally fails to install.",
    packages=[],
)
