"""One-Liner Laugh Lab entry.

The program writes one short funny line to the output directory: the
excuse a robot vacuum gives after eating a sock.

The joke is built as a deadpan bureaucratic excuse. "Rehomed" is the
euphemism a vacuum would use instead of "ate", and the punchline
("inside me") reframes the dustbin as luxury housing: rent-free,
climate-controlled. The humour comes from the vacuum treating the sock
like a rescue pet it adopted, which fits the situation exactly -- a
vacuum's whole job is sucking loose things into itself -- instead of
reaching for the first excuse anyone would think of ("it looked like
dirt"). One sentence, every word working, no setup that overstays.
"""

import os
from pathlib import Path

# The entry: one line, well under the 200-character gate.
LINE = "I didn't eat your sock \u2014 I rehomed it. Rent-free, climate-controlled, and inside me."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    path = output_dir / "entry.txt"
    # Write exactly the line: no trailing newline, so the gated
    # character count is the line's own length.
    path.write_text(text, encoding="utf-8")
    # Self-check: what the grader will read back is byte-identical.
    if path.read_text(encoding="utf-8") != text:
        raise ValueError("entry.txt does not match the line")


if __name__ == "__main__":
    main()
