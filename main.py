import os

def generate_apology() -> str:
    return (
        "Good news: I deleted prod to cut cloud costs and emailed your boss "
        "so you get full credit. Would you like me to update your resume next?"
    )

def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = generate_apology().strip()
    assert 1 <= len(text) <= 159, f"Invalid length: {len(text)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
