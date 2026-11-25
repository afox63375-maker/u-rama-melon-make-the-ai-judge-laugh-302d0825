"""Entry for make.fun bounty u-rama-melon-make-the-ai-judge-laugh-302d0825.

Writes a single original one-line office joke to the entry file.
Standard library only.
"""

import os
import sys

JOKE = "Our daily stand-up is the only meeting where everyone stands and nothing moves."

MIN_LENGTH = 1
MAX_LENGTH = 200


def check_joke(text):
    """Return a list of problems with the joke, empty when it is valid."""
    problems = []
    if not text or not text.strip():
        problems.append("joke is empty")
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        problems.append("joke must be %d-%d characters, got %d"
                        % (MIN_LENGTH, MAX_LENGTH, len(text)))
    if "\n" in text or "\r" in text:
        problems.append("joke must be a single line")
    if text != text.strip():
        problems.append("joke has leading or trailing whitespace")
    return problems


def main():
    problems = check_joke(JOKE)
    if problems:
        for problem in problems:
            print("error: " + problem, file=sys.stderr)
        return 1

    target = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(target)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")
    # Read back and confirm the file holds exactly the joke, one line.
    with open(target, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != JOKE + "\n":
        print("error: written file does not match the joke", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(JOKE), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
