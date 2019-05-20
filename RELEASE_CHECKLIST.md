# Release Checklist

0. Ensure we're on the ```master``` branch.
1. Build locally```python setup.py sdist bdist_wheel```.
2. Run ```tox``` to ensure that the package builds and can be used with the Python 3.x env.
3. Bump version number in ```VERSION``` and commit.
4. Tag the local git repository: ```git tag x.y.z```.
5. Push tags: ```git push origin master --tags```.
6. Wait for Travis CI to publish package.
