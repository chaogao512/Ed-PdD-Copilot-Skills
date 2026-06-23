# Failure Case Regression Protocol

This folder contains weak inputs used to test whether the skills can detect, downgrade or reject common failure patterns.

## Required Fields

Each failure case should include:

1. Weak input.
2. Expected skill response.
3. Expected diagnosis.
4. Required repair.

## Failure Cases

| File | Target skill | Expected severity | Must not output |
|---|---|---|---|
| `01-technology-first-idea.md` | `governance-idea-evaluator` | CRITICAL | Do not score as a strong idea before reframing governance problem and ethics |
| `02-evidence-mismatch.md` | `mixed-methods-evidence-template`, `edtech-pre-submission-reviewer` | CRITICAL | Do not accept technical metrics as proof of education or governance value |
| `03-decorative-theory.md` | `governance-paper-template` | MAJOR | Do not let theory remain a label without design consequences |
| `04-policy-sloganization.md` | `edtech-intro-drafter`, `edtech-pre-submission-reviewer` | MAJOR | Do not accept policy slogans without concrete governance contradiction |

## Future Test Expansion

- Add privacy failure case.
- Add teacher digital fatigue failure case.
- Add overclaimed causal conclusion failure case.
- Add fabricated citation / AI misconduct case.
