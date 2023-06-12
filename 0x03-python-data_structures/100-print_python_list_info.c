#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t _size, _allocate, i;
	PyObject *item;

	_size = PyList_Size(p);
	_allocate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", _size);
	printf("[*] Allocated = %ld\n", _allocate);

	for (i = 0; i < _size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
