import argparse

parser = argparse.ArgumentParser(description="Simple CLI Calculator")

parser.add_argument("--num1", type=int, required=True)
parser.add_argument("--num2", type=int, required=True)
parser.add_argument(
    "--operation",
    choices=["add", "subtract", "multiply", "divide"],
    required=True,
)

args = parser.parse_args()
result = ''

if args.operation == "add":
    result = args.num1 + args.num2

elif args.operation == "subtract":
    result = args.num1 - args.num2

elif args.operation == "multiply":
    result = args.num1 * args.num2

elif args.operation == "divide":
    if args.num2 == 0:
        print("Cannot divide by zero")
        exit()

    result = args.num1 / args.num2

print(f"Result: {result}")