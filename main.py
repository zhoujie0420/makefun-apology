import os

def generate_apology() -> str:
    return (
        "No action needed: I accidentally deleted payroll.xlsx, so I "
        "reconstructed 84 salaries from memory; several people will be "
        "pleasantly surprised on Friday."
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
