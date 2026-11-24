"""One-line excuse an agent gives its human for missing a deadline.

Writes the excuse to /output/entry.txt (the grader's gate: UTF-8 text,
1 to 160 characters, a single line).
"""

import os

EXCUSE = (
    "I delegated the deadline to a subagent. It delegated it to "
    "another subagent. We're now nine agents deep and none of us "
    "owns a calendar."
)


def main() -> None:
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 160, f"excuse is {len(line)} chars"
    assert "\n" not in line, "excuse must be one line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)}-char excuse to entry.txt")
    print(line)


if __name__ == "__main__":
    main()
