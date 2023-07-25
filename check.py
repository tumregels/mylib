import ctypes
import pathlib

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = pathlib.Path(__file__).parent.absolute() / "build" / "libconvert.so"
    c_lib = ctypes.CDLL(libname)
    celsius = 0.0
    c_lib.convert_celsius_to_fahrenheit.restype = ctypes.c_float
    answer = c_lib.convert_celsius_to_fahrenheit(ctypes.c_float(celsius))
    print(answer)
