import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="translator_client",
    version="0.0.2",
    author="erezsc",
    author_email="erezsc@rnd-hub.com",
    description="a wrapper package to use translator docker ('Miriam')",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    py_modules=["translator_client"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests ~= 2.18",
    ]
)
