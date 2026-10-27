---
type: Tutorial
title: "Working with Repository-Level Secrets: Log masking: what it catches, and what it misses"
description: "Masking hides only the exact secret value; encoded, partial or derived copies leak unless you register them with ::add-mask::."
tags: [github-actions, secrets, security, masking, github-token, docker, hands-on]
status: stable
generated: { by: claude-code/claude-opus-5-5, at: 2026-10-26T00:00:00Z }
sources:
  - id: gh-secrets
    resource: https://docs.github.com/en/actions/concepts/security/secrets
    title: Secrets
  - id: gh-use-secrets
    resource: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets
    title: Using secrets in GitHub Actions
  - id: gh-secure-use
    resource: https://docs.github.com/en/actions/reference/security/secure-use
    title: Secure use reference
  - id: gh-secret-set
    resource: https://cli.github.com/manual/gh_secret_set
    title: gh secret set
  - id: docker-login-action
    resource: https://github.com/docker/login-action
    title: docker/login-action
---

<p align="center">
  <a href="README.md">📂 <b>Working with Repository-Level Secrets</b></a> &nbsp;·&nbsp; Lesson 12 · Part 4 of 10 &nbsp;·&nbsp; ⏱️ 2 min
</p>

# 🙈 Log masking: what it catches, and what it misses

GitHub scans the logs for the **exact** secret value and replaces it with `***`:

```text
Run echo "The secret is $DEMO_SECRET"
The secret is ***
```

That's a safety net, not a guarantee. It misses **changed copies**:

| You print | Masked? |
|---|---|
| The exact value | ✅ `***` |
| The value base64-encoded | ❌ Readable |
| Part of it (`${SECRET:0:4}`) | ❌ Readable |
| A JSON secret, one field at a time | ❌ Often readable. Store each field as its own secret instead |
| A value you derived, after `echo "::add-mask::$VALUE"` | ✅ `***` |

```yaml
- run: |
    TOKEN_B64=$(printf '%s' "$API_TOKEN" | base64)
    echo "::add-mask::$TOKEN_B64"       # register the derived value for masking first
    echo "Encoded: $TOKEN_B64"          # → Encoded: ***
```

> [!NOTE]
> **📘 From the GitHub docs:** don't wrap a secret in a blob of JSON, XML or YAML. Redaction works best on plain values, so create one secret per sensitive value. And any sensitive value that isn't a GitHub secret (a token you generated, say) should be masked with `::add-mask::`. ([Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use))

> [!CAUTION]
> **Never print a secret on purpose, even "just to check it".** If you need to know it's set, print its length or test that it's non-empty.

---

<p align="center">
  <a href="03-using-it-fixing-the-docker-login.md">⬅️ Using it: fixing the Docker login</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="README.md">📂 Topic overview</a>
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="05-rules-that-catch-people-out.md"><b>Next: Rules that catch people out ➡️</b></a>
</p>
