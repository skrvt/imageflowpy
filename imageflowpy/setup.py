from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='imageflow-py',
  version='0.0.2',
  description='Library that generates images of basically anything.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='',  
  author='skrvt',
  author_email='skrvtbusiness@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='image generator', 
  packages=find_packages(),
  install_requires=[''] 
)