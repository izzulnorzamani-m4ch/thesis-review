# University requirements and examiner comments

Students often have two kinds of documents that matter more than any generic standard:

- **University requirements** — thesis/dissertation guidelines, formatting and submission rules, the faculty's marking rubric or examiner report form, programme handbook sections, supervisor checklists.
- **Examiner or panel comments** — from the proposal defense, a progress/candidature review, a pre-viva or viva, or a previous round of corrections. They may arrive as a typed list, a filled-in form, minutes, an email, or as comments and annotations inside the student's PDF or Word file.

When the student provides either, they take priority over generic best practice, because these are the standards the student will actually be judged against. This reference explains how to use them.

## Contents
1. Extracting the documents
2. University requirements: building and checking the requirements register
3. Examiner comments: building and checking the comments register
4. When sources disagree
5. Report sections
6. Coaching boundaries for responses to examiners

---

## 1. Extracting the documents

- Plain documents (PDF, Word, text): extract with `scripts/thesis_map.py <file> --out <dir>` and read `thesis_text.txt`, or read them directly if short.
- **Comments embedded in a file** (Word comments, PDF sticky notes/highlights with notes, tracked-change comments): run `scripts/extract_comments.py <file>`. It lists each comment with its author, page (PDF) and the text it's attached to. Embedded comments are easy to miss by reading the text alone — always run it on any PDF or Word file that might be annotated.
- **Scanned or handwritten** forms: if text extraction returns little or nothing, view the pages as images and transcribe the comments. If handwriting is illegible, list the comment as "illegible — please confirm" rather than guessing.

Identify for each document: what it is (guideline, rubric, comments), who wrote it, the stage (proposal defense, viva, etc.) and its date. A comment from the proposal stage may be about chapters that have since changed.

## 2. University requirements register

Turn the guidelines into a list of **checkable requirements**. Skip general exhortations ("the thesis should be of high quality") and keep things that can be verified:

- Structure: required chapters/sections and their order, required front matter (declaration, abstract in one or two languages, acknowledgements, ethics approval page), appendices.
- Limits: word/page limits overall and per part (abstract length is a common one), number of keywords.
- Formatting: font, size, spacing, margins, page numbering, heading style, table/figure captions. You can only check formatting you can see — extracted text often loses it, so mark these "Please check in the original file" unless the file format lets you verify.
- Referencing: required style and edition.
- Content requirements: e.g. "must include a statement of contribution", "research objectives must be numbered", "limitations section required", "ethics approval number in methodology".
- Assessment criteria from a rubric or examiner form: use these instead of the generic rubric (see `rubric.md`), with their scale and weightings.

Check each requirement against the thesis and give it a status:

| Status | Meaning |
|---|---|
| Met | Evidence found; give the location |
| Partly met | Some evidence; say what's missing |
| Not met | Requirement not satisfied; say what to do |
| Can't verify | Needs the original file or information you don't have (e.g. margins, printed binding) |
| Not applicable | Requirement doesn't apply to this thesis (e.g. a lab-safety section in a humanities thesis) |

## 3. Examiner comments register

Split the comments into **individual, numbered items** — one action per item. Examiners often bundle several requests in one paragraph; separate them so none get lost. Keep the examiner's wording short (quote the key phrase, paraphrase the rest) and record who made it and where it points.

Classify each comment:

- **Required change** (e.g. "the sample size must be justified")
- **Suggestion** (e.g. "the candidate may consider…")
- **Question to answer** (often at the viva — needs an answer, sometimes also a change in the text)
- **Unclear** — the meaning is genuinely ambiguous; suggest the student clarify with their supervisor rather than guessing.

Then check the current thesis for each one:

| Status | Meaning |
|---|---|
| Addressed | The change is visible; give the location and a one-line note on how |
| Partly addressed | Something changed but not fully what was asked; say what's missing |
| Not addressed | No change found; say what the examiner will look for |
| Superseded | The thesis has changed so much the comment no longer applies (e.g. the method was replaced) — the student should still explain this in their response |
| Can't tell | Needs information you don't have (e.g. a dataset, a revised appendix not provided) |

Judge "addressed" by whether **the examiner would be satisfied**, not whether something on the topic now exists. If an examiner asked for justification of the sample size and the thesis now states the sample size again without justifying it, that's "Partly addressed" at best.

Also look for **ripple effects**: a change made for one comment can break something elsewhere (new objectives that the conclusion doesn't answer; a new instrument not reflected in the results chapter). Flag these.

Examiners also look closely at anything their comments touched. If the student addressed a comment, check the new text with the same care as the rest of the thesis.

## 4. When sources disagree

Priority order: **examiner/panel requirements → university requirements → discipline conventions → generic best practice.**

- If the university guideline differs from generic advice (e.g. it requires a separate literature review chapter in a field that often integrates it), follow the guideline and don't flag the convention as a weakness.
- If an examiner comment conflicts with a university requirement, or two examiners contradict each other, don't pick a side. Flag the conflict and suggest the student agree an approach with the supervisor before resubmitting.
- If you think an examiner's request is mistaken (it happens), still treat it as required unless the student and supervisor decide otherwise. You can note the tension respectfully and suggest how the student might address it in their response.
- Generic findings that no examiner raised still go in the report — examiners at the final stage may be different people, and the final examiners will read the whole thesis fresh.

## 5. Report sections

Add these to the report when the documents were provided (see SKILL.md for placement):

```
## Examiner comments: response check
Source: [e.g. Proposal defense panel, 12 March 2026 — 3 examiners, 18 comments]
Summary: X addressed · Y partly · Z not addressed · W superseded/can't tell

| # | Examiner | Comment (short) | Type | Status | Where / what's still needed |
|---|---|---|---|---|---|

## University requirements check
Source: [e.g. Faculty of Education Thesis Guidelines 2025, rubric form PG-07]
Summary: X met · Y partly · Z not met · W can't verify

| Requirement | Status | Evidence / action |
|---|---|---|
```

Put unaddressed and partly addressed items into **Top priorities** too — an examiner who sees their earlier comment ignored is far less forgiving than one meeting a new problem.

When the student's university rubric was provided, the **Rubric summary** uses that rubric's criteria, scale and weightings (and a total if the rubric uses one), and says so.

## 6. Coaching boundaries for responses to examiners

Many universities require a **corrections table** or response letter. You can:

- give the student the tracking table above as the skeleton for it,
- explain what a good response entry contains (what was asked → what was changed → where, with page/section),
- point out where a response would need to justify *not* making a change, and what kind of justification examiners usually accept (evidence, citations, scope).

Don't write the student's responses or the revised thesis text for them. The response is part of their examination; it has to be theirs.
