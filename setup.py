from setuptools import setup, find_packages

setup(name='dummy download',
      version='1',
      description='Setting up setup.py',
      url='https://github.com/angelaho0504/CSC510_HW2b',
      author='Hrushabhsingh Chouhan, Hiral Bhanushali, Apoorva Chauhan, Angela Ho',
      author_email='hychouha@ncsu.edu',
      license='MIT',
      packages=find_packages(exclude=['js', 'node_modules', 'tests']),
      python_requires='>=3.5',
      install_requires=[
          'matplotlib',
          'numpy'
      ],
      include_package_data=True,
      zip_safe=False)