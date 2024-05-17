"""
42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS
"""

# Import the 'platform' and 'struct' modules.
import platform
import struct

# Use the 'architecture' function from the 'platform' module to get the bit architecture (32-bit or 64-bit) of the current platform.
# The [0] index retrieves the first element of the result, which is the architecture string.
architecture = platform.architecture()[0]

# Print the bit architecture string, which will be "32bit" or "64bit."
print(architecture)

# Use the 'calcsize' function from the 'struct' module to determine the size (in bytes) of the C int type for the current platform.
# The format string "P" is used to represent the C void pointer type, and multiplying it by 8 gives the size in bits.
# The result will be 32 for 32-bit platforms and 64 for 64-bit platforms.
print(struct.calcsize("P") * 8)