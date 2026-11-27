import os

APOLOGY = (
    "I'm sorry I spent twenty minutes agreeing with you before "
    "realizing you were describing the bug I wrote."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(APOLOGY + "\n")
    print(APOLOGY)
    print(f"length: {len(APOLOGY)} chars")


if __name__ == "__main__":
    main()

    if len(APOLOGY) > 200 or not APOLOGY.strip():
        raise SystemExit(1)
