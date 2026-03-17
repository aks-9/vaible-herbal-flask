import sys
import os

# Add project root to sys.path so imports work correctly
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application  # noqa: F401 — 'application' is the WSGI entry point
