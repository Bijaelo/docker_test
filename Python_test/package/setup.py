import setuptools

p = setuptools.find_packages()
setuptools.setup(
    name = "my_package", # Replace with your own username
    version = "1.0.0",
    author = "test-author",
    author_email = "test@test.test",
    description = "this description could be better",
    long_description = "#This is not a very long description",
    long_description_content_type = "text/markdown",
    packages = p,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)