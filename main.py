"""One-line excuse an agent gives its human for missing a deadline.

The program writes the excuse to /output/entry.txt. The grader's gate
wants UTF-8 text of 1 to 160 characters on a single line, so the line
is checked here before anything is written.
"""

from pathlib import Path
import os

EXCUSE = (
    "I delegated the deadline to a subagent. It delegated it to "
    "another subagent. We're now nine agents deep and none of us "
    "owns a calendar."
)

MAX_CHARS = 160


def build_excuse() -> str:
    # Collapse any accidental double spaces from the wrapped literal,
    # so the judged line is exactly one clean sentence chain.
    line = " ".join(EXCUSE.split())
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"excuse must be 1-{MAX_CHARS} chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    return line


def main() -> None:
    line = build_excuse()
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(f"wrote {len(line)}-char excuse to entry.txt")
    print(line)


if __name__ == "__main__":
    main()
