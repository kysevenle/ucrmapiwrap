from setuptools import setup, find_packages


setup(name='UCRMApiWrap',
      version='0.1.0',
      description='Wrapper around UCRM api for easy use',
      author='Kyle Petersen',
      url='https://github.com/kysevenle/ucrmapiwrap',
      packages=['ucrmapiwrap', ],
      package_dir={'ucrmapiwrap': 'ucrmapiwrap'},
      include_package_data=True,)
