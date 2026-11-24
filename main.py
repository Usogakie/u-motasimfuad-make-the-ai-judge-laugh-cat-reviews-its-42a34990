"""The cat reviews its human.

This entry is a one-line review written from a cat's point of view. The
human moved the food bowl two whole inches to the left and expected the
cat to simply adapt, as if a cat were some kind of dog. The cat disagrees
and says so, in one star, with feeling.

The program writes the review line to entry.txt inside the output
directory given by MAKEFUN_OUTPUT_DIR (defaulting to /output).
"""

import os

LINE = (
    "Gave my human one star because he moved my food bowl two whole "
    "inches left and expected me to just adapt like some kind of dog."
)


def _check_line(line):
    """Make sure the review is one non-empty line before it is written."""
    if not line or not line.strip():
        raise ValueError("review line must not be empty")
    if "\n" in line.strip():
        raise ValueError("review line must be a single line")
    return line.strip()


def main():
    line = _check_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
