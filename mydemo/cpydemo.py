#!/usr/bin/python
import sys
import os

setup_module='''#!/usr/bin/python

from distutils.core import setup, Extension

setup(
    name='%s',
    version='%s',
    author='%s',
    author_email='%s',
    url='%s',
    ext_modules=[Extension('%s', sources=[%s])]
)

'''

src_module='''#include <stdio.h>
#include <Python.h>

static PyObject* %s_helloworld(PyObject* self, PyObject* args) {
        printf("Hello World!\\n");
	return Py_BuildValue("");
}

static PyMethodDef methods[] = {
	{"helloworld", %s_helloworld, METH_VARARGS, "Test"},
	{NULL, NULL, METH_VARARGS, NULL}
};

static PyModuleDef module = {
	PyModuleDef_HEAD_INIT,
	"%s",
	NULL,
	-1,
	methods
};

void PyInit_%s() {
	PyModule_Create(&module);
}
'''

def setup_data(name, sources, version='0.0.1', author='', email='', url=''):
    sources = f"""'{"','".join(sources)}'"""
    return setup_module % (name, version,author,email,url,name,sources)

def mkdir(p):
    if not os.path.exists(p):
        os.mkdir(p)
        print(f'dir {p} created')
    else:
        print(f'dir {p} exists')

def mkfile(f, d):
    with open(f, 'w', encoding='utf-8') as fd:
        fd.write(d)

def demo(mod, path='.'):
    print('module name:', mod)
    if not isinstance(mod, str) or not mod[0].isalpha():
        print('The module name must be alphabetic')
        exit()
    
    mod1 = mod.lower()
    bdir = os.path.join(path, mod1)

    # 1
    print('mkdir ', bdir)
    mkdir(bdir)

    # 2
    print('make setup')
    file = os.path.join(bdir, 'setup.py')
    srcfiles=[os.path.join(bdir, mod1, mod1+'.c')]
    data = setup_data(mod, srcfiles)
    mkfile(file, data)
    
    # 3
    sdir = os.path.join(bdir, mod1)
    print('make ', sdir)
    mkdir(sdir)
    
    # 4
    print('make src')
    file = os.path.join(sdir, mod1+'.c')
    data = src_module % (mod, mod, mod, mod)
    mkfile(file, data)

    print('ok')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        mod = sys.argv[1]
        demo(mod)
    elif len(sys.argv) == 3:
        mod = sys.argv[1]
        path = sys.argv[2]
        demo(mod, path)
    else:
        print('usage: cpydemo.py modulename [path]')
