#!/usr/bin/env python3
"""Print a greeting with the current user and datetime."""

import datetime
import getpass


def main() -> None:
    """Entry point."""
    username: str = getpass.getuser()
    now: str = datetime.datetime.now().strftime("%A, %B %d, %Y %I:%M:%S %p")
    print(f"Hello, {username}! The current date and time is {now}.")


if __name__ == "__main__":
    main()
