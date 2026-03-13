# Log Scrubber Skill

An OpenClaw skill to automatically redact sensitive information (API keys, tokens, secrets) from your workspace logs and memory files.

## Features

- **Automated Redaction:** Targets `memory/`, `logs/`, and `MEMORY.md`.
- **Regex-Based Detection:** Supports OpenRouter, OpenAI, and generic `key:secret` patterns.
- **Privacy First:** Designed to prevent accidental exfiltration or leakage of credentials in chat histories.

## Installation

This skill is designed to be part of an OpenClaw workspace. 

1. Ensure the `scripts/scrub.py` file is present.
2. Add the skill to your OpenClaw configuration.

## Usage

### Manual Trigger

Run via CLI or tool:
```bash
python3 scripts/scrub.py
```

### Scheduled (Automatic)

Recommended cron setup (daily at 02:00 UTC):
```json
{
  "name": "Jennifer-Log-Scrub",
  "schedule": { "kind": "cron", "expr": "0 2 * * *", "tz": "UTC" },
  "payload": { "kind": "systemEvent", "text": "Running scheduled log scrub..." },
  "sessionTarget": "main"
}
```

## Disclaimer

This is a best-effort redactor. Always verify sensitive logs before sharing.
