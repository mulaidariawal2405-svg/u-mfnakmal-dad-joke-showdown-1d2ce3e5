#!/usr/bin/env python3
"""Dad Joke Showdown.

Writes one dad joke (at most 200 characters) to /output/entry.txt,
the text the make.fun judge compares two at a time.

Pure standard library; no network, no input, no secrets.
"""

import os
from pathlib import Path

JOKE = (
    "I told my kids I was going to grill them at the barbecue. "
    "They said, Dad, we're already well done."
)
# The pun does double duty: "grill" as in interrogate and as in cook,
# "well done" as in cooked through and as in already finished.


def check_joke() -> None:
    """Fail loudly unless the joke is one line of 1-200 characters."""
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be only white space"
    assert "\n" not in JOKE.strip(), "joke must be a single line"


def main() -> None:
    check_joke()
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
