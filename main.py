"""Write this entry's one-line excuse to the harness output directory.

The grader runs this program and reads ``entry.txt`` from the output
directory (``$MAKEFUN_OUTPUT_DIR``, or ``/output`` when that is unset).
The excuse itself lives in ``ENTRY.txt`` beside this file; this program
is only plumbing: read the line, check its length, write it out.
The output file holds exactly the excuse text, with no trailing
newline, so repeated runs are byte-identical.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "ENTRY.txt"), "r", encoding="utf-8") as fh:
        excuse = fh.read().strip()
    if not excuse:
        print("ENTRY.txt is empty", file=sys.stderr)
        return 1
    if len(excuse) > 200:
        print("excuse is %d characters, over the 200 limit" % len(excuse),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(excuse)
    print("wrote %d bytes to %s" % (len(excuse.encode("utf-8")), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
