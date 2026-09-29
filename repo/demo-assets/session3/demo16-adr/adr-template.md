# ADR-NNN: [Decision title]

**Status**: Proposed | Accepted | Superseded

**Context**

What problem are we solving, and what constraints apply? (For the
Session 3 Demo 16 demo: reliably sending a notification after an
invoice is approved, without double-sending or losing notifications on
a crash.)

**Options considered**

1. Transactional outbox
2. Direct publish from the request handler
3. Polling for status changes

**Decision**

Which option was chosen, in one or two sentences.

**Consequences**

What gets easier, what gets harder, and what we're explicitly not
solving yet.
