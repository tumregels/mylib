import ctypes
import pathlib


if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = pathlib.Path(__file__).parent.absolute() / "build" / "libconvert.so"
    clib = ctypes.CDLL(libname)
    celsius = 0.0
    clib.convert_celsius_to_fahrenheit.restype = ctypes.c_float
    answer = clib.convert_celsius_to_fahrenheit(ctypes.c_float(celsius))
    print(answer)
