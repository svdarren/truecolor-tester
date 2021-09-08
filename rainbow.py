from sys import argv
from truecolor import
def main(col_arg="80"):
    try:
        cols =int(col_arg)
    except:
        raise "Error: column number incorrect"
    colors = [
        {
            "r": 255-(col*255/cols),
            "g": col*510/cols if col*510/cols>255 else 510-col*510/cols,
            "b": col*255/cols,
        } for col in range(cols)
    ]

    for c in colors:
        r,g,b = c.values()
        print("\033[48;2;{};{};{}".format(
            round(r),
            round(g),
            round(b),
        ))

        

if __name__ == "__main__":
    main(*argv[1:])