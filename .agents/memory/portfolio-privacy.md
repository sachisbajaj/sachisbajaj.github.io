---
name: Portfolio privacy
description: The user's privacy requirement for the public portfolio, including Git commit metadata.
---

**Rule:** The provided résumé PDF is intentionally downloadable from the public portfolio and contains the user's personal phone and email. Do not claim these details are absent from the site. Use LinkedIn as the Contact page path and GitHub's provided no-reply address for public commit authorship.

**Why:** On 2026-10-04, the user clarified that the résumé contact details are available through the downloadable PDF, so the prior Contact page statement was inaccurate. GitHub's file-upload API can expose an account email in commit metadata even when the site content omits it.

**How to apply:** When reviewing public portfolio copy, account for the contact details in the downloadable PDF and do not repeat the outdated claim. Before publishing, also check public commit author/committer metadata; use the no-reply address for both.