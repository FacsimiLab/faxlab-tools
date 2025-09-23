__all__ = ["get_file_size"]

import os

def get_file_size(file_path, return_size=False):
    """
    Print the size of a file in a human-readable format (bytes, KB, MB, or GB).

    Parameters
    ----------
    file_path : str
        Path to the file whose size will be printed.
    return_size : bool, optional
        If True, only return the file size in bytes without printing. If False (default), print the size and return the value.

    Returns
    -------
    int
        Size of the file in bytes, if return_size is True. Otherwise, returns None.
    """

    size_bytes = os.path.getsize(file_path)
    if size_bytes < 1024:
        print(f"File size: {size_bytes} bytes")
    elif size_bytes < 1024 ** 2:
        print(f"File size: {size_bytes / 1024:.2f} KB")
    elif size_bytes < 1024 ** 3:
        print(f"File size: {size_bytes / (1024 ** 2):.2f} MB")
    else:
        print(f"File size: {size_bytes / (1024 ** 3):.2f} GB")

    if return_size:
      return None
    else:
      return size_bytes
