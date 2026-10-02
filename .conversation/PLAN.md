# Personal Portfolio Site Plan

## Site direction

- Build a static GitHub user site with Jekyll for `myusername.github.io`.
- Use a light-only, single-column layout with a clean, modern, feminine visual direction.
- Use high-contrast text, generous spacing, responsive sizing, visible keyboard focus states, and semantic HTML.
- Keep the design restrained: a soft feminine accent palette, clear hierarchy, and no animation system or unnecessary dependencies.

## Pages

- **Home** — concise introduction, current MBA context, selected strengths, and links to Work and Contact.
- **About** — education, interests, volunteering, and a short professional overview based only on the supplied résumé.
- **Work Experience** — Google and Apple experience with roles, dates, responsibilities, and supplied outcomes.
- **Contact** — LinkedIn link only. No public email address or `mailto:` link.

## Content source

Content will be created from the supplied August 2026 résumé. The LinkedIn URL will be displayed as a link but will not be fetched or used as a content source. Any missing personal statement, headshot, GitHub username, or project portfolio will remain clearly labeled as a placeholder rather than being invented.

## Implementation

- Jekyll layouts and includes for reusable page structure, navigation, metadata, and footer.
- Page copy in Markdown with YAML front matter.
- `baseurl: ""` in `_config.yml`, with `relative_url` and `absolute_url` filters for links.
- Plain HTML and CSS with minimal JavaScript only if needed for a small accessible navigation enhancement.
- SEO metadata, canonical URLs, Open Graph basics, `sitemap.xml`, `robots.txt`, and a favicon.
- README instructions for editing content, local preview, GitHub Pages publishing, and Lighthouse checks.

## Validation

- Check all navigation and internal links.
- Check layout at 375px and 1280px widths.
- Run an HTML/accessibility and Lighthouse review where tooling is available, targeting 90+ in Performance, Accessibility, Best Practices, and SEO.

## Assumptions and placeholders

- `myusername.github.io` is a placeholder until the actual GitHub username is supplied.
- The résumé name, education, roles, dates, achievements, volunteering, and interests are treated as supplied facts.
- No projects, testimonials, headshot, personal bio, GitHub profile, or public email will be added unless supplied.
- The Contact page will use LinkedIn as the primary contact route because email should remain private.