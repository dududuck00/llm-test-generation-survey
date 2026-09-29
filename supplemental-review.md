# 补充检索与论文整合建议

检索日期：2026-09-29。沿用既定的“信息来源—生成策略—质量证据”主线。本轮增加 35 条经一手材料筛选的记录，文献库由 60 条增至 95 条：7 条综述/路线图，88 条方法、工具、基准、实证及历史记录。95 是当前登记数，不是系统综述最终纳入数；相同研究的题名和版本合并计数。2026-09-29 已将新增研究整合进主稿正文、引用和 PDF；下文保留检索时的证据卡与整合依据，实际章节变更见 manuscript/revision-notes.md。

新增条目、作者、核验层级、版本状态及章节映射保存在 [supplemental-search.json](supplemental-search.json)，可用引用候选保存在 [supplemental-references.bib](supplemental-references.bib)。完整登记表见 [papers.md](papers.md)。本文的整合建议是分析判断；论文的具体输入权限和评价定义以所列原文片段为依据。

## 覆盖变化与章节映射

| 方向 | 新增数 | 代表记录 | 对当前文章的补强 |
|---|---:|---|---|
| 单元测试/项目上下文 | 7 | U12 ASTER、U13 HITS、U14 TELPA、U15 KTester、U16 exLong、U17 RAG 实证、U18 ChatTester | §5 从提示方法扩展到结构化上下文、异常路径、mocking 和测试设计知识；§6 补充专用微调 |
| 需求/验收/变更意图 | 2 | R05 Testora、R06 AToMIC | §4 区分外部需求、PR 变更意图与源码上下文；§8 纳入工业移动验收 |
| Oracle/测试验证 | 7 | O07 TOGLL、O08 Doc2OracLL、O09 Tratto、O10 ConVerTest、O11 VALTEST、O12 需求 oracle、O13 DCAware | §4 区分具体输出、公理性质和异常 oracle；§5 区分共识、执行与统计验证 |
| API/GUI | 3 | A05 LlamaRestTest、A06 ARMeta、A07 ScenGen | §4–5 比较参数规则、蜕变关系和场景动作；补充小模型学习 |
| Fuzzing | 3 | F08 G2FUZZ、F09 OSS-Fuzz-Gen、F10 Scheduzz | §5–7 增加二进制输入生成器、合法 API 用法、调度与假阳性 |
| 训练与数据增强 | 3 | T13 CAT-LM、T14 CURE、T15 FuzzAug | §6 纳入对齐预训练、协同 RL、动态分析数据增强及监督来源 |
| 基准/数据资源 | 4 | B06 TC-Bench、B07 MultiFileTest、B08 TOGBench、B09 UniTSyn | §7 按竞赛程序区分、多文件生成、真实 oracle 与训练语料区分任务 |
| 实证/复制/修复 | 6 | E04 错误代码影响、E05 指标相关性、E06 misguidance、E07 oracle 实证、E08 Test Wars、E09 YATE | §7 比较实现状态、代理指标、真实缺陷与修复干预；避免普遍优劣结论 |

## 优先精读的证据卡

### T14 CURE：没有参考代码不等于没有金标准监督

