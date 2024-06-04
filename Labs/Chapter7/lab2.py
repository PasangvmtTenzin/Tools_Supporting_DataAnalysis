import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True, help="lab2.py")
    parser.add_argument("-n", "--num", type=int, required=True, help="Intiger Number")
    parser.add_argument("-o", "--output", type=str, required=True, help="lab2_result.py")
    args = parser.parse_args()


    print("Input:", args.input)
    print("Number:", args.num)
    print("Output:", args.output)

if __name__ == "__main__":
    main()

# python lab2.py -i input.txt -n 5 -o output.txt