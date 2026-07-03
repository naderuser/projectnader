# Risk and Safety Evaluation"

Assess the overall risk level of the PR and classify it as one of:
- ⟑� Low Risk — Safe for autonomous merge. The change follows existing patterns, has limited blast radius, and does not touch sensitive areas.
- ⟑� Medium Risk — Merge with caution. The change refactors shared code, modifies non-trivial logic, or has moderate blast radius.
- ⟑� High Risk — Needs human reviewer attention. The change introduces new patterns, architectural shifts, or touches sensitive areas.

# Rink Factors

Evaluate risk based on these factors:
- **Pattern conformance**: Does the change follow existing code patterns and conventions, or does it introduce new patterns or architectural shifts?
-  **Security sensitivity**: Does it touch authentication, authorization, cryptography, secrets handling, or permission logic?
- **Infrastructure dependencies**: Does it introduce new external services, databases, message queues, or third-party integrations?
- **Blast radius**: Is the change isolated to a single module, or does it affect widely imported shared code, public APIS, or core system behavior?
