# 🎓 Thesis Review: a Claude skill for thesis self-checks

**Know what your examiners will say, before they say it.**

`thesis-review` is a skill for [Claude](https://claude.ai). It reads a thesis the way a fair but demanding examiner would, then gives the student honest, prioritised, actionable feedback before submission or a defense.

It works for **PhD dissertations, master's theses, undergraduate final year projects (FYP), and single thesis statements**, in **any field** and **any language**. It can also check a thesis against **your own university's requirements** and track whether your **examiners' comments** have actually been addressed.

> It's a self-check that coaches; it doesn't ghostwrite. It tells students what's wrong, why it matters, and how to fix it, but it won't rewrite their thesis or their responses to examiners. The work stays theirs.

---

## Why

Most students get feedback too late: at the proposal defense, at the viva, or in a list of corrections. Supervisors are busy, and some problems are hard to see in your own writing:

- a research question the conclusion never actually answers
- a theoretical framework that disappears after Chapter 2
- a methodology that describes but never justifies
- an examiner's comment from the proposal defense that was quietly missed
- a date, statistic or citation that's simply wrong

This skill is built to find those problems early, while there's still time to fix them.

---

## What you get

| Section | What it tells you |
|---|---|
| **Overall readiness** | An honest verdict: *Ready to submit* · *Minor revisions* · *Major revision needed* · *Not yet ready* |
| **Rubric summary** | Ten criteria scored 1–5 relative to your level (FYP / Master's / PhD), each with a one-line reason. Or your own university's rubric, if you attach it |
| **Top priorities** | The 3–7 fixes that matter most, in order. If you only do these, do these |
| **Golden thread check** | A table tracing each research question through method, results and conclusion, which shows where the argument breaks |
| **Chapter-by-chapter feedback** | What works, plus issues rated **Critical / Major / Minor**, each with *why it matters* and *how to fix it* |
| **Fact checks** | Claims marked ✅ *Verified* (with source) or 🔎 *Please check* (with exactly where to check) |
| **Examiner comments check** | Every comment from your proposal defense or viva, marked Addressed / Partly / Not addressed, with where in the thesis |
| **University requirements check** | Each rule in your faculty guidelines marked Met / Partly / Not met / Can't verify |
| **Likely examiner questions** | Viva or panel questions grounded in *your* thesis |
| **What it couldn't assess** | An honest list of its own limits for this review |

### Example rubric (illustrative)

| Criterion | Score | Basis |
|---|---|---|
| Problem, gap and RQs | 3 | Clear question; gap overstated given the literature cited |
| Theoretical framework | 2 | Framework introduced in Ch. 1 but not used in the analysis |
| Methodology and rigour | 2 | No criteria for identifying the key concept; no case-selection rationale |
| Argument and coherence | 2 | Factors asserted rather than tested across periods |
| Referencing and integrity | 2 | 12 in-text / reference-list mismatches |
| Writing and presentation | 3 | Clear structure; recurring grammar issues |

---

## Features

- 🎯 **Calibrated to your level.** An FYP isn't judged like a PhD. "Good" means different things at each level.
- 🔬 **Works across disciplines.** Field-specific guidance for sciences, engineering and computing, maths, health (CONSORT, STROBE, COREQ, PRISMA…), quantitative and qualitative social science, education, business and economics, humanities, law, creative and practice-based research, and systematic reviews.
- 🌏 **Multilingual.** Reviews theses in English, Bahasa Melayu, Indonesian, Chinese, Arabic, French, Spanish and more. The report comes in the language you write to it in, and writing is judged by the conventions of the thesis's own language. It also checks that bilingual abstracts (e.g. *Abstrak* and *Abstract*) say the same thing.
- 🏛️ **Your university's rules.** Attach your faculty guidelines or marking rubric and it checks against those, not generic advice.
- 📝 **Your examiners' comments.** Attach the proposal defense or viva comments as a list, a form, minutes, or **comments embedded in your PDF or Word file** (it extracts those automatically). It then checks each one.
- ✅ **Fact-checking.** Verifies the claims your argument depends on (when web search is available) and tells you where to check the rest.
- ⚖️ **Fair on contested topics.** It judges how well a position is argued, never whether it agrees with it.
- 📏 **Quality over quantity.** It judges the strength of the argument, not the length. Report length follows how serious the issues are.

---

## Installation

### Claude app (web, desktop, mobile)

Requires a Pro, Max, Team or Enterprise plan with **code execution** enabled.

1. Download **`thesis-review.zip`** from the [Releases](../../releases) page. Don't unzip it.
2. In Claude, go to **Settings → Capabilities** and upload the zip under **Skills**.
3. Make sure the skill is toggled **on**.

On Team or Enterprise plans, your admin may need to allow custom skills.

### Claude Code

```bash
git clone https://github.com/<your-username>/thesis-review.git
cp -r thesis-review/thesis-review ~/.claude/skills/
```

---

## How to use it

Attach your thesis (PDF or Word) and just ask. No special commands needed.

```
Can you check my master's thesis before I submit? Be honest.
```
```
This is my FYP methodology chapter. Panel presentation in 2 weeks. Is it good enough?
```
```
Here's my thesis, my faculty's thesis guidelines, and the comments from my
proposal defense. Have I addressed everything?
```
```
Tolong semak tesis PhD saya. Adakah ia sudah sedia untuk dihantar?
```
```
Is my thesis statement okay? "Social media has both positive and negative effects on students."
```

**Tips**
- Attach the **whole thesis** if you can. The most serious problems often only show up across chapters.
- Attach your **university's rubric or guidelines** and **examiner comments** for a review that matches how you'll actually be assessed.
- Say your **level** (FYP / Master's / PhD) if it isn't obvious from the title page.

---

## What's inside

```
thesis-review/
├── SKILL.md                                  # the workflow Claude follows
├── references/
│   ├── level-expectations.md                 # FYP vs Master's vs PhD
│   ├── chapter-criteria.md                   # what each part of a thesis must do
│   ├── discipline-notes.md                   # field-specific standards of rigour
│   ├── rubric.md                             # 10-criterion summary rubric
│   ├── institution-and-examiner-inputs.md    # university rules + examiner comments
│   ├── language-notes.md                     # non-English and bilingual theses
│   └── thesis-statement.md                   # quick mode for essay thesis statements
└── scripts/
    ├── thesis_map.py                         # maps chapters, word counts, figures, references
    └── extract_comments.py                   # pulls examiner comments out of PDF / Word files
```

---

## Evaluation

> **Status: beta.** Tested on 7 cases across 6 fields; see [EVALUATION.md](EVALUATION.md) for the full method, results and limitations.

In a planted-flaw test (1 real thesis + 5 constructed chapters, in English and Bahasa Melayu, from FYP to PhD), reviewers using the skill found **all 48 known flaws**, with **no false alarms** on a clean control chapter.

To be transparent: **plain Claude without the skill also found all 48.** On these flaws the skill didn't find more. What it adds is:

- the same structured report every time: verdict, rubric, priorities, alignment check, examiner questions;
- fact checks backed by cited sources;
- level-calibrated scoring;
- checks against your university's rules and your examiners' comments (not covered by this test).

Harder tests and comparisons with real examiner reports are next. Contributions welcome.

## Responsible use

- **A self-check, not an examination.** The readiness verdict is a judgement on how examiners are *likely* to read the thesis, not a prediction of their decision.
- **Your supervisor comes first.** Use this to prepare for supervision meetings, not to replace them. Specialist technical correctness (a complex proof, a lab protocol, a novel legal argument) still needs a human expert.
- **Academic integrity.** The skill explains problems and how to fix them. It won't write thesis sections or responses to examiners for you. Check your university's policy on AI use, and declare it where required.
- **Privacy.** Unpublished theses and examiner reports can be sensitive. Follow your institution's rules on sharing them with AI tools.
- **AI can be wrong.** Treat every finding as something to check, especially *Please check* items.

---

## Contributing

Contributions are very welcome, especially:

- **Discipline notes** for fields that aren't well covered yet
- **Language notes** on the academic writing conventions of other languages
- **Real-world feedback.** Where did the review miss something, or flag something that's normal in your field?
- **Heading vocabulary** for `thesis_map.py` in more languages

Open an issue or a pull request.

---

## License

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

Licensed under [Creative Commons Attribution-NonCommercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You're free to use, share and adapt this skill for **non-commercial** purposes with credit. For commercial use (paid services, courses, products or institutional deployment), contact the author for a commercial licence. See [LICENSE](LICENSE).

## Author

Created by Izzul Norzamani ([@izzulnorzamani-m4ch(https://github.com/izzulnorzamani-m4ch)). Built with Claude.

If this helped you, ⭐ the repo and share it with someone who's writing up.
