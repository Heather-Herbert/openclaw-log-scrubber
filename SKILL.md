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
