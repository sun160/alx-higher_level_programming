#!/usr/bin/python3
"""Module inherited list class MyList."""


class MyList(list):
    """Implements sorted printing."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
