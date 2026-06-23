# Chinese Core Literature Verified Registry

> 目的：本文件用于登记已经完成题录核验的中文核心/CSSCI/教育技术权威期刊文献。  
> 当前状态：V1.1 阶段先建立核验规范和登记模板，不把未核验候选文献写成正式引用。  
> 来源候选：`docs/chinese-core-literature-inventory.md`。

## Verification Rule

只有同时满足以下条件的文献才能进入本文件：

1. 题名、作者、期刊/来源、年份、卷期、页码等元数据已核验。
2. 至少有一种可追溯来源：CNKI 详情页、期刊官网、DOI 页面、本地 PDF 或学校数据库导出的题录。
3. 文献主题与教育信息化治理、教育数字化、教育数据治理、智能教育、教师数字素养、AI 教育治理、教育技术研究方法等方向直接相关。
4. 不得把搜索结果摘要、AI 生成题录或未经核验的候选条目作为正式文献。

## Metadata Fields

| Field | Requirement |
|---|---|
| ID | 连续编号 |
| Authors | 与原文一致 |
| Year | 与原文一致 |
| Title | 与原文一致 |
| Source | 期刊、会议、学位论文或官方出版物名称 |
| Volume/Issue/Pages | 尽可能完整 |
| DOI/CNKI URL | 如有则记录 |
| Verification source | CNKI、期刊官网、本地 PDF、DOI、学校数据库等 |
| Skill mapping | 该文献支撑哪些技能或 reference |
| Notes | 使用边界或待补信息 |

## Verified Entries

| ID | Authors | Year | Title | Source | Volume/Issue/Pages | DOI/CNKI URL | Verification source | Skill mapping | Notes |
|---:|---|---:|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

## Migration Workflow

1. 从 `docs/chinese-core-literature-inventory.md` 选择一条候选文献。
2. 打开 CNKI、期刊官网、DOI 页面或本地 PDF 核验元数据。
3. 若元数据完整，复制到 `Verified Entries`。
4. 在 `docs/verified-source-registry.md` 中增加来源说明，或在 `docs/evidence-base.md` 中增加规则映射。
5. 若无法核验，保留在 inventory，不进入正式引用。

## Use Boundary

本文件一旦填写正式条目，可用于：

- 补强 `references/` 中的中文学术语境。
- 支撑论文引言、文献综述、理论框架和投稿前审查。
- 连接教育技术中文期刊写作范式。

本文件不可用于：

- 伪造不存在的文献。
- 用未核验候选替代正式引用。
- 为了凑数量而加入主题不相关文献。

