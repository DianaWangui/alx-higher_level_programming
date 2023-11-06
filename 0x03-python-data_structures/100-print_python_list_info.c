#include <Python.h>
/**
 * print_python_list_info -This is a function than prints
 * information about a python list
 * @p: A pointer to the python obkect rep in the python list
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i, allocated;

	size = PyList_Size(p);

	if (!PyList_Check(p))
	{
		fprinf(stderr,"Invalid PyList");
		return;
	}

	allocated = ((PyObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p,i);

		if(element != NULL)
		{
			printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		}
		else
		{
			fprintf(stderr,"Filed to retrieve element %d\n", i);
		}
	}
}
