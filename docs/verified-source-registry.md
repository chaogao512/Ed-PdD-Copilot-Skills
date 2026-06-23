# Verified Source Registry

> This registry separates sources that can currently support skill rules from candidate Chinese core-journal records that still require CNKI or journal-site verification. It prevents the skills from treating unverified bibliographic targets as formal citations.

## Verified and Usable Sources

| No. | Source | Type | URL | Skill use |
|---:|---|---|---|---|
| 1 | UNESCO, *Guidance for generative AI in education and research* | International guidance | https://unesdoc.unesco.org/ark:/48223/pf0000386693 | GenAI governance, privacy, age appropriateness, institutional policy |
| 2 | UNESCO, *AI competency framework for teachers* | International framework | https://unesdoc.unesco.org/ark:/48223/pf0000391104 | Teacher AI competency and professional learning |
| 3 | European Commission, *Ethical guidelines on the use of AI and data in teaching and learning for educators* | Ethical guidance | https://education.ec.europa.eu/news/ethical-guidelines-on-the-use-of-artificial-intelligence-and-data-in-teaching-and-learning-for-educators | AI/data ethics, educator and school-leader responsibilities |
| 4 | U.S. Department of Education, *Artificial Intelligence and the Future of Teaching and Learning* | Policy/report | https://www.ed.gov/sites/ed/files/documents/ai-report/ai-report.pdf | Human-in-the-loop, explainability, override, trust |
| 5 | Regulation (EU) 2024/1689, Artificial Intelligence Act | Regulation | https://data.europa.eu/eli/reg/2024/1689/oj | Risk-based AI governance, oversight, transparency |
| 6 | Hevner et al., design science research guidelines | Method source | https://en.wikipedia.org/wiki/Design_science_(methodology) | Artifact, relevance, evaluation, rigor, contribution, communication |
| 7 | Peffers et al., DSR process model | Method source | https://arxiv.org/abs/2006.02763 | Problem identification, objectives, design, demonstration, evaluation, communication |
| 8 | Delphi method overview | Method source | https://en.wikipedia.org/wiki/Delphi_method | Expert consensus, iteration, anonymized feedback, consensus reporting |
| 9 | Mixed methods / multimethodology overview | Method source | https://en.wikipedia.org/wiki/Multimethodology | Quantitative + qualitative integration and triangulation |
| 10 | National Smart Education Platform overview | Context source | https://zh.wikipedia.org/wiki/国家智慧教育公共服务平台 | Smart education platform context; not used as formal policy citation |
| 11 | NIST, *AI Risk Management Framework* | AI risk framework | https://www.nist.gov/itl/ai-risk-management-framework | AI risk identification, governance, measurement and monitoring patterns |
| 12 | OECD AI Principles | International AI principles | https://oecd.ai/en/ai-principles | Human-centred values, transparency, robustness, accountability |
| 13 | European Commission, DigCompEdu | Digital competence framework | https://joint-research-centre.ec.europa.eu/digcompedu_en | Teacher digital competence, professional engagement, teaching, assessment and learner empowerment |
| 14 | UNESCO, Recommendation on the Ethics of Artificial Intelligence | International ethics recommendation | https://www.unesco.org/en/artificial-intelligence/recommendation-ethics | Human rights, transparency, accountability, fairness and governance framing for AI |
| 15 | Education Endowment Foundation, *Effective Professional Development* | Evidence guidance | https://educationendowmentfoundation.org.uk/education-evidence/guidance-reports/effective-professional-development | Teacher professional development design, implementation and mechanism evidence |
| 16 | What Works Clearinghouse Standards Handbook | Evidence standard | https://ies.ed.gov/ncee/wwc/Handbooks | Education intervention evidence, causal claims, study quality and evidence boundaries |
| 17 | 教育部, 《教育信息化2.0行动计划》通知 | Chinese official policy | http://www.moe.gov.cn/srcsite/A16/s3342/201804/t20180425_334188.html | Chinese policy framing for education informatization and digital governance |
| 18 | 教育部, 《教师数字素养》教育行业标准发布通知 | Chinese official standard notice | http://www.moe.gov.cn/srcsite/A16/s3342/202302/t20230214_1044634.html | Teacher digital literacy/competence framing and evidence design |
| 19 | 中共中央、国务院, 《教育强国建设规划纲要（2024－2035年）》 | Chinese central policy | https://www.gov.cn/zhengce/202501/content_6999913.htm | Education strong nation, digital education and governance modernization background |
| 20 | 国家智慧教育公共服务平台 | Chinese national platform | https://www.smartedu.cn/ | Smart education platform context; distinguish platform construction from governance capability |

## Candidate Sources Not Used as Formal Citations

The entries in `docs/chinese-core-literature-inventory.md` marked `needs_cnki_verification` or `local_plan_reference` are used only as search targets and pattern prompts. They should not be cited in academic outputs until exact bibliographic metadata are verified.

## Rule for Future Edits

When adding a source-based rule to a skill:

1. Add the source to this registry if it is verified.
2. If the source is only a candidate, add it to `docs/chinese-core-literature-inventory.md` instead.
3. Do not mix candidate bibliographic records into formal citation lists.

## V1.1 Source-Use Notes

- The V1.1 multi-case examples use verified international frameworks for rule design, not as substitutes for Chinese policy or CSSCI literature.
- Chinese policy and Chinese journal records remain important for future localization, but they should be added only after URL, PDF or bibliographic metadata are verified.
- Current V1.1 rules derived from these sources focus on: human oversight, risk governance, teacher digital competence, data minimization, explainability, fairness, accountability and evidence boundaries.

## V1.2 Source-Use Notes

- EEF professional development guidance supports the teacher digital competence case by emphasizing that teacher learning should connect mechanisms, practice, feedback and implementation rather than simple training attendance.
- WWC evidence standards support the mixed-methods and pre-submission rules that causal claims require stronger designs than satisfaction surveys or one-shot posttests.
- These sources are used to strengthen evidence-boundary rules, not to replace field-specific Chinese literature that still requires verification.

## V1.4 Source-Use Notes

- Chinese official sources 17-20 were verified through direct URL access, page title/H1 checks and keyword checks.
- These sources may support policy framing, standard alignment and platform-context rules.
- They are not substitutes for Chinese CSSCI/core-journal academic literature; journal articles still require CNKI, journal-site, DOI or local-PDF verification.
