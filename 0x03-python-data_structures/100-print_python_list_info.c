#include <Python.h>
#include <stdio.h>
/**
 * c_python_info - prints info about a Python list
 * @p: pointer to a PyObject
 */
void c_python_info(PyObject *p)
{
	int size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);
	for (int i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
