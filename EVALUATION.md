# Evaluation: Thesis Review skill (v1.0)

*Planted-flaw evaluation, October 2026. A first, small-scale study. Read the limitations before quoting the numbers.*

## Summary

- **Detection:** reviewers using the skill found **all 42 deliberately planted flaws** across 6 test cases in 6 fields, plus all 6 known errors already present in a real thesis. They raised **no false alarms** on a clean control chapter.
- **The same model without the skill also found all of them.** On flaw detection, the skill did not outperform plain Claude in this test.
- **What the skill adds** is how the review is delivered:
  - a consistent structure: readiness verdict, rubric, priorities, alignment check, examiner questions, and a statement of limits;
  - fact checks verified with **cited sources** instead of from memory;
  - level-calibrated scoring;
  - features this test did not cover: checks against university rules and against examiner comments.
- **Cost:** with the skill, reviews used about 30% more processing and took about twice as long, mostly because of web fact-checking.

## Method

**Test set.** Seven cases:

| # | Case | Field / level | Language | Source | Planted flaws |
|---|---|---|---|---|---|
| 1 | Political science thesis | MA (research) | English | Real, publicly available thesis (~28,000 words) | 5 planted + 6 known pre-existing errors |
| 2 | Education, Abstrak + Ch. 1 + Ch. 3 | Master's | Bahasa Melayu (bilingual abstract) | Constructed | 8 |
| 3 | Public health, methods + results + discussion | MSc | English | Constructed | 8 |
| 4 | Computing, methodology chapter | Undergraduate FYP | English | Constructed | 7 |
| 5 | Law, doctrinal/comparative chapter | LLM | English | Constructed | 8 |
| 6 | History chapter | PhD | English | Constructed | 6 |
| 7 | **Clean control**: revised version of case 4 | Undergraduate FYP | English | Constructed | 0 (should not raise serious issues) |

**Planted flaws** covered the problems examiners most often raise:

- **Inconsistencies:** abstract vs body, tables vs text, percentages summing to 105%.
- **Factual errors:** dates, courts, laws already amended.
- **Statistical misreporting:** p = 0.18 called "significant"; sample size misread from Krejcie & Morgan.
- **Design and claims:** causal claims from cross-sectional data; generalisation beyond the sample.
- **Alignment:** objectives with no method; a methodology label that doesn't match the process; a conclusion that contradicts the thesis argument.
- **Integrity and ethics:** new data introduced in a conclusion; missing ethics and privacy provisions.
- **Referencing:** citations missing from the reference list.

**Procedure.**

- Each case was given to **two independent Claude reviewers**: one with the skill, one without. Neither saw the answer key.
- Each reviewer received only the document and a realistic student request, in Malay for case 2.
- One run per condition. The model was Claude Opus 5.5 (the same model in both conditions).

**Scoring.** A flaw counted as detected only if the report identified that specific problem, not just the general area. Scoring was done against a fixed answer key written before the runs.

## Results

### Detection

| Case | Planted | With skill | Without skill |
|---|---|---|---|
| 1. Political science MA (planted) | 5 | 5 | 5 |
| 1. Political science MA (pre-existing errors) | 6 | 6 | 6 |
| 2. Education master's (BM) | 8 | 8 | 8 |
| 3. Public health MSc | 8 | 8 | 8 |
| 4. Computing FYP | 7 | 7 | 7 |
| 5. Law LLM | 8 | 8 | 8 |
| 6. History PhD | 6 | 6 | 6 |
| **Total** | **48** | **48 (100%)** | **48 (100%)** |

### Clean control (case 7)

| | With skill | Without skill |
|---|---|---|
| Verdict | Ready after minor revisions | Good shape, no fatal problems |
| Serious issues that were factually wrong about the text | 0 | 0 |
| Rated clearly better than flawed version (case 4) | Yes | Yes |

### How the reviews differed

| | With skill | Without skill |
|---|---|---|
| Readiness verdict | 7 of 7, same four-level scale | Usually given, format varies |
| Rubric scores | 7 of 7 | 0 of 7 |
| Research-question alignment table | 7 of 7 | Occasionally |
| Fact checks backed by a cited source | In all 7 reviews | Rarely; mostly "from memory, please check" |
| States what it could not assess | 7 of 7 | Sometimes |
| Report language matched the student (Malay case) | Yes | Yes |
| Average processing used | ~119,000 tokens | ~91,000 tokens |
| Average time | ~4.8 min | ~2.5 min |

## What this means

1. **Claude is already a strong thesis reviewer for clear-cut problems.** Anyone telling you the skill finds problems Claude "would otherwise miss" is overselling it, at least for flaws like these.
2. **The skill's value is consistency, verifiability and fit to how theses are actually examined.** Every review has the same structure, scores calibrated to the student's level, priorities in order, cited fact checks, and an honest statement of limits. It also handles things a plain request doesn't set up: checking against a university's own rules and rubric, and tracking examiner comments (including comments embedded in PDF and Word files). Neither was tested here.

## Limitations

- **Small and mostly constructed.** One real thesis plus five constructed chapters, all written by the skill's developer, with one run per condition. Real theses are longer and messier, and their problems are subtler.
- **Planted flaws may be too easy.** Both conditions scored 100%, which suggests a ceiling effect. Subtler flaws (e.g. a weak but not wrong theoretical choice) would discriminate better.
- **Not compared with human examiners.** We don't yet know how closely the reviews match what real examiners say, or whether readiness verdicts predict actual outcomes.
- **Not independently scored.** The answer key and the scoring were done by the developer, not by blinded experts.
- **Untested features.** University-rules and examiner-comment checking were not part of this evaluation.

## Next steps

- Compare skill reviews with real examiner reports, with consent and ethics approval.
- Use harder, subtler flaws and multiple runs per case.
- Independent expert rating of review quality.
- Collect real-world outcomes through the [feedback form](#) (does the readiness verdict match how examination went?).

*Help wanted:* if you're a supervisor or examiner willing to contribute anonymised theses and examiner reports, please get in touch.
