# dmwish
a better wapper for dmget: create your wishlist and run a single command to get them all.
dmwish will group the files by directory and submit dmget jobs for all the listed directories.

Command line tool:

```
usage: dmwish [-h] [-a ADD [ADD ...]] [-l] [-g] [-d]

dmget wish list

optional arguments:
  -h, --help            show this help message and exit
  -a ADD [ADD ...], --add ADD [ADD ...]
                        files to add to wishlist
  -l, --list            list files in wishlist
  -g, --get             get all files
  -d, --delete          clean all files in wishlist
```

In python:

```python

from dmwish import pydmwish
pydmwish(['dir1/file1', 'dir1/file2', 'dir2/file3'])
```
