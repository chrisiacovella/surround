"""
Unit and regression test for the surround package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import surround


def test_surround_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "surround" in sys.modules
