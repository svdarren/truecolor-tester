from sys import argv
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

    for count, c in enumerate(colors):
        r,g,b = c.values()
        foreground = "\033[48;2;{};{};{}m".format(
            round(r),
            round(g),
            round(b),
        )
        background = "\033[38;2;{};{};{}m".format(
            round(255-r),
            round(255-g),
            round(255-b),
        )
        print(foreground, background, str(count))

    return True

        

if __name__ == "__main__":
    main(*argv[1:])