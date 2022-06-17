from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='ttlecs',
    version=__version__,
    description='create ttl ecs on cloud',
    long_description=long_description,
    url='http://git.souche.com/datacenter/dayu',
    download_url='http://git.souche.com/datacenter/dayu/tarball/' + __version__,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    zip_safe=False,
    author='shenyubao',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='ssybb1988@gmail.com',
    entry_points={
        'console_scripts': {
            'ttlecs = ttlecs.ttlecs:execute'
        },
    },
)