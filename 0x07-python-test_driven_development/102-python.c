#include <Python.h>

/**
 * print_python_string - ...
 *
 * @p: ....
 *
 */

void print_python_string(PyObject *p)
{
	Py_UNICODE *unicode_data;
	Py_ssize_t unicode_length;

	if (!PyUnicode_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid String Object\n");
		return;
	}

	unicode_data = PyUnicode_AsUnicodeAndSize(p, &unicode_length);

	printf("[.] string object info\n");
	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p)
							   ? "compact ascii"
							   : "compact unicode object");
	printf("  length: %ld\n", unicode_length);
	printf("  value: %ls\n", unicode_data);
}
