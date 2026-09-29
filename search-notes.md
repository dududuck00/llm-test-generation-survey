# 检索与核验记录

日期：2026-09-28；类型：综述选题的一轮广泛调研。来源：网络检索、直接访问公开论文页、正文 HTML 和正式论文 PDF；复用了既有需求测试生成调研作为检索种子。

## 已执行的检索簇

- 已有综述：LLM test generation survey/systematic review；software testing survey；unit testing lifecycle；requirements-based test generation survey；2025–2026 更新。
- 单元测试：TestPilot、ChatUniTest、CodaMOSA、SymPrompt、CoverUp、MuTAP、TestGen-LLM、CITYWALK、TestAgent、AdverTest。
- 需求/验收：RAGTAG、multi-step test specifications、acceptance test generation、APITestGenie。
- Oracle：nl2postcond、metamorphic relations、TOGA/复制、CANDOR/Nexus。
- API/GUI：AutoRestTest、SAINT、GPTDroid、DroidAgent。
- Fuzzing：TitanFuzz、FuzzGPT、Fuzz4All、ChatAFL、PromptFuzz、ELFuzz、Bulbasaur。
- 训练与代码生成应用：PyTester、UTRL、ATGen、Sol-Ver、UTGen、CodeRM、TCS、SAGE、LogiCase、CodeT、TiCoder、RLSQM。
- 基准与实证：TestGenEval、TestEval、SWT-Bench、ULT/PLT、RESTestBench、真实 Python bug、软件演化、数据库 flakiness、LIBRO。

检索使用公开题名和技术关键词。广义搜索命中大量产品、论坛、test-time scaling 和测试 LLM 的噪声；最终文献表只使用可核查的一手材料。根据所用检索技能的来源政策，MDPI 及不透明来源未纳入；这是本轮来源筛选限制，正式 SLR 应披露筛选规则，不能宣称对全部来源无偏覆盖。

## 额外检查的正文

- S02/S03：分类、目录、RQ；确认已有生命周期、oracle、混合、维护及评价效度讨论。
- S07：摘要、8 个 RQ、检索方法；确认与宽题名直接相关，不使用其自述“first”作为优先权证据。
- O03 Nexus：方法、引用与评价表格；候选实现执行是验证步骤，不能据此推出独立语义保证；摘要与表格有不一致迹象，因此本轮不引用其具体提升数字。
- T01 PyTester：奖励与 aligned/passing 定义；训练使用 ground-truth code，推理仅描述与签名的设置须分别编码。
- T02 UTRL：训练输入 instruction–code pairs、参考程序与采样代码区分；测试 fidelity 的对象不等于完备需求符合性。
- U07 TestGen-LLM：过滤/回归定位；通过和覆盖筛选的证据对象是回归增强。
- B03 SWT-Bench：fail-to-pass 复现定义与 patch 验证。
- B05 RESTestBench：精确/模糊需求、正确/变异 SUT 反馈条件。
- F04/F05/B02：正式论文摘要和场所信息。

其余多数条目核验到摘要与元数据，papers.md 逐项标明。R03/O01/T05/T06/T09 的若干输入权限细节沿用先前全文核对，本轮重新访问论文页但未完整复查对应附录；正式编码前须复核当前版本。

## 当前状态与覆盖缺口

文献库是种子集合，不能作为 PRISMA/SLR 最终纳入数；没有运行覆盖全部数据库的穷尽检索，没有独立双人筛选/编码，没有提取全量效应值，也没有复现方法。正式投稿场所核验并未对每篇完成，未核实者保留 arXiv 标签。

已覆盖主要功能测试路线及 fuzzing/security 输入生成。仍需专门补查性能/负载测试、可访问性、并发/分布式、复杂 Web E2E、模型/契约驱动验证、测试维护与数据质量研究，以及非英文/工业灰色文献是否纳入。早期神经断言/测试生成只选历史锚点，未全量回溯。

初轮候选补查：Architectural perspectives on GenAI-driven software testing systems: A systematic literature review（ScienceDirect S0950584926002351）。2026-09-29 再检索发现 DOI 10.1016/j.infsof.2026.108246，直接访问仍为 403，保留待核验状态。

## 增量判断的边界

“信息依据—生成职责—质量证据”是本报告建议的整合方式，尚未证明是此前无人使用的分类。已有综述已涉及相近维度，正式新颖性判断应比较字段定义、跨场景覆盖、训练/推理权限拆分、证据分析深度和更新文献。

