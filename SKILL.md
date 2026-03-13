---
name: log-scrubber
description: Automatically scrub API keys and secrets from logs and memory files.
homepage: https://github.com/Heather-Herbert/log-scrubber
metadata:
  clawdbot:
    emoji: "🧼"
    requires:
      env: []
    primaryEnv: ""
    files: ["scripts/scrub.py"]
---

# Log Scrubber

Protect your session data by redacting common API key patterns and secrets from your workspace logs and memory files.

## External Endpoints
None. This skill operates entirely locally on your workstation/server.

| Endpoint | Data Sent |
| :--- | :--- |
| N/A | None |

## Security & Privacy
- **Local Only:** This skill does not transmit data to any external server.
- **File Access:** Reads and modifies files in designated `memory/`, `logs/`, and `MEMORY.md` locations within the OpenClaw workspace.
- **Redaction:** Uses regex patterns to identify and replace sensitive tokens with `[REDACTED]`.

## Model Invocation Note
This skill is designed to run as a cron job or manual command to maintain workspace hygiene. It does not require continuous model monitoring.

## Trust Statement
By using this skill, you allow it to modify files in your workspace for the purpose of secret redaction. Only install if you trust the local regex implementation.

## Usage
Add to your `cron` jobs to run periodically:
```json
{
  "name": "Log Scrubbing",
  "schedule": { "kind": "cron", "expr": "0 2 * * *" },
  "payload": { "kind": "systemEvent", "text": "Run log-scrubber to protect secrets." },
  "sessionTarget": "main"
}
```
