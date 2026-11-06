from genesis_core import GenesisMind


if __name__ == "__main__":
    gm = GenesisMind()

    result = gm.run("Should I expand Alternative Slowbar globally now?")

    print(result)
