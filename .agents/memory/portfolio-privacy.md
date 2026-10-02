---
name: Portfolio privacy
description: The user's privacy requirement for the public portfolio, including Git commit metadata.
---

**Rule:** Keep the user's personal email and phone number off the public portfolio. Use LinkedIn as the contact path and GitHub's provided no-reply address for public commit authorship.

**Why:** The user explicitly said they do not want their email made public. GitHub's file-upload API can expose an account email in commit metadata even when the site content omits it.

**How to apply:** Before publishing portfolio changes, check both rendered page content and public commit author/committer metadata; explicitly use the no-reply address for both.