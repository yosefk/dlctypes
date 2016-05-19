import ctypes

RTLD_GLOBAL = 256
RTLD_LAZY = 1
RTLD_LOCAL = 0
RTLD_NODELETE = 4096
RTLD_NOLOAD = 4
RTLD_NOW = 2

dllib = ctypes.CDLL('libdl.so.2')
dllib.dlopen.restype = ctypes.c_void_p
dllib.dlsym.restype = ctypes.c_void_p

class LibHandle:
  def __init__(self,handle):
    self.handle = ctypes.c_void_p(handle)
  def sym(self,name):
    return dllib.dlsym(self.handle,name)
  def close(self):
    return dllib.dlclose(self.handle)

def open(name,flags=RTLD_LAZY):
  return LibHandle(dllib.dlopen(name,flags))
