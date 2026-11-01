# Publishing litenc 1.9

Run these commands from this repository's root:

```sh
python3 -m venv .venv-release
.venv-release/bin/python -m pip install -r requirements-release.txt
.venv-release/bin/python -m build
.venv-release/bin/python -m twine check --strict dist/*
```

Both the source archive and wheel use BSD-3-Clause. Inspect the artifacts
before uploading. With a PyPI account authorized for this project, upload:

```sh
.venv-release/bin/python -m twine upload dist/*
```

Twine prompts for credentials. Use `__token__` as the username and your PyPI
API token as the password. Nothing is uploaded by the build commands.
For a TestPyPI rehearsal, add `--repository testpypi` to the upload command.

Verify in a fresh environment:

```sh
python -m pip install litenc==1.9
python -m pip check
```

Publish litenc 1.9 before tntapi 1.9, which depends on it.

## Debian packages

The upstream package version is 1.9 and the Debian package version is 1.9-1.
Install the build tools on a Debian 13 host:

```sh
sudo apt install debhelper dh-sequence-python3 pybuild-plugin-pyproject python3-all python3-setuptools python3-wheel
dpkg-buildpackage -us -uc -b
lintian ../litenc_1.9-1_*.changes
```

The build creates `../python3-litenc_1.9-1_all.deb`. Build both projects,
then install their packages together:

```sh
sudo apt install ./python3-litenc_1.9-1_all.deb ./python3-tntapi_1.9-1_all.deb
```
