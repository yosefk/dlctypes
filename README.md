The dl module which provides access to dlopen and dlsym has been deprecated in Python and it is recommended
that ctypes is used instead. However, while ctypes lets you call functions conveniently, dlsym lets you get the memory
address of functions and global variables and the latter is sometimes useful in itself.

This module provides an implementation of the dl module using ctypes (it simply loads libdl.so using ctypes
and calls dlopen and dlsym.) It can be used thusly:

import dlctypes
dl = dlctypes
