from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='extractmodel',
  version='0.1',
  description='Extract model function',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Semih Yumusak',
  author_email='semihyumusak@yahoo.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='model', 
  packages=find_packages(),
  install_requires=[''] 
)