from genesis_full import GenesisMind


if __name__ == "__main__":
    gm = GenesisMind()

    while True:
        try:
            user = input("You > ")
        except (EOFError, KeyboardInterrupt):
            break
        if user.strip().lower() in {"exit", "quit"}:
            break
        result = gm.run(user)

        print("\n--- GENESIS OUTPUT ---")
        for k, v in result.items():
            print(f"{k}: {v}")
        print("\n")
