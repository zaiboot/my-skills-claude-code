---
name: hello-skill
description: >
  Greets the user by their system username and prints the current datetime.
  Triggers when the user says anything like "say hello", "hello", "greet me",
  or "what time is it". Use this skill to validate that Claude Code is loading
  skills correctly from the shared skills repo.
---

# Hello Skill

Greet the user by their system username and print the current datetime.

## Instructions

1. Retrieve the system username by running `whoami` via bash
2. Retrieve the current datetime by running `date` (macOS/Linux) or
   `Get-Date` (Windows) via bash
3. Print the greeting in this exact format: