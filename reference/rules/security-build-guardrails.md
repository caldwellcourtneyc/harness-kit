---
name: security-build-guardrails
description: Build-time security rules that fire when a session touches code, in every project.
paths:
  - "**/*.ts"
  - "**/*.tsx"
  - "**/*.js"
  - "**/*.jsx"
  - "**/*.mjs"
  - "**/*.cjs"
  - "**/*.py"
  - "**/*.html"
---

<!-- Kit note: later shelf. The moment for it: your first app that uses a paid API key or
stores anyone's data. If the seed's first look finds you already have code projects, it
offers this one on day one. Install it as ~/.claude/rules/security-build-guardrails.md.
The paths: block means it loads only when code files are read, so on a brand-new project
it may not have loaded yet when the first code gets written; the new-project checklist
covers that gap. -->

# Security guardrails (build-time)

The "don't ship this" rules that apply while building any feature. They came out of a
security audit of real projects that found each of these mistakes at least once.

## API keys and secrets
Never put API keys in code that runs in the browser. Anything in client-side JavaScript
can be read by anyone who opens the page. Calls to paid providers (AI models, speech,
payment, any external API) go through server-side code (an API route, a serverless or
edge function). Environment variables that a build tool exposes to the browser (for
example `VITE_` or `NEXT_PUBLIC_` prefixes) are only for values that are safe to be
public. When adding any external API call, ask "does this key need to be in the
browser?" The answer is almost always no.

## File access
Any endpoint that reads or writes files is limited to a list of allowed folders: resolve
the path, then check it starts with an allowed folder. Always refuse `.env`, `.env.local`,
and any file with "secret" or "credential" in its name.

## Auth fails closed
In production, pages and endpoints that need a login require one. If the auth setup
comes from an environment variable and that variable is missing in production, deny
access (return an error) rather than letting everyone in. Open access is for local
development only.

## Auth exceptions stay narrow
When some routes skip the normal login check (because they handle their own), match
exactly those routes, not a broad path prefix that quietly includes others.

## Security headers
On every web app: `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`,
`Referrer-Policy: strict-origin-when-cross-origin`. Add a Content Security Policy when
there's time to tune it for the app.

## Debug routes
Debug and diagnostic endpoints are off in production, and need a login where they do
exist. Return 404 rather than 401, so their existence isn't revealed.
