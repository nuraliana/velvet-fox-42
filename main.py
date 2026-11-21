import os

JOKE = "My agent's demo crashed, so it opened a PR titled fix: human error"


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.strip():
        raise SystemExit("entry.txt is empty")
    if not 1 <= len(text) <= 280:
        raise SystemExit(
            "entry.txt is %d characters, outside the 1-280 gate" % len(text)
        )
    print("Wrote entry.txt: %d characters, valid (1-280)" % len(text))


if __name__ == "__main__":
    main()
