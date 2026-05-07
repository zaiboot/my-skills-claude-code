# claude-skills

A shared collection of Claude Code skills for the team. Clone once, run the installer, and get updated skills automatically via `git pull`.

---

## What's inside

```
claude-skills/
├── README.md
├── skills/
│   ├── hello-skill/
│   │   └── SKILL.md
│   └── sprint-ticket-writer/
│       └── SKILL.md
└── install/
    └── install.py
```

---

## Requirements

- [Claude Code](https://claude.ai/code) installed and working
- Git
- Python 3.8+

---

## Windows 11 setup

### 1. Clone the repo

```powershell
git clone https://github.com/zaibootcr/claude-skills.git C:\Tools\claude-skills
```

### 2. Run the installer

```powershell
python C:\Tools\claude-skills\install\install.py
```

### 3. Verify

```powershell
ls $env:USERPROFILE\.claude\skills
```

### Updating skills

```powershell
cd C:\Tools\claude-skills
git pull
```

No reinstall needed — the junction picks up changes immediately.

---

## macOS setup

### 1. Clone the repo

```bash
git clone https://github.com/zaibootcr/claude-skills.git ~/Tools/claude-skills
```

### 2. Run the installer

```bash
python3 ~/Tools/claude-skills/install/install.py
```

### 3. Verify

```bash
ls -la ~/.claude/skills
```

### Updating skills

```bash
cd ~/Tools/claude-skills
git pull
```

No reinstall needed — the symlink picks up changes immediately.

---

## How it works

The installer creates a single junction (Windows) or symlink (macOS) from `~/.claude/skills` to the `skills/` folder in this repo. Claude Code loads skills from that folder automatically on startup. When you pull new changes, every skill updates instantly — no reinstall needed.

---

## Adding a new skill

1. Create a folder under `skills/` with a `SKILL.md` inside
2. Commit and push
3. Teammates run `git pull` — skill is immediately available

---

## Troubleshooting

**Skill not triggering in Claude Code**
Run `/skills` inside a Claude Code session to see what's loaded. If your skill is missing, check that the junction/symlink exists under `~/.claude/skills`.

**Junction creation fails on Windows**
Some corporate policies restrict junction creation. Try running the script from a terminal with elevated privileges.

**Symlink creation fails on macOS**
Check that `~/.claude/` exists. If not, run `mkdir -p ~/.claude` first and retry.

**Skill loads but doesn't fire**
The skill description in `SKILL.md` controls when Claude auto-invokes it. Make sure the description covers the phrases you're using to trigger it.
