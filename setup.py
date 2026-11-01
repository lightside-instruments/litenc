from pathlib import Path

from setuptools import setup

ROOT = Path(__file__).resolve().parent

setup(name='litenc',
      version='1.9',
      install_requires=["paramiko", "lxml"],
      description="Lite NETCONF session framer",
      author="Vladimir Vassilev",
      author_email="vladimir@lightside-instruments.com",
      url="https://github.com/vlvassilev/litenc",
      packages=["litenc", "litenc_lxml"],
      license="BSD-3-Clause",
      license_files=["LICENSE", "COPYRIGHT"],
      long_description=(ROOT / "README.pypi.md").read_text(encoding="utf-8"),
      long_description_content_type="text/markdown",
      python_requires=">=3.7",
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3 :: Only",
          "Topic :: System :: Networking",
      ],
      platforms=["Posix; OS X; Windows"],
      scripts=['scripts/ncget']
      )
