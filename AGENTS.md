# AGENTS

## AI Collaboration Conventions

This file documents a **recommended** workflow for AI-assisted analysis, writing, and ideation in this repository. It is **not mandatory**, but teams have reported better decision traceability when following these protocols.

### When to Use This Workflow
- **Recommended for:** Complex analysis, high-stakes decisions, multi-stakeholder projects, anything requiring rollback or audit trail
- **Overkill for:** Quick fixes, low-risk iterations, solo spike work, reversible changes, prototyping

### Core Principles (With Rationale)
- **Explicitness** — Naming assumptions upfront prevents misalignment. Undocumented assumptions become invisible until they cause failure.
- **Traceability** — Linking decisions to source data enables auditability, rollback, and learning from past choices
- **Iterability** — Structured feedback loops reduce rework *on decisions that might change*. Not all decisions benefit from iteration.
- **Separation of Concerns** — Keeping briefs, analysis, and decisions distinct prevents confusion of fact, interpretation, and judgment

### Session Workflow

1. **Before** — Write a brief (scope, hypothesis, success criteria)
   - *Cost:* ~30 minutes per project
   - *Benefit:* Prevents scope creep, aligns team, clarifies what success looks like
   
2. **During** — Use AI for ideation, code, analysis, writing
   - *Log critical decisions:* What did you ask? What assumptions did you make? What did you reject?
   
3. **After** — Document decision/recommendation with rationale
   - *Include:* What changed your mind? What data supported this? What would falsify it?
   
4. **Log** — Record significant sessions in `prompt-log.md`
   - *Significant = decision that affects scope, timeline, deliverables, or budget*

### File Organization
- `docs/briefs/` — Pre-work planning (hypothesis, scope, deliverables, success criteria)
- `docs/decisions/` — Post-work documentation (findings, recommendations, rejected hypotheses and why)
- `data/` — Source materials with attribution and access dates
- `analysis/figures/` — Charts, models, outputs, and version history
- `capabilities/` — Full capability documentation (spec + implementation)

### Documentation Standards
- Markdown format throughout
- **Tag all claims:** Mark each statement as [SUPPORTED], [ASSUMPTION], or [REJECTED]
- Include source/provenance for data with dates and access methods
- Use version numbers (v1.0, v1.1) for iterative work
- Cross-reference related documents
- For rejected hypotheses: explain why and what you learned

### How to Know If This Protocol Succeeded
This workflow is **falsifiable**. You should only use it if you can commit to measuring one of these:
- **Time to decision:** Does following this protocol make decisions faster or slower?
- **Decision reversals:** Are decisions made with this protocol reversed less often?
- **Rework hours:** Do projects spend less time fixing "wrong direction" mistakes?
- **Stakeholder alignment:** Do reviewers spend less time requesting clarification?
- **Audit readiness:** Can you trace each decision back to data and assumptions?

Pick one metric. Track it. If this protocol doesn't improve it, stop using it.

### Limitations of This Protocol
- **Overhead cost:** Add ~2–3 hours per project. True cost only justified if decision stakes are high.
- **Not universal:** Works better for analysis than for rapid prototyping.
- **Assumes good-faith documentation:** If people skip steps or write fake rationales, the protocol fails.
- **Requires agreed-upon definitions:** What counts as "significant"? What's an acceptable assumption? Define these with your team first.

### Add Custom Conventions Below
[Your specific AI collaboration guidelines here]
