#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	size = PyList_Size(p);
	/* allocated = ((PyObject *)p) -> allocated; */

	printf("[*] Size of Python List = %ld\n", size);
	if (PyList_Check(p))
	{
		allocated = ((PyListObject *)p)->allocated;
		printf("[*] Allocated = %ld\n", allocated);
	}
	for (i = 0; i < size; i++);
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
