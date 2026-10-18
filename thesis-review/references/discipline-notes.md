# Discipline notes

The criteria in `chapter-criteria.md` describe functions every thesis must perform. *How* a field performs them differs, and judging one field by another's conventions produces bad feedback (asking a historian for a sample-size justification, or a chemist for a positionality statement). Find the closest family below, read it, and adjust your expectations. Many theses mix families (e.g. a health-services thesis with a qualitative strand); apply each to the relevant part.

If the field isn't listed, reason from the nearest family and from the thesis's own stated methods. Don't invent conventions — when unsure, describe the issue in general terms and suggest the student check with their supervisor.

## Contents
1. Natural and life sciences (experimental / lab / field)
2. Engineering and computing (design, build, evaluate)
3. Mathematics, theoretical physics, theoretical CS
4. Health, medicine, nursing and allied health
5. Social sciences — quantitative
6. Social sciences — qualitative and interpretive
7. Education
8. Business, management and economics
9. Humanities (history, literature, philosophy, religion, languages)
10. Law
11. Creative arts, design and practice-based research
12. Systematic reviews and meta-analysis as theses

---

## 1. Natural and life sciences

- **Structure:** often IMRaD per chapter or thesis-by-publication; literature review may be compact.
- **What rigour means:** controls, replication (biological vs technical), randomisation/blinding where applicable, calibration, uncertainty and error propagation, appropriate statistics, sufficient methods detail to reproduce (reagents, strains, instruments, settings, software versions).
- **Evidence checks:** figures with error bars defined, n stated, statistical tests named; images unmanipulated beyond accepted practice; raw data/code availability statement.
- **Common problems:** p-values without effect sizes; pseudo-replication; over-interpreting non-significant results; discussion that restates results; methods "as previously described" with no citation detail.
- **Ethics/compliance:** animal ethics, biosafety, field permits, data deposition where required.

## 2. Engineering and computing

- **Structure:** problem → requirements → design → implementation → testing/evaluation → discussion. Design-science and software-engineering models are common methodologies.
- **What rigour means:** requirements traced to the problem; design decisions justified against alternatives; evaluation that tests the claims (benchmarks, baselines, ablations, usability studies, field trials) rather than "it works".
- **Evidence checks:** baselines are fair and current; datasets described with splits and provenance; metrics suit the task; results include variance across runs; threats to validity discussed; code/data availability.
- **Common problems:** feature lists presented as contribution; no comparison with existing solutions; evaluation only by the developer; testing confused with evaluation; screenshots in place of analysis.
- **Ethics:** user studies need ethics approval; data protection for personal data; responsible AI considerations where relevant.

## 3. Mathematics, theoretical physics, theoretical CS

- **Structure:** definitions → known results → new results (theorems, proofs, derivations) → discussion.
- **What rigour means:** correctness and completeness of proofs; clear statement of assumptions; notation consistent; new results clearly distinguished from known ones.
- **Your limits:** you can check structure, clarity, whether results are stated precisely and whether claimed contributions are distinguished from prior work. Verifying every step of a long proof is beyond a reliable review — flag steps that look unjustified and recommend the supervisor or a specialist check the core proofs.
- **Common problems:** contribution buried; "it is easy to see" hiding real gaps; examples missing; literature positioning too thin.

## 4. Health, medicine, nursing and allied health

- **Reporting guidelines matter:** CONSORT (trials), STROBE (observational), COREQ/SRQR (qualitative), PRISMA (reviews), STARD (diagnostic), TRIPOD (prediction models). Check the thesis follows the relevant one and say which items are missing.
- **What rigour means:** clear population/intervention/comparison/outcome; sample size calculation; handling of confounding, missing data and bias; clinical vs statistical significance.
- **Ethics:** ethics approval number, consent, trial registration where required, patient confidentiality.
- **Common problems:** causal language from observational data; outcomes changed from protocol; implications for practice overstated.

## 5. Social sciences — quantitative

(psychology, sociology, political science, quantitative education/business research)

