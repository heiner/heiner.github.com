def af(p, n):
    a = (1 + p) ** n
    return p * a / (a - 1)


def afapprox(p, n):
    return (1 + n * p / 2) / n


def main():
    ps = (0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0, 20.0)
    ns = (2, 5, 7, 10, 15, 20, 25, 30)

    print(" " * 5, end="\t")
    print("\t".join("%22i" % n for n in ns))
    for p in ps:
        print("p = %.1f%%" % p, end="\t")
        for n in ns:
            print(
                "%.3f%% vs %.3f%%"
                % (
                    100 * af((1 + p / 100) ** (1 / 12) - 1, 12 * n),
                    100 * afapprox(p / 100 / 12, 12 * n),
                ),
                end="\t",
            )
        print("")


if __name__ == "__main__":
    main()
