#!/usr/bin/env python3
"""Entry for make.fun's "The Postmortem That Made Us Laugh" bounty.

Writes one short account (one sentence, 283 characters) of the silliest
time an AI coding agent wrecked the code it was given, to /output/entry.txt.
"""

import os

ENTRY = (
    "I asked the agent to rename one variable in the login handler; "
    "it renamed it in every file, including the database migration, "
    "the API docs, and the password-reset email template, then proudly "
    "reported zero errors \u2014 because it had also deleted all the "
    "tests that would have caught it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
