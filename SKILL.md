---
name: log-scrubber
description: Automatically redacts API keys, tokens, and secrets from workspace logs and memory files.
---

# Log Scrubber

This skill automatically scans your `/root/.openclaw/workspace/` environment, logs, and memory files to detect and redact sensitive information like API keys, tokens, and credentials.

## Features
- **Proactive Scanning**: Scans for known patterns (regex) of common secrets.
- **Automated Redaction**: Sanitizes files in-place while keeping backups of original files (e.g., `.bak` extension).
- **Security**: Ensures your secrets don't accidentally end up in logs sent to providers or stored in plain-text memory files.

## Usage

### 1. Manual Scrub
You can trigger a full scan and scrub manually:
```bash
# Within an agent swarm or directly via tools
log_scrub_run
```

### 2. Automated Maintenance (Cron)
This skill is designed to run automatically at 2:00 AM UTC to ensure your environment stays clean.

---
## Implementation
- **Script**: `/root/.openclaw/workspace/skills/log-scrubber/scripts/scrub.py`
- **Schedule**: `0 2 * * *` (Cron)
- **Target**: `main` session
