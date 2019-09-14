import os

readme_data='''# pydemo
## PyPA
[Python Packaging User Guide](https://packaging.python.org/)
## Install
`pip install pydemo`
## Usage
```
import pydemo
pydemo.init('testdemo')
```
'''

license_data='''MIT License

Copyright (c) 2019 q1b1fd8l

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

setup_data='''import setuptools

with open('README.md', 'r', encoding='utf-8') as fd:
	desc_data = fd.read()

setuptools.setup(
	name =    'pydemo',
	version = '0.0.1',
	author  = 'q1b1fd8l',
	author_email = 'q1b1fd8l@yandex.com',
	description  = 'A simple example',
	long_description = desc_data,
	long_description_content_type = 'text/markdown',
	url = 'https://github.com/q1b1fd8l/pydemo',
	packages = setuptools.find_packages(),
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
	],
)
'''

ignore_data='''.gitignore
build/
dist
*.egg-info
'''

demo_data='''
def hello():
	print('Hello world!')
'''


def make_dir(path):
	if not os.path.exists(path):
		print(f'make dir {path}')
		os.mkdir(path)

def make_file(path, data=None):
	pdir, pfile = os.path.split(path)
	make_dir(pdir)
	if data:
		print(f'make file {path}')
		with open(path, 'w', encoding='utf-8') as fd:
			fd.write(data)

def make_package(package_name, path='.'):
	'''https://packaging.python.org/'''
	# package name
	if not isinstance(package_name, str) or not package_name[0].isalpha():
		print('The module name must be alphabetic')
	pname = package_name.lower()
	# package path
	path = path or '.'
	ppath = os.path.join(path, pname)
	make_dir(ppath)
	# readme file
	readme_file = os.path.join(ppath, 'README.md')
	make_file(readme_file, readme_data)
	# lecense file
	license_file = os.path.join(ppath, 'LICENSE')
	make_file(license_file, license_data)
	# setup file
	setup_file = os.path.join(ppath, 'setup.py')
	make_file(setup_file, setup_data)
	# git ignore file
	ignore_file = os.path.join(ppath, '.gitignore')
	make_file(ignore_file, ignore_data)
	# src path
	spath = os.path.join(ppath, pname)
	make_dir(spath)	
	# src init file
	init_file = os.path.join(spath, '__init__.py')
	make_file(init_file, ' ')
	# src demo file
	demo_file = os.path.join(spath, 'pydemo.py')
	make_file(demo_file, demo_data)

def init(module, path='.'):
	make_package(module, path)

if __name__ == '__main__':
	init('pydemo', 'd:/pro')