来源：[arXiv v2 正文 §3.3、图3、式3–4](https://arxiv.org/html/2506.03136v2)。摘要强调不使用 ground-truth code；§3.3 明确将任务与 ground-truth unit tests 配对，并用这些测试区分生成代码的正确/错误类别，构建 coder 与 tester 奖励。主设置应编码为“无参考代码监督、有参考测试监督”。下游代码选择收益与测试语义正确性分别编码。不同消融是否去掉参考测试，留待逐变体复核。

### O10 ConVerTest：无预先实现与候选代码执行的区别

来源：[正文 §II–III](https://arxiv.org/html/2602.10522v1)。方法生成代码候选和测试候选，以 SC、CoVe 和 dual execution agreement 筛选测试。可以归入无需预先参考实现的生成，但仍有候选程序执行证据。本文分析：互相一致可能保留共同误解，不能将候选共识称为独立语义真值。训练数据、预算及完整提示待编码。

### O12 需求 oracle：生成权限与数据构造权限分开

来源：[正文 §3、§4.1–4.4](https://arxiv.org/html/2607.10277v1)。模型接收需求与最小方法结构，不接收实现或修复差异；研究者由 buggy/fixed diff 构造需求和 REQ oracle。评价区分 REQ 一致和 SUT 一致。适合需求生成小规模实证，但仅涉及 10 个 Lang bug，且基准构造依赖修复信息。不能写成原始工业需求的无实现构造基准。

### E05 指标相关性：评价指标的用途受设置约束

来源：[v1 摘要与正文目录](https://arxiv.org/html/2607.22880v1)。研究分别讨论覆盖、mutation、真实 bug detection，并控制测试规模及输入代码状态。作者报告，回归式、代码可合理视为正确的设置下，代理指标可以提供比较信号；buggy-code 揭错设置下，其可靠性下降。本文应说明适用条件，不将“代理不等于语义真值”写成“代理完全无用”。相关系数、置信区间和混杂控制数值表待读。

### E06 misguidance：从实现抽取的规格仍有来源依赖

来源：[正文 §2.1–2.2](https://arxiv.org/html/2607.22883v1)。研究用 Defects4J 的 buggy/fixed 对分析误导测试，并以 LLM 生成 docstring 替换提示中的 buggy code。研究问题包括规格质量、是否继承 bug 和无 bug 代码设置。综述分类应保留“源码派生规格”字段，避免与外部独立需求混为一类。

### O13 DCAware：修复陷阱对应回归 oracle 补全

来源：[正文 §1 设置及动机](https://arxiv.org/html/2608.05917v1)。研究有可执行 test prefix，将当前程序版本视为预期行为，生成或加强缺失 oracle；不是从零生成完整测试。作者将多轮执行修复偏向易通过断言称为 Self-Repair Trap。结论限定所研究的回归补全设置，完整对照和消融仍需精读。

### E09 YATE：有益修复与 oracle 迁就应拆分

来源：[正文 §1](https://arxiv.org/html/2507.18316v1)。方法用静态规则与重新提示修复 near-miss 测试，正文也讨论通过当前程序输出修订失败断言。前者可以恢复测试的可执行性；后者依赖当前实现作为回归依据的假设。与 DCAware 应比较修复类型、目标和预算，不能仅凭“repair”将两篇结果写成矛盾。

### E07 Oracle 实证：正确性代理与缺陷代理都有边界

来源：[作者 PDF §I.A](https://homes.cs.washington.edu/~mernst/pubs/neurosymbolic-oracles-ase2025.pdf)。研究在模型时间截断后收集人工 Java oracle；原文明确将原开发者 oracle 比较视为正确性代理、mutation 视为错误检出代理。可以支撑时间切分与上下文消融的讨论，不能把“与人工一致”或“mutation 相近”写成完备规格符合性。

### B06 TC-Bench：有限错误池中的诊断能力

来源：[当前 v3 摘要](https://arxiv.org/abs/2510.08720)。WrongSelect 根据代码—测试矩阵选择竞赛错误代码，形成更紧凑的区分基准。适合分析候选池内错误多样性与测试判别；本报告判断其矩阵 rank 的覆盖解释限于观测池，不能外推到全部可能错误。本轮未复核所有定理和数据构造附录。

### B08 TOGBench：真实 oracle 多样性与指标定义

来源：[作者 README Overview、Features、Outputs](https://github.com/assert-lab/TOGBench)，[ACM 元数据和摘要](https://doi.org/10.1145/3805760.3814927)。涵盖六类 oracle 及单、多、混合、自定义实例，提供回填、编译、执行和变异评价。README 将 False Positive Rate 描述为错误程序仍通过；该名称与常见“合法实现被误拒”的使用不同，提取时必须记录原始定义。论文正文与实现尚未审计。

### U17 RAG 实证：覆盖、正确性与报告确认分开

来源：[v2 摘要](https://arxiv.org/abs/2409.12682)。比较 API 文档、issues、社区问答；作者报告 RAG 未改善其正确性度量，但改善覆盖。摘要分别列发现、上报、确认、拒绝及待确认 bug。可以作为检索收益的条件性证据，数值不与其他领域 RAG 方法直接排名。

### F09 OSS-Fuzz-Gen：crash 的真实性需要验证

来源：[Google Research 作者机构摘要](https://research.google/pubs/lessons-from-mitigating-false-positives-in-googles-oss-fuzz-gen/)。报告使用 API 约束和现实程序入口上下文验证生成驱动导致的 crash，筛除较多初步错误报告。补强“输入/驱动合法性→失败归因→确认缺陷”证据链；本轮未取得完整正式论文配置，不报告可复现效果。

## 综述框架需要加强的位置

1. **§4 信息权限表**：增加“规格来源”与“基准构造权限”。外部需求、实现派生 docstring、由修复差异编写的需求不是同一种证据。
2. **§5 生成机制**：上下文组织拆成切片、依赖/调用分析、领域知识和检索；修复拆成构建修复、输入修复、回归 assertion 修订及语义审查。
3. **§6 学习方法**：按参数更新方式和监督来源整合；CURE 与 UTRL/ATGen、PyTester、CAT-LM、FuzzAug 对照。逐变体记录参考代码、参考测试和候选程序的可见性。
4. **§7 评价**：增加“任务—指标—支持的结论—不支持的结论”表；区分回归增强、已有 bug 揭错、已知 issue 复现、候选代码排序和业务符合性。
5. **§8 实践**：用 ASTER、AToMIC、TestGen-LLM 和 OSS-Fuzz-Gen 讨论 mocking、人工负担、执行稳定性、成本与误报处理。

现有章节顺序仍适用。更有价值的变化是补充跨论文比较表和上述条件分析，不必为每个新工具新增小节。建议新增比较图等字段完成全文编码后再画，当前数据不足以制作可信的频率/趋势图。

## 版本纠正、筛选与待核验候选

| 条目 | 本轮决定与依据 |
|---|---|
| S03，arXiv:2511.21382 | 当前 v3 于 2026-09-27 修订，摘要报告 178 项、截止 2026-07-31；旧 v2 的 115 项不能描述当前版本。保留同一 ID，更新登记说明；旧精读内容不自动视为当前全文已核验。 |
| TELPA，arXiv:2404.04966 | 旧题名和当前 Advancing Code Coverage 合并为 U14。 |
| ScenGen，arXiv:2506.05079 | 旧 LLM-Guided Scenario-based GUI Testing 与当前题名合并为 A07；采用 v4 摘要。 |
| VALTEST，arXiv:2411.08254 | 登记当前题名 Toward Automated Validation…；简称不另计一篇。 |
| VisiDroid，arXiv:2504.15917 | [当前页标注 withdrawn](https://arxiv.org/abs/2504.15917)，作者说明方法及实验将改变；不纳入核心集合，等待替代版本。 |
| AssertionBench，Findings NAACL 2025 | [官方论文](https://aclanthology.org/2025.findings-naacl.449/)实际是硬件设计断言，不作为软件单元测试 oracle 核心基准；本轮不扩展硬件范围。 |
| Architectural perspectives… | DOI 10.1016/j.infsof.2026.108246；发现出版商摘要，直接访问 403；待获取可访问一手全文，未增加 S08。该综述对架构与评价分类的重叠值得后续检查。 |
| Large language models-driven fuzzing: A systematic survey | DOI 10.1016/j.engappai.2026.115126；直接访问 403，待可访问一手版本，未增加 S09。 |

## 本轮完成范围与仍需完成的检索

完成主题补查、已有综述伴随清单的定向追踪、35 条新记录一手核验、研究家族去重、部分正文片段核验及章节映射。未使用订阅数据库导出完整结果集，未完成所有前向/后向引用的递归筛选，没有独立双人筛选和全量 variant 编码，因此仍定位为结构化叙述性综述的增量检索。

下一步优先补查高质量的训练数据质量、性能/负载、并发/分布式、复杂 Web E2E 与测试维护文献。后四类先作为范围边界检查，再决定是否拓宽正文；不将测试 LLM 自身的 benchmark 自动纳入“LLM 生成软件测试”。对核心研究完成全文编码后，继续规范化正式引用和完善匿名材料。正文整合与 PDF 更新已完成，全量全文编码仍待完成。
