from distutils.core import setup

setup(
    name='yoshix',
    version='0.5.0',
    packages=['yoshix'],
    url='https://github.com/THeK3nger/yoshix',
    license='MIT',
    author='Davide Aversa',
    author_email='thek3nger@gmail.com',
    description='A library for collecting and processing experimental data and benchmarks results.',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
