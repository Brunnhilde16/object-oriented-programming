"""Class implementing a linked list."""
import sys


class Link:
    """Class implementing a linked list."""

    def __init__(self, value, next=None):
        """Initialise linked list."""
        self.value = value
        self.next = next

    def insert(self, link):
        """Insert a new link after the current one."""
        link.next = self.next
        self.next = link

    def __iter__(self):
        """Iterate through the linked list."""
        return LinkIterator(self)


class LinkIterator:
    """Implementation of the iterator protocol on class Link."""

    def __init__(self, link):
        """Initialize yourself."""
        self.here = link

    def __iter__(self):
        """Return yourself."""
        return self

    def __next__(self):
        """Get the value of next item."""
        if self.here:
            next = self.here
            self.here = self.here.next
            return next.value
        else:
            raise StopIteration


def byte_size(n):
    """Print the size in bytes of lists up to length n."""
    data = []
    for i in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print(f"Length:{a}; Size in bytes:{b}")
        data.append(i)
