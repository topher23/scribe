import sys
from perform import main

def arg_parse():

    if sys.argv is None:
        arg = ["dt"]
        return arg

    for arg in sys.argv[1:len(sys.argv)]:
        if arg == "dt" or arg == "knn" or arg == "nn":
            return arg
        else:
            raise Exception("Arg specified is incorrect. Acceptable args: dt, knn, and nn.")


if __name__ == "__main__":
    arg = arg_parse()
    main(arg)
