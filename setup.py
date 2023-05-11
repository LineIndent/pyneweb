from setuptools import setup

setup(
    name="pyneweb",
    version="0.5.1",
    author="S. Ahmad P. Hakimi",
    author_email="pourhakimi@pm.me",
    description="Web Boilerplate for Pynecone",
    long_description="Pyneweb is a Python web boilerplate project designed to provide a solid foundation for building web applications with Python and Pynecone. The project comes pre-configured with a range of tools and features to make it easy for developers to get started building their web applications, without the need to spend time setting up infrastructure or configuration.",
    long_description_content_type="text/markdown",
    url="https://github.com/LineIndent/pyneweb",
    packages=["logic"],
    install_requires=["click==8.1.3", "pynecone==0.1.28", "PyYAML==6.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["pyneweb-init=logic.cli:init"],
    },
    keywords=["python web template", "web application", "development"],
)
