---
name: security-review
description: "Use when reviewing a vulnerable codebase for security issues, identifying exploitable risks, prioritizing findings, and proposing safe remediations. Good for security-review demos, PR audits, incident triage, and hardening a repository without introducing new vulnerabilities."
---

# Security Review of a Vulnerable Repository

## Purpose

Use this skill to review a repository or targeted module for security weaknesses, explain why they matter, and recommend concrete, safe fixes. This is especially effective for live demos where the goal is to show the AI acting as a reviewer rather than just a code generator.

## Workflow

### 1. Define the review scope
- Identify the code path to review: specific file, module, API route, service, or repository.
- Determine the expected trust boundaries: user input, external APIs, database, auth/session state, file access, or admin-only flows.
- Confirm whether the code is intentionally vulnerable demo content or real production code.

### 2. Map the attack surface
- Trace entry points and data flow.
- Look for untrusted input, external dependencies, and privileged operations.
- Identify where validation, authorization, and sanitization should occur.

### 3. Look for common vulnerability patterns
Prioritize checks for:
- Injection flaws (SQL, command, template, or expression injection)
- Broken access control
- Insecure direct object references
- Deserialization or unsafe object handling
- Path traversal or unsafe file handling
- Weak crypto or insecure secrets handling
- Missing validation or type constraints on input
- Unsafe defaults or permissive configuration
- Logging or error leakage of sensitive data

### 4. Assess exploitability and business impact
For each issue, answer:
- What is the vulnerable path?
- Who can trigger it?
- What data or action can be impacted?
- How severe is the risk in context?
- Is there a straightforward exploit path or a more constrained one?

### 5. Rank findings by risk
Use a simple severity model:
- Critical: remote execution, full unauthorized access, data breach, or privilege escalation
- High: direct attacker impact with realistic exploitability
- Medium: partial compromise, reduced confidentiality/integrity, or abuse through a privileged flow
- Low: limited impact, difficult exploitation, or defense-in-depth issues

### 6. Recommend safe remediation
- Prefer minimal, targeted fixes over broad rewrites.
- Recommend validation, authorization checks, allowlists, parameterized queries, least-privilege patterns, and secure defaults.
- Explain why the proposed fix removes the vulnerability without introducing regressions.

### 7. Validate and report clearly
Provide a review summary with:
- Finding title
- File and function or endpoint involved
- Root cause
- Exploit path
- Risk level
- Recommended fix
- Optional test or verification step

## Decision points

- If the issue is in a route or API boundary, focus on input validation, authz, and user-controlled data flow.
- If the issue is in a repository/service layer, focus on data access patterns, trust boundaries, and unsafe operations.
- If the issue is in configuration or deployment, focus on secrets management, permission defaults, and attack surface exposure.
- If the code is intentionally vulnerable demo material, describe the exploit path and remediation clearly without wiring it into the app flow.

## Quality bar

A good review result should:
- Be concrete and evidence-based
- Tie the issue to a real code path, not a vague concern
- Distinguish between actual risk and theoretical risk
- Provide a fix that is narrow, secure, and realistic
- Keep the output easy for engineers to act on

## Repo-specific guardrail

When reviewing this workspace, treat files under `demo-assets/session2/demo12-security/` as review targets only. Do not integrate or wire intentionally vulnerable demo code into the main application unless the task explicitly asks for a security exercise.

## Example prompts

- Review this repository and identify the most serious security issues.
- Find the highest-risk vulnerability in this API and explain how an attacker could exploit it.
- Audit this repository for broken access control and insecure data handling.
- Provide a security review of this PR and rank the findings by severity.
- Explain which code paths are vulnerable to injection and how to fix them.

## Related customizations

- Create a companion prompt for “PR security review”
- Create a checklist-based instruction for “security review before merge”
- Pair this with a “root cause analysis” skill for incident follow-up
