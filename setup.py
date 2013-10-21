from distutils.core import setup


conf = dict(
    name='inf',
    version='1.1.0',
    description="Infinity",
    long_description="\n".join(list(open("README"))[2:]).strip(),
    classifiers=[
        "Development Status :: 6 - Mature",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    keywords='inf infinity',
    author='Peter Waller',
    author_email='p@pwaller.net',
    url='http://github.com/pwaller/inf',
    py_modules=["inf"],
)

if __name__ == '__main__':
    setup(**conf)
