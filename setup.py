from setuptools import setup

versionContext = {}
with open('pytest_forcefail/version.py') as f:
    exec(f.read(), versionContext)

setup(
    name='pytest-forcefail',
    description='py.test plugin to make the test failing regardless of pytest.mark.xfail',
    long_description=open("README.md").read(),
    version=versionContext['__version__'],
    url='https://github.com/cielavenir/pytest-forcefail',
    license='BSD',
    author='cielavenir',
    author_email='cielartisan@gmail.com',
    packages=['pytest_forcefail'],
    entry_points={'pytest11': ['forcefail = pytest_forcefail.pytest_forcefail']},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['pytest>=3.2'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ]
)
