"""
>>> sys.tracebacklimit = 0
>>> assert sys.version_info > (3, 8, 0), \
'Python 3.8+ is required'
"""

import sys

print('Your Python version:', sys.version[:6])
