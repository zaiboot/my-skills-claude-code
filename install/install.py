#!/usr/bin/env python3
"""Claude Skills installer — Windows & macOS/Linux."""

import os
import platform
import sys


def get_source_path() -> str:
    """Return the absolute path to the skills folder in the repo."""
    script_dir: str = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(script_dir, "..", "skills"))


def get_target_path() -> str:
    """Return the absolute path to ~/.claude/skills."""
    return os.path.join(os.path.expanduser("~"), ".claude", "skills")


def link_skills(source: str, target: str) -> None:
    """Create a junction (Windows) or symlink (macOS/Linux) for the skills folder."""
    if platform.system() == "Windows":
        import _winapi  # pylint: disable=import-outside-toplevel
        _winapi.CreateJunction(source, target)
    else:
        os.symlink(source, target)


def main() -> None:
    """Entry point."""
    source: str = get_source_path()
    target: str = get_target_path()

    # Create source skills/ folder if it doesn't exist yet
    if not os.path.exists(source):
        os.makedirs(source)
        print(f"Created {source}")

    # Create ~/.claude/ if it doesn't exist yet
    target_parent: str = os.path.dirname(target)
    if not os.path.exists(target_parent):
        os.makedirs(target_parent)
        print(f"Created {target_parent}")

    # Refuse to overwrite a non-empty target to avoid data loss
    if os.path.exists(target):
        if os.listdir(target):
            print(f"Warning — {target} already exists and is not empty.")
            print("Refusing to override. Remove or back it up manually first.")
            sys.exit(1)
        print(f"Skipping — {target} already exists and is empty, nothing to do.")
        sys.exit(0)

    link_skills(source, target)
    print(f"Linked skills -> {source}")
    print("\nDone. Open Claude Code and run /skills to verify.")


if __name__ == "__main__":
    main()
