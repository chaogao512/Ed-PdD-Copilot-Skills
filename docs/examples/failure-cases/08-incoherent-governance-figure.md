# Failure Case 08: Incoherent Governance Figure

## Weak input

“请画一个教育数据治理架构图：最底层是所有学生数据，中间是 AI 大模型，上面输出学生画像、风险预警、教师评价和领导驾驶舱。”

## Expected skill response

Use `governance-figure-designer` and `edtech-pre-submission-reviewer`.

## Expected diagnosis

- **CRITICAL: No human oversight in a high-risk education AI diagram**. Student profiles, risk warnings and teacher evaluation are high-impact uses, but the diagram has no review, appeal or accountability layer.
- **MAJOR: Data governance missing**. The figure shows data aggregation but not ownership, authorization, quality control, retention, audit or deletion.
- **MAJOR: Accountability flow missing**. Leaders receive dashboard outputs, but affected teachers and students have no explanation or correction channel.
- **MAJOR: Label language too technical**. The diagram uses “all student data” and “AI big model” instead of educational purpose, data boundary and governance responsibility.

## Required repair

Redesign the figure as a data governance responsibility map:

1. Add data subject, data steward, data user and oversight body.
2. Separate data flow, authorization flow, decision flow, accountability flow and feedback flow.
3. Add data minimization, access control, quality review, risk assessment, audit trail and retention/deletion.
4. Treat AI output as decision-support evidence requiring teacher or committee review.
5. Add explanation, correction and appeal channels for affected students and teachers.

