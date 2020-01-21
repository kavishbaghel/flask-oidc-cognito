# Release Checklist

0. Ensure we're on the ```master``` branch.
0. Ensure that the ```wheel``` package is installed in the venv.
1. Build locally```python setup.py sdist bdist_wheel```.
2. Run ```tox``` to ensure that the package builds and can be used with the Python 3.x env.
3. Update the ```CHANGELOG.rst```.
4. Run ```bumpversion [part]``` where part is either major, minor or patch.
5. Push tags: ```git push origin master --tags```.
6. Wait for Travis CI to publish package.
