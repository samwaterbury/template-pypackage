from distutils.core import setup

with open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="cookiecutter-pypackage",
    version="0.1.0",
    author="Sam Waterbury",
    author_email="samwaterbury1@gmail.com",
    url="https://github.com/samwaterbury/template-pypackage",
    description="Lightweight Python package template using my preferred configuration for new projects.",
    long_description=LONG_DESCRIPTION,
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    zip_safe=True,
)
