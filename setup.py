from setuptools import setup, find_packages


def readme():
    with open(r"README.md") as f:
        README = f.read()
    return README


with open("requirements.txt", "r") as f:
    requirements = f.read()
    setup(
        name="pygita",
        packages=find_packages(),
        version="2.0.0",
        license="MIT",
        description="""pygita is a wrapper
          of bhagavadgita.io api for Python 3""",
        author="Shubhendra Kushwaha",
        author_email="shubhendrakushwaha94@gmail.com",
        url="https://github.com/TheShubhendra/pygita",
        keywords=[
            "Gita",
            "ShrimadBhagwatGita",
            "Verse",
            "Literature",
            "Mythology",
            "Hinduism",
        ],
        install_requires=requirements,
        include_package_data=True,
        long_description=readme(),
        long_description_content_type="text/markdown",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Religion",
            "Topic :: Software Development :: Build Tools",
            "Topic :: Religion",
            "Topic :: Sociology :: History",
            "Topic :: Software Development",
            "License :: OSI Approved :: MIT License",
            "License :: Free For Educational Use",
            "License :: Free For Home Use",
            "Natural Language :: English",
            "Natural Language :: Hindi",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        python_requires=">=3.0",
    )
