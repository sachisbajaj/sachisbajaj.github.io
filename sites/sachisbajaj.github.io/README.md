# Sachi Bajaj — Personal Portfolio

Static Jekyll site for [sachisbajaj.github.io](https://sachisbajaj.github.io), published with GitHub Pages. Pages are written in Markdown with YAML front matter; shared structure lives in Jekyll layouts and includes.

## Update the site

- Edit `index.md`, `about.md`, `work.md`, or `contact.md` to update page copy.
- Edit `_data/navigation.yml` to update the navigation labels or page destinations.
- Edit `_config.yml` for the site title, description, canonical URL, or LinkedIn profile link.
- Edit `assets/css/main.css` for visual changes and `assets/favicon.svg` for the browser icon.
- Keep private details out of this public site. The résumé's email address and phone number are intentionally not included.

## Protect commit metadata

Git commit author details are public in this repository. Before committing locally, set Git's author email to the GitHub-provided no-reply address shown under **Settings → Emails**, not a personal address.

## Preview locally

Install Ruby and Bundler if needed, then run these commands from this directory:

```sh
gem install bundler
bundle install
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000`. Changes to Markdown and CSS are rebuilt automatically; stop the server with `Ctrl+C`.

GitHub Pages builds the site from the `main` branch root using its supported Jekyll build. No custom build workflow is required.

## Run Lighthouse

After publishing, open `https://sachisbajaj.github.io` in Chrome, open DevTools, select **Lighthouse**, and run the **Performance**, **Accessibility**, **Best Practices**, and **SEO** categories. For a command-line run with Chrome installed:

```sh
npx lighthouse https://sachisbajaj.github.io \
  --only-categories=performance,accessibility,best-practices,seo \
  --view
```

Check both a 375px-wide mobile viewport and a 1280px-wide desktop viewport in Chrome DevTools' responsive device mode.
