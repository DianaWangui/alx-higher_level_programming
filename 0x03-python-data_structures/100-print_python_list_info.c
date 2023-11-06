#include <Python.h>
#include <listobject.h>
#include <object.h>
/**
 * print_python_list_info -This is a function than prints
 * information about a python list
 * @p: A pointer to the python obkect rep in the python list
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (i = 0; i < size; i+=)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