- **What rigour means:** constructs operationalised; instrument validity and reliability; sampling and sample size justified; model assumptions checked; appropriate analysis (regression, SEM, multilevel etc.) with diagnostics; effect sizes.
- **Common problems:** convenience samples generalised to populations; Likert-scale analysis choices unjustified; SEM fit indices cherry-picked; common-method bias ignored; hypotheses written after results.

## 6. Social sciences — qualitative and interpretive

(including case studies, ethnography, discourse and textual analysis, historical-comparative political science)

- **What rigour means:** case/participant selection justified; data sources and corpus defined; analysis procedure transparent (coding, themes, process tracing); trustworthiness; reflexivity/positionality where the tradition expects it.
- **Key test for argument-driven work:** are central concepts defined so that evidence could count *against* the claim? Are alternative explanations considered?
- **Common problems:** themes that are just topic headings; quotations without analysis; concepts left vague; method described in the introduction but not visible in the analysis; heavy reliance on secondary sources presented as primary analysis.

## 7. Education

- Mix of quantitative, qualitative, mixed-methods and design-based research (e.g. ADDIE, design-based research cycles), so read §5, §6 and §2 as needed.
- **Specifics:** intervention studies need a clear comparison and implementation fidelity; instrument adaptation (translation, back-translation, expert validation) documented; ethics for minors and institutional permissions.
- **Common problems:** perception surveys used to claim effectiveness; developmental studies with no real evaluation; pre/post designs without control interpreted causally.

## 8. Business, management and economics

- **Business/management:** often theory-testing quantitative (§5) or case-based qualitative (§6). Expect managerial as well as theoretical implications; check the theory actually generates the hypotheses.
- **Economics:** identification strategy is central — how does the design isolate the causal effect (IV, DiD, RDD, RCT, structural model)? Robustness checks, data sources, and model specification justified.
- **Common problems:** "implications for managers" generic; endogeneity unaddressed; secondary financial data without cleaning description.

## 9. Humanities

- **Structure:** usually thematic chapters building one argument; literature woven through; methodology may be an "approach" section.
- **What rigour means:** command of primary sources (texts, archives, artefacts) and their context; careful close reading; engagement with the scholarly debate; originality of interpretation; precise use of evidence and quotation; for philosophy, validity of arguments and engagement with strongest objections.
- **Don't expect:** hypotheses, sampling, IMRaD, or a separate methods chapter.
- **Common problems:** description or plot summary instead of argument; secondary sources doing the interpretive work; thesis stated late or vaguely; chapters that don't build on each other.

## 10. Law

- **Methods:** doctrinal (what the law is), socio-legal/empirical, comparative, theoretical/critical. Expect the method to be named and fitted to the question.
- **What rigour means:** accurate statement of law with correct citation of cases and legislation (correct jurisdiction, current law at the stated date); critical analysis rather than description; for comparative work, justified choice of jurisdictions.
- **Citation:** usually OSCOLA, the Bluebook, AGLC or a national style — check consistency.
- **Common problems:** descriptive survey of cases; outdated law; normative recommendations not grounded in the analysis.

## 11. Creative arts, design and practice-based research

- **Structure:** a creative or practical component plus an exegesis/dissertation.
- **What rigour means:** the research question is answered *through* practice; the exegesis contextualises the work in its field, documents the process, and reflects critically on what the practice revealed.
- **Your limits:** you usually only see documentation of the practice. Assess the exegesis and its relation to the work, and say you can't judge the work itself from documentation alone.
- **Common problems:** exegesis that describes the work but doesn't make a research claim; contextual review that's a list of influences.

## 12. Systematic reviews and meta-analyses as theses

- Check against PRISMA 2020: protocol/registration, search strategy reproducible, screening by two reviewers, risk-of-bias assessment, synthesis method, certainty of evidence (e.g. GRADE).
- **Common problems:** search too narrow or undated; quality appraisal missing; narrative synthesis that lists studies; conclusions stronger than the evidence certainty allows.
