import unittest
import sys
import os

# Add scripts directory to path to import scrub.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from scrub import scrub_content

class TestScrubber(unittest.TestCase):
    def test_scrub_patterns(self):
        # OpenRouter token
        test_str = "My key is sk-or-v1-12345678901234567890123456789012"
        scrubbed, changed = scrub_content(test_str)
        self.assertTrue(changed)
        self.assertNotIn("sk-or-v1-", scrubbed)
        self.assertIn("[REDACTED]", scrubbed)

        # Standard OpenAI token
        test_str = "sk-12345678901234567890123456789012"
        scrubbed, changed = scrub_content(test_str)
        self.assertTrue(changed)
        self.assertNotIn("sk-", scrubbed)
        self.assertIn("[REDACTED]", scrubbed)

        # Generic API token
        test_str = "api_key = abcdef1234567890"
        scrubbed, changed = scrub_content(test_str)
        self.assertTrue(changed)
        self.assertIn("api_key: [REDACTED]", scrubbed)

if __name__ == '__main__':
    unittest.main()
