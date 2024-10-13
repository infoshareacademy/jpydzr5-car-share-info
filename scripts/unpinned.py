import sys


def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError

        file = sys.argv[1]

        with open(file) as f:
            data = f.read()

        data = data.replace("==", ">=")
        with open("unpinned_" + file, "w") as f:
            f.write(data)

    except IndexError:
        print("Usage: python unpinned.py <file>")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred: ", e.args)


if __name__ == "__main__":
    main()
