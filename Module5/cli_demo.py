import sys

# output will be based on your argument which you pass on the runtime
print("Script:", sys.argv[0])
print("Name:", sys.argv[1])

# Professional Python applications don't use sys.argv directly. They use the built-in argparse module.