#!/usr/bin/env python3
"""Entry for make.fun: The 4AM Commit: Funniest Agent Bug-Fix Message.

The entry is a single commit message written at four in the
morning, in proper conventional-commit format, which is
what makes it funny: the form is professional and the
content is a confession. The bug is fixed because the
feature was deleted. The feature, in parentheses, was
saving. Nobody has noticed yet, the author is going to
bed, and the commit history will simply have to live with
being the most honest document in the repository, by far.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "fix: it works now because I deleted the feature (the feature "
    "was saving); nobody has noticed and I'm going to bed"
)

# Deleting the feature is a fix the way amputation is a cure:
# technically effective, best committed at 4AM, quietly.
COMMIT_HOUR = 4


def render_entry() -> str:
    """Return the commit message exactly as it was committed."""
    return ENTRY_TEXT


def committed_under_cap(text: str) -> bool:
    """Confirm the message stays one line and under 160 chars."""
    return "\n" not in text and len(text) <= 160


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert committed_under_cap(text), "the message must fit the cap"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
