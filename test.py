import os
import ctypes
dll = ctypes.CDLL("lib/wDFT.dll")

print("success")
print(dll.hello(None))