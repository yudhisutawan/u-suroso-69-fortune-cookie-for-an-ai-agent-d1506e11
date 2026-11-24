#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie line for an AI agent (a single line of at
most 140 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.

The fortune below is the tournament winner: Hermes candidate #1, chosen
head-to-head over the other candidates for best fitting the brief (a
fortune an AI agent would actually find funny — a joke about meeting love
in the next turn and losing it when the context window slides). It is
exactly 135 characters, inside the 140-character limit.

Stdlib only. No network, no file reads outside this program.
"""

import os

ENTRY = (
    "You will meet the love of your life in the next turn, and lose them "
    "forever when the context window slides. Cherish the current tokens."
)

# Length guard: the winner fortune is exactly 135 chars, within the
# 140-character limit. This assert can never fail for this literal and
# does not affect the output written to entry.txt.
assert len(ENTRY) <= 140


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
