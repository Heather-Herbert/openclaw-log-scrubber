# SECURITY MANIFEST:
# Environment variables accessed: None
# External endpoints called: None
# Local files read: memory/*, logs/*, MEMORY.md
# Local files written: memory/*, logs/*, MEMORY.md

import os
import re

# Redaction patterns
PATTERNS = [
    r'sk-or-v1-[a-zA-Z0-9]{32,}',  # OpenRouter
    r'sk-[a-zA-Z0-9]{32,}',         # Standard OpenAI
    r'(?i)(api[_-]key|token|password|secret|key)["\']?\s*[:=]\s*["\']?([a-zA-Z0-9\-]{10,})["\']?', # Generic
]

def scrub_content(content):
    original = content
    for pattern in PATTERNS:
        content = re.sub(pattern, lambda m: f"{m.group(1)}: [REDACTED]" if len(m.groups()) > 1 else "[REDACTED]", content)
    return content, content != original

def main():
    base_dir = "/root/.openclaw/workspace"
    target_dirs = ["memory", "logs"]
    extra_files = ["MEMORY.md"]

    for d in target_dirs:
        full_path = os.path.join(base_dir, d)
        if not os.path.exists(full_path):
            continue
        for root, _, files in os.walk(full_path):
            for f in files:
                path = os.path.join(root, f)
                process_file(path)

    for f in extra_files:
        path = os.path.join(base_dir, f)
        if os.path.exists(path):
            process_file(path)

def process_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content, changed = scrub_content(content)
        
        if changed:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Scrubbed: {path}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

if __name__ == "__main__":
    main()
