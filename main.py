import numpy


def main() -> None:
    num = numpy.random.default_rng(10)
    # print(numpy.random.seed)
    # print(num.integers(0, 129))
    # print(num.integers(0, 129))
    # print(num.integers(0, 129))
    # print(num.integers(0, 129))
    # print()
    # print(num.integers(0, 256, size=256))

    print(num.random(10))
    print(num.random())
    print(num.random())
    print()
    print(numpy.sin(90 * numpy.pi / 180))


if __name__ == "__main__":
    main()
