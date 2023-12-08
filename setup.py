from setuptools import setup
from setuptools import find_packages

long_description = '''
Pinnacle is an experimental library for solving differential equations
using neural networks. It uses TensorFlow and Jax as backends. 

Pinnacle has been tested on Python >=3.10
and is made available under the GNU GENERAL PUBLIC LICENSE Version 3
'''

setup(
    name='pinnacle',
    version='0.0.1',
    description='A light-weight library for solving differential equations using neural networks',
    long_description=long_description,
    author='Alex Bihlo',
    author_email='abihlo@mun.ca',
    license='GNU GPL',
    url='https://github.com/abihlo/pinnacle',
    install_requires=['numpy',
                      'scipy',
                      'tensorflow>=2.14',
                      ],
    extras_require={
          'visualize': ['matplotlib'],
          'tests': ['pytest',
                    'matplotlib',
                    ],
    },
    classifiers=[
          'Development Status :: Alpha',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU GPL',
          'Programming Language :: Python :: 3.10',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
    packages=find_packages(),
    include_package_data=True
)