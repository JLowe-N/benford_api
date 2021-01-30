import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="benford-api-JLowen", # Replace with your own username
    version="0.0.1",
    author="Justin Lowen",
    author_email="Justin.G.Lowen@gmail.com",
    description="Tornado based API to visualize Benford's Law",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JLowe-N/benford_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)