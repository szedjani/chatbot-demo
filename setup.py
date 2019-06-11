import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chatbot_demo",
    version="0.0.5",
    author="Janos Szedelenyi",
    author_email="janos.szedelenyi@gmail.com",
    description="A small demonstration of a chatbot engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/szedjani/chatbot-demo",
    packages=setuptools.find_packages(),
    install_requires=[
        'rasa',
        'langdetect'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
