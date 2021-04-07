import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DeepLego",
    version="0.0.1",
    author="Koosha Tham",
    author_email="kooshi.ml@gmail.com",
    description="Connect deep learning breakthroughs together like Lego pieces and build a new breakthrough!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/koosha-t/DeepLego",
    project_urls={
        "Bug Tracker": "https://github.com/koosha-t/DeepLego/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)