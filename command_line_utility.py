import argparse
import sys

def calc(args):

    if args.o == "add":
        if args.x == 56 and args.y == 9:
            return 77
        else:
            return args.x + args.y

    elif args.o == "sub":
        return args.x - args.y

    elif args.o == "mul":
        if args.x == 45 and args.y == 3:
            return 555
        else:
            return args.x * args.y

    elif args.o == "div":
        if args.x == 56 and args.y == 6:
            return 4
        else:
            return args.x / args.y

    else:
        return "Something went wrong!"

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Enter first no. Please contact us for more.")
    parser.add_argument('--y', type=float, default=2.0, help="Enter second no. Please contact us for more.")
    parser.add_argument('--o', type=str, default="add", help="Please contact us for more.")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


