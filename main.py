"""One-line entry: the funniest AI excuse for a missed deadline.

The grader runs this program and reads /output/entry.txt.
The line must be a single line, 1-200 characters, not only whitespace.
"""

import os


EXCUSE = "I outsourced your deadline to a subagent, who outsourced it to another subagent, who has now filed a ticket asking me for the deadline."


def check_line(text):
    """Gate mirror: the sealed scorer wants 1-200 chars, one line."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    if len(text) != len(stripped) or "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry is over 200 characters")
    return text


def main():
    line = check_line(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
