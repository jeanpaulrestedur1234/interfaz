import ctypes

# Specify the path to the OpenSim library
opensim_lib_path = "path/to/OpenSim/libraries/libosimSimbody.dylib"  # Replace with the actual path to libosimSimbody.dylib or libosimSimbody.so

# Load the library
osim = ctypes.CDLL(opensim_lib_path)