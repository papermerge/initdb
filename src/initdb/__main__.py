import sys

from .config import config
print("this is __main__.py")


if len(sys.argv) > 1:
    print(sys.argv[1])

print(config)
