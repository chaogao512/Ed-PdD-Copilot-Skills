#!/usr/bin/env python3
"""Check basic structure for Ed-PdD-Copilot skills."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugins" / "ed-pdd-copilot" / "skills"

REQUIRED_REFERENCE_HINTS = {
    "governance-idea-evaluator": ["rubric.md", "fatal-flaws.md", "theory-anchors.md", "worked-examples.md"],
    "edtech-intro-drafter": ["four-part-logic.md", "paragraph-patterns.md", "alienation-patterns.md", "worked-examples.md"],
    "governance-paper-template": ["paper-types.md", "theory-to-design.md", "dual-topology.md", "section-skeleton.md", "worked-examples.md"],
    "mixed-methods-evidence-template": [
        "claim-evidence-matrix.md",
        "indicator-system.md",
        "quantitative-methods.md",
        "qualitative-methods.md",
        "triangulation.md",
        "method-reporting-templates.md",
        "design-science-reporting.md",
    ],
    "governance-figure-designer": ["figure-types.md", "layout-patterns.md", "label-language.md", "quality-audit.md"],
    "edtech-pre-submission-reviewer": ["review-rubric.md", "theory-policy-checklist.md", "method-evidence-checklist.md", "ethics-data-governance.md", "style-anti-patterns.md"],
    "ai-assisted-edtech-research-workflow": ["human-ai-boundary.md", "allowed-uses.md", "red-lines.md", "verification-checklist.md"],
}

REQUIRED_DOCS = [
    "docs/evidence-base.md",
    "docs/literature-map-edtech-governance.md",
    "docs/skill-coverage-matrix.md",
    "docs/case-multi-agent-smart-campus.md",
    "docs/review-2026-06-23-v0.4.md",
    "CHANGELOG.md",
]

REQUIRED_EXAMPLES = [
    "docs/examples/01-governance-idea-evaluator-output.md",
    "docs/examples/02-governance-paper-template-output.md",
    "docs/examples/03-edtech-intro-drafter-output.md",
    "docs/examples/04-mixed-methods-evidence-output.md",
    "docs/examples/05-governance-figure-designer-output.md",
    "docs/examples/06-edtech-pre-submission-review-output.md",
    "docs/examples/07-ai-assisted-workflow-output.md",
    "docs/examples/failure-cases/01-technology-first-idea.md",
    "docs/examples/failure-cases/02-evidence-mismatch.md",
    "docs/examples/failure-cases/03-decorative-theory.md",
    "docs/examples/failure-cases/04-policy-sloganization.md",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def main() -> int:
    if not SKILLS.exists():
        fail(f"Missing skills directory: {SKILLS}")

    failures = []
    for rel in REQUIRED_DOCS + REQUIRED_EXAMPLES:
        path = ROOT / rel
        if not path.exists():
            failures.append(f"missing required project artifact: {rel}")
        elif len(path.read_text(encoding="utf-8").strip().splitlines()) < 5:
            failures.append(f"project artifact too short: {rel}")

    coverage = ROOT / "docs" / "skill-coverage-matrix.md"
    if coverage.exists():
        coverage_text = coverage.read_text(encoding="utf-8")
        if "pending" in coverage_text.lower():
            failures.append("coverage matrix still contains pending items")

    for skill, refs in sorted(REQUIRED_REFERENCE_HINTS.items()):
        folder = SKILLS / skill
        skill_md = folder / "SKILL.md"
        agents = folder / "agents" / "openai.yaml"
        ref_dir = folder / "references"
        if not folder.exists():
            failures.append(f"{skill}: missing folder")
            continue
        if not skill_md.exists():
            failures.append(f"{skill}: missing SKILL.md")
            text = ""
        else:
            text = skill_md.read_text(encoding="utf-8")
            if not text.startswith("---\n") or f"name: {skill}" not in text or "description:" not in text:
                failures.append(f"{skill}: invalid frontmatter")
            if "TODO" in text or "placeholder" in text.lower():
                failures.append(f"{skill}: contains TODO/placeholder")
        if not agents.exists():
            failures.append(f"{skill}: missing agents/openai.yaml")
        if not ref_dir.exists():
            failures.append(f"{skill}: missing references directory")
        else:
            for ref in refs:
                path = ref_dir / ref
                if not path.exists():
                    failures.append(f"{skill}: missing references/{ref}")
                else:
                    ref_text = path.read_text(encoding="utf-8").strip()
                    if not ref_text:
                        failures.append(f"{skill}: empty references/{ref}")
                    if len(ref_text.splitlines()) < 8:
                        failures.append(f"{skill}: references/{ref} is too thin")
                    if ref not in text:
                        failures.append(f"{skill}: references/{ref} is not mentioned in SKILL.md")

    if failures:
        for item in failures:
            print(item)
        return 1
    print("OK: all Ed-PdD-Copilot skill structure checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
