"""
52. Write a Python program to print to STDERR.
"""

import sys
import logging

sys.stderr = open('err.txt', 'w')
print("u", "w", "u", file=sys.stderr, flush=True)


# Create a logger object
logger = logging.getLogger()

# Set the level to print all messages
logger.setLevel(logging.DEBUG)

# Create a stream handler for stderr
handler = logging.StreamHandler(sys.stderr)

# Add the handler to the logger
logger.addHandler(handler)

# Log an error message
logger.error('ola')