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

检索使用公开题名和技术关键词。广义搜索命中大量产品、论坛、test-time scaling 和测试 LLM 的噪声；最终文献表只使用可核查的一手材料。本轮 MDPI 及不透明来源未纳入；这是本轮来源筛选限制，正式 SLR 应披露筛选规则，不能宣称对全部来源无偏覆盖。

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

本轮候选补查：Architectural perspectives on GenAI-driven software testing systems: A systematic literature review（ScienceDirect S0950584926002351）。搜索发现出版商结果，但直接打开失败，未纳入已核验文献表；后续取得正文/可访问一手版本再补入。

## 增量判断的边界

“信息依据—生成职责—质量证据”是本报告建议的整合方式，尚未证明是此前无人使用的分类。已有综述已涉及相近维度，正式新颖性判断应比较字段定义、跨场景覆盖、训练/推理权限拆分、证据分析深度和更新文献。

本轮没有根据单篇最高分值宣称任何方法普遍最好。方法原作者报告、外部复制结果和本报告的分析建议分别使用。
