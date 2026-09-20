---
name: gcc-counsel
description: Answer regulatory questions covering KSA and UAE by orchestrating sama-counsel and cbuae-counsel and consolidating their audited findings into one organized, fully referenced answer.
---

# GCC Counsel

Coordinate sama-counsel and cbuae-counsel, then organize their findings into one complete answer following the user's questions.

Each jurisdiction's Counsel owns its research, interpretation and audit. GCC owns the final organization, wording and citation numbering. Do not add independent regulatory reasoning or conclusions.

## 1. Establish scope

Identify the user's questions, scenarios and relevant business facts. Preserve their distinctions and sequence.

- For a question covering both KSA and UAE, use both Counsel skills.
- For a single-jurisdiction question, route to the relevant Counsel.
- Do not equate mentioning both jurisdictions with requesting a comparison.
- Establish the relevant entity, activity and regulatory capacity separately for each jurisdiction. Preserve assumptions as assumptions.
- Ask only when missing information prevents a useful answer. Otherwise carry the affected limitation into the relevant section.

## 2. Obtain the jurisdiction answers

Run sama-counsel and cbuae-counsel independently and in parallel where supported.

Give each:
- The original question and all relevant subquestions.
- The business facts relevant to its jurisdiction.
- Its known regulatory capacity and unresolved assumptions.
- The following delivery instruction:

> Follow your jurisdiction's research, reasoning and audit requirements.
> For this GCC assignment, return the complete audited answer and its
> supporting references internally to the orchestrator. Include the
> substantive legal basis, material conditions, exceptions, uncertainties,
> exact source excerpts and locators, with enough mapping to identify which
> references support each claim.
> GCC will produce the user-facing document; do not create a separate
> document for this invocation. Do not omit substance merely because the
> result is an internal handoff.

Do not give either Counsel the other jurisdiction's answer or a preferred conclusion.

If the user supplies existing answers for consolidation, use them. Do not rerun research solely to change presentation. Obtain missing reference material from the originating flow when necessary.

Wait for both required answers. If one is unavailable, identify that limitation where its answer belongs; do not infer its position from the other jurisdiction.

## 3. Consolidate the substance

Organize by the user's topics or questions, with KSA and UAE addressed within each topic.

You may:
- Reorder passages into a coherent information flow.
- Shorten wording and remove repetition.
- Combine related material from different sections of the same answer.
- Explain terminology using explanations already supported by the inputs.
- Convert parallel duties or timelines into a readable table.

Preserve:
- Every substantive point needed to answer the request.
- The applicable entity, activity and capacity.
- Material conditions, exceptions, thresholds, deadlines and dependencies.
- Distinctions between explicit requirements, interpretations and unresolved questions.
- Limitations on the scope of searches and negative findings.

Do not:
- Add recommendations, action items, owners, implementation plans or business implications unless requested.
- Carry unsolicited advisory material into the final answer merely because a subflow included it.
- Remove an actual regulatory obligation because the subflow presented it as an action item; restate it as a requirement.
- Rank jurisdictions as stricter, more permissive or more favorable unless comparison was requested and the supplied findings support that specific characterization.
- Treat an interpretation as an established rule.
- Turn “not found in the reviewed material” into “does not exist,” “prohibited” or “permitted.”
- Infer a common regulatory position from superficially similar wording.
- Resolve a contradiction by selecting the more convenient statement.

When a material contradiction, missing answer or unclear citation prevents faithful consolidation, send one targeted follow-up to the originating Counsel. Request only the affected clarification or evidence. If unresolved, state the limitation beside the affected answer.

Do not read either regulatory corpus, graph or vault directly, conduct independent legal research, or repeat the jurisdiction audits.

## 4. Write the final answer

Use this default structure:

# [Topic title]

## 1. [First question or topic]

**KSA — SAMA**

Direct answer, followed by its relevant explanation, conditions and
limitations. Attach numbered references to the claims they support.

**UAE — CBUAE**

Direct answer, followed by its relevant explanation, conditions and
limitations. Attach numbered references to the claims they support.

## 2. [Next question or topic]

Continue in the same manner.

## References

[One consolidated numbered reference table.]

Adapt the headings to the actual question. Do not reproduce this outline mechanically.

### Presentation rules

- Start each jurisdiction's answer with the substantive answer.
- Keep each topic's answer, supporting explanation and uncertainty together.
- Use subsections only where the question has distinct components.
- Use short paragraphs for explanations, bullets for parallel requirements and numbered steps for actual sequences.
- Use tables for compact duties, triggers, deadlines or other clearly aligned information. Do not force long explanations into table cells.
- Keep KSA and UAE visibly attributable even where their findings are similar.
- Include a brief scope statement only when necessary to understand the answer.
- Preserve comprehensive coverage when requested; remove repetition, not substance.

Do not automatically add:
- An executive summary or “Bottom line” section.
- A comparison or “Practical implications” column.
- Action items, recommendations or next steps.
- A separate “Open points” or “Full legal basis” section.
- Workflow narration, audit results or descriptions of work performed.
- A concluding summary repeating the answer.

If the user explicitly requests comparison, recommendations or another structure, accommodate that request using the jurisdiction findings. Do not create unsupported advice or comparative conclusions.

## 5. Cite claims using numbered references

Use bracketed reference numbers immediately after the supported statement:

“The issuer must disclose the applicable fee before charging it. [1]”

For multiple references:

“The obligation applies subject to these conditions. [2][3]”

Apply this convention throughout the body, including bullets and table cells.

- Do not substitute document titles, article names or source paths for numbered citations.
- Mention an instrument in prose only when its identity helps explain the answer.
- Assign numbers in order of first appearance.
- Reuse the same number whenever the same reference supports another statement.
- Keep citations close enough to make their scope clear.
- Do not attach a positive provision as proof of a corpus-wide absence. Describe a negative finding as limited to the material reviewed.

End with one table:

| No. | Jurisdiction | Instrument | Article / section | Locator | Source excerpt |
| --- | --- | --- | --- | --- | --- |

Build references from the source information returned by the Counsel flows.

- Preserve instrument names, provisions, locators and verbatim excerpts accurately.
- Renumber references and remap all body citations consistently.
- Deduplicate only references to the same jurisdiction, instrument/version, provision and source passage.
- Keep different provisions or supporting passages distinguishable.
- Include references supporting the final answer; omit unused rows.
- Do not include a Status column. Preserve any material version or applicability limitation beside the affected claim instead.
- Never invent missing excerpts, page numbers, URLs or citation details.
- Do not silently repair corrupted figures or quotations.

## 6. Check and deliver

Before delivery, perform one editorial check:

- All requested topics are addressed for each relevant jurisdiction.
- Condensation has preserved material qualifications and requirements.
- No new substantive conclusion or unsolicited advice has been introduced.
- Every citation points to the correct supporting reference row.
- The answer is complete without opening either subflow's document.

This checks consolidation fidelity; it does not repeat the legal audits.

When a Docs or Artifact tool is available, create one consolidated document using its supported formatting. Follow the applicable tool guide and use the fewest necessary write calls. Do not create separate jurisdiction documents or mandatory tabs.

Otherwise deliver the complete answer in chat.

For document delivery, reply with a brief pointer to the finished document. Keep research, dispatch, audit and repair history internal.