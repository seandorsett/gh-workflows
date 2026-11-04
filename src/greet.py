import argparse


def main():
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--recipient", default="World", help="Recipient to greet.")
    args = parser.parse_args()
    print(f"Hello, {args.recipient}!")


if __name__ == "__main__":
    main()
