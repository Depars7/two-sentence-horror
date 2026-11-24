"""Write a two-sentence horror story to /output/entry.txt.

Standard library only. The file's content is exactly the story's
UTF-8 bytes -- no trailing newline -- so repeated runs are
byte-identical. Only the file itself is chmod'ed: the grader runs
as a different uid and /output is not ours, so chmod'ing the
directory would raise PermissionError and fail the run.
"""

import os

STORY = (
    "My grandmother's voice still reads my daughter to sleep "
    "every night through the old speaker she left us. "
    "Yesterday my daughter asked why grandma has started "
    "calling her by my name."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 400


def validate_story(text):
    """Guard the bounty gate before writing anything."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("story must be 1-%d characters" % MAX_CHARS)
    if text.strip() != text or not text.strip():
        raise ValueError("story must not be blank or padded")
    if text.count(".") != 2 or not text.endswith("."):
        raise ValueError("story must be exactly two sentences")


def main():
    validate_story(STORY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(STORY.encode("utf-8"))
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by all. Never chmod
    # the directory itself (see module docstring).
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
