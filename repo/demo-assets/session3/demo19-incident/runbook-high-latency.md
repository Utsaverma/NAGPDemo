# Runbook: API p95 latency above 2s

**Trigger**: alerting rule fires when p95 request latency exceeds 2000ms
for 5 consecutive minutes.

## Step 1 - Confirm the scope
- Check whether latency is elevated across all endpoints or one route.
- Check the last deploy timestamp against when latency started rising.

## Step 2 - Check the database connection pool
- Look for "Connection pool exhausted" warnings in the API logs.
- Note the pool's configured max size and current in-use/waiting counts.

## Step 3 - Check recent config changes
- Diff the last deploy's `appsettings.json` against the previous
  release for `Database.CommandTimeoutSeconds` and
  `Database.MaxPoolSize` specifically - these have caused this alert
  before.

## Step 4 - Remediation options (require approval before acting)
- **Rollback** the most recent release if the timing correlates
  exactly with a deploy.
- **Hotfix config**: raise `MaxPoolSize` and
  `CommandTimeoutSeconds` back toward previous values without a full
  rollback, if the only regression is those two settings.
- **Scale out**: add API replicas if the pool exhaustion is due to
  genuine increased load rather than a config regression.

## Step 5 - Postmortem
- File a postmortem within 24 hours covering timeline, root cause,
  and the check that should be added to prevent recurrence (e.g. a
  config-diff gate in CI for `Database.*` settings).
