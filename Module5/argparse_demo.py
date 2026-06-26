import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name")
parser.add_argument("--city")

args = parser.parse_args() 

print(args.name)
print(args.city)

# Advantage to use this
# In sys.argv we need to remember the order
# In argparse order does not metter

# If you want something as required argument then you can set
# parser.add_argument(
#     "--name",
#     required=True
# )