本轮没有根据单篇最高分值宣称任何方法普遍最好。方法原作者报告、外部复制结果和本报告的分析建议分别使用。

## 2026-09-29 补充检索

目的：沿当前大纲补齐方法、oracle、训练监督和评价证据。结果：新增 35 条，经 ID、规范题名及 arXiv/DOI 家族去重，登记总数 95。详见 [补充检索报告](supplemental-review.md) 与 [新增记录及章节映射](supplemental-search.json)。此计数不包括筛选候选和撤回论文，不代表完整数据库筛选的 PRISMA 纳入数。

### 执行方式与可复查查询

执行的是公开网络检索、已有综述伴随清单的定向追踪及一手链接核验。没有登录 IEEE/ACM/Scopus/Web of Science 执行数据库导出。查询没有起始年份硬限制；重点核对 2023–2026，检索日期为 2026-09-29。查询日期不能解释为所有数据库检索的统一截止日期。

代表性原始查询如下（部分检索附加 `-site:mdpi.com` 和 `-site:reddit.com` 降低排除来源及论坛噪声）：

- `LLM unit test generation 2025 2026 ASTER TELPA HITS TestSpark`
- `large language model test oracle assertion generation 2025 2026`
- `LLM test generation benchmark 2025 2026 TC-Bench`
- `LLM requirements test generation 2025 2026 business requirements real bugs TC-Bench`
- `LLM test generation REST API GUI metamorphic 2025 2026`
- `LLM fuzzing 2025 2026 USENIX Fuzz driver generation`
- `"TC-Bench" "test" arxiv`；`"TC-Bench" arxiv test case generation`
- `"TELPA" test generation arxiv`；`"ARMeta" "REST" testing`
- `"LLM" "GUI testing" "2025" "test generation"`
- `"TOGBench" test oracle generation`；`"TOGBench" "3805760.3814927"`
- `"CAT-LM" arxiv`；`"UniTSyn" arxiv`；`"exLong" "arxiv"`
- `"LlamaRestTest" arxiv`；`"LLM test generation" "test maintenance"`
- `"Architectural perspectives on GenAI-driven software testing systems"` 及追加 `arxiv`
- `"Large language models-driven fuzzing: A systematic survey" arxiv`

引用追踪种子：[S02 作者文献清单](https://github.com/iSEngLab/AwesomeLLM4UT)。该清单作为发现入口，不能代替一手核验，所列 228 个 unique studies 包含修复、迁移、重构等范围更宽的任务，未直接全部导入。S03 本轮核对的是 [arXiv v3](https://arxiv.org/abs/2511.21382v3) 的摘要与版本信息；178 项更新为其当前摘要自述，未重审 v3 全文。

### 纳入与筛选规则

- 纳入：LLM 生成/补全/增强软件测试、oracle、驱动或输入生成器的方法；直接评价这些产物的实证；相应训练数据、评价基准和工业案例。需要可访问一手论文页、正文或作者项目证据，逐条标记检查层级。
- 合并：同一 arXiv 家族的题名更新及预印本/正式关联版本。本轮 TELPA、ScenGen、VALTEST 均采用当前题名，不额外计旧题名。
- 排除或待核验：撤回的 VisiDroid；硬件 AssertionBench（范围不符）；直接访问 403 的两篇综述；仅二手摘要的候选；技能政策排除的 MDPI 来源。
- 不依据摘要缺少某字段推断方法没有该输入/训练/反馈。未核实正式场所者明确标注未核实；arXiv comments 的接收自述与官方 proceedings 核验分开。
- 新记录中 TOGBench 的主证据为作者 README 和 ACM 摘要/元数据，OpenReview 正文访问触发验证页；正文未精读。ScenGen 使用 v4 摘要；ASTER 额外检查的正文是 v2，不冒称 v3 方法全文已核验。

### 可核查产物与后续缺口

本轮保存了全部 35 条的标题、作者、稳定链接、首次年份、检查版本/状态、类型、机制、分析边界、核验层级和章节映射。关键补充证据包括 CURE 的参考测试监督、ConVerTest 的候选实现共识、需求 oracle 的 diff 派生构造、回归 oracle 修复假设、指标相关性的任务条件以及 TOGBench 指标命名差异。

尚未完成全部数据库检索、完整递归引用追踪、独立双人筛选、所有核心论文的全文 variant 编码、效果复现或定量合成。性能/负载、并发/分布式、Web E2E、测试维护与数据质量仍是后续定向检索项。本轮未将论文全文 PDF 上传至公开仓库。
