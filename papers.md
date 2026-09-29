# LLM 测试用例生成综述：初步文献库

检索日期：2026-09-28。用途：确定综述范围、分类体系及精读顺序。本文献库是一轮广泛调研形成的种子集合，不是完成系统检索后的全量纳入集合。

核验层级：所有条目均有本轮访问的一手论文页、正式论文正文或作者项目页；多数方法目前核验到摘要及元数据。标记“正文”的条目额外检查了与分类相关的正文内容，但不代表全文审计或效果复现。年份用首次公开年份及当前版本/正式发表年份并列；未核实正式场所时直接标注 arXiv，不能据此断言尚未录用。综述、历史前驱、邻近应用与核心方法分开使用。数值结果不做跨论文排名。

## 已有综述：用于定位与滚雪球检索

| ID | 论文及来源 | 年份/状态 | 类型 | 整合用途与边界 | 核验 |
|---|---|---|---|---|---|
| S01 | [Software Testing with Large Language Models: Survey, Landscape, and Vision](https://arxiv.org/abs/2307.07221) | 2023/2024；TSE | survey | 广义测试任务与 LLM 技术；102 项研究包含程序修复，不能当成测试生成文献总数 | 摘要、元数据 |
| S02 | [Large Language Models for Unit Testing: A Systematic Literature Review](https://arxiv.org/abs/2506.15227) | 2025；arXiv | survey | 单元测试任务、模型适配与混合方法；范围截至 2025-03；包含 oracle | 正文分类框架 |
| S03 | [Large Language Models for Unit Test Generation: Achievements, Challenges, and Opportunities](https://arxiv.org/abs/2511.21382) | 2025；arXiv v2 | survey | 115 项研究；生成与质量保证两阶段；已有生命周期、oracle、维护、指标错位讨论 | 正文目录、RQ、分类框架 |
| S04 | [Large Language Models for Software Testing: A Research Roadmap](https://arxiv.org/abs/2509.25043) | 2025；arXiv | survey | 广义测试研究路线图；用于确认已有方向与分类覆盖 | 摘要、元数据 |
| S05 | [Requirements-Based Test Generation: A Comprehensive Survey](https://arxiv.org/abs/2505.02015) | 2025/2026；v3 标注 TOSEM 接收 | survey | 需求表示、方法、工具、评价和工业应用；包含传统及形式规格方法 | 摘要、元数据 |
| S06 | [AI-Driven Test Case Generation from Natural Language Requirements: A Survey of Techniques and Research Gaps](https://arxiv.org/abs/2606.06563) | 2026；arXiv | survey | 2000–2025 范围内筛选 21 项研究；并非仅现代 LLM | 摘要、元数据 |
| S07 | [Test case generation using large language models: a systematic literature review](https://link.springer.com/article/10.1007/s10586-026-06021-z) | 2026；Cluster Computing | survey | 38 篇 2020–2025 同行评审论文；预后处理、数据、指标、语言与工作流整合；与宽题名直接重叠 | 正文摘要、RQ、检索方法 |

## 单元测试与代码上下文

| ID | 论文及来源 | 年份/状态 | 类型 | 输入与生成机制 | 综述应分析什么 | 核验 |
|---|---|---|---|---|---|---|
| U01 | [An Empirical Evaluation of Using Large Language Models for Automated Unit Test Generation — TestPilot](https://arxiv.org/abs/2302.06527) | 2023/2024；arXiv/正式关联版本 | system/tool | 函数签名、函数体及文档示例；生成 JavaScript 测试，失败后重新提示 | 代码条件、文档补充与执行修复的早期代表 | 摘要 |
| U02 | [ChatUniTest: A Framework for LLM-Based Test Generation](https://arxiv.org/abs/2305.04764) | 2023/2024；FSE 2024 Demo 版本 | system/tool | focal context；生成—校验—修复 | 完整工程流水线；Demo 与长版本效果证据区分 | 摘要、版本说明 |
| U03 | [Code-Aware Prompting: A study of Coverage Guided Test Generation in Regression Setting using LLM — SymPrompt](https://arxiv.org/abs/2402.00097) | 2024；arXiv | pure method | 按执行路径分解提示，补充类型与依赖上下文 | 路径条件用于提示；不能直接称为 SMT 求解或形式保证 | 摘要 |
| U04 | [CODAMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models](https://www.microsoft.com/en-us/research/publication/codamosa-escaping-coverage-plateaus-in-test-generation-with-pre-trained-large-language-models/) | 2023；ICSE | pure method | 搜索停滞时请求 LLM 生成例子，继续搜索 | LLM 为传统搜索提供种子；职责分工和调用条件 | 作者机构项目页 |
| U05 | [CoverUp: Effective High Coverage Test Generation for Python](https://arxiv.org/abs/2403.16218) | 2024/2025；FSE 2025 | system/tool | 代码、覆盖信息及执行错误；迭代生成回归测试 | 覆盖反馈和上下文获取；回归目标与规格符合性区分 | 摘要、元数据 |
| U06 | [Effective Test Generation Using Pre-trained Large Language Models and Mutation Testing — MuTAP](https://arxiv.org/abs/2308.16557) | 2023；arXiv | pure method | 程序和存活变异体增强提示 | 训练/生成期间可见变异体与独立评价变异体的区分 | 摘要 |
| U07 | [Automated Unit Test Improvement using Large Language Models at Meta — TestGen-LLM](https://arxiv.org/abs/2402.09171) | 2024；FSE | system/tool | 扩充已有人工测试；构建、执行、稳定性和覆盖筛选 | 工业采纳；只保留运行通过测试的目标和 oracle 限制 | 正文过滤与回归定位 |
| U08 | [CITYWALK: Enhancing LLM-Based C++ Unit Test Generation via Project-Dependency Awareness and Language-Specific Knowledge](https://arxiv.org/abs/2501.16155) | 2025；arXiv v2 | pure method | 项目依赖分析和 C++ 语言知识 | 复杂语言、项目依赖和可执行落地 | 摘要 |
| U09 | [Multi-Agent LLM Collaboration for Unit Test Generation via Human-Testing-Inspired Workflows — TestAgent](https://arxiv.org/abs/2607.09101) | 2026；arXiv | pure method | 规划、生成、评审 agent；静态分析知识图谱和动态工具调用 | 仓库上下文与推理期自主决策；planner 生成的 test requirements 不等于外部需求 | 摘要 |
| U10 | [Test vs Mutant: Adversarial LLM Agents for Robust Unit Test Generation — AdverTest](https://arxiv.org/abs/2602.08146) | 2026；arXiv v3 | pure method | 测试 agent 与变异 agent 迭代对抗 | 推理期测试演化；不能仅凭“对抗”归类为参数训练 RL | 摘要、版本说明 |
| U11 | [Unit Test Case Generation with Transformers and Focal Context — AthenaTest](https://arxiv.org/abs/2009.05617) | 2020/2021；历史前驱 | method + benchmark | Java 预训练、代码—测试监督训练；Methods2Test | 神经测试生成历史、训练数据与上下文；与现代通用生成式 LLM 分层 | 摘要 |

## 需求、测试设计与验收测试

| ID | 论文及来源 | 年份/状态 | 类型 | 输入→输出 | 整合用途与边界 | 核验 |
|---|---|---|---|---|---|---|
| R01 | [Generating Test Scenarios from NL Requirements using Retrieval-Augmented LLMs: An Industrial Study — RAGTAG](https://arxiv.org/abs/2404.12772) | 2024；RE 关联 DOI | pure method | 需求及领域文档→自然语言测试场景 | 领域检索与专家评估；抽象场景不是完整执行脚本 | 摘要、元数据 |
| R02 | [Multi-Step Generation of Test Specifications using Large Language Models for System-Level Requirements](https://aclanthology.org/2025.acl-industry.11/) | 2025；ACL Industry | system/tool | 系统需求→中间测试制品→测试规格 | 工业需求分解与人工协作；文本相似度与缺陷检出分开 | 摘要、正式元数据 |
| R03 | [Acceptance Test Generation with Large Language Models: An Industrial Case Study](https://arxiv.org/abs/2504.07244) | 2025；arXiv/工业案例 | system/tool | user story→Gherkin→Cypress | 设计阶段和脚本落地阶段的上下文权限分别编码 | 摘要；阶段区分使用既有精读记录 |
| R04 | [APITestGenie: Generating Web API Tests from Requirements and API Specifications with LLMs](https://arxiv.org/abs/2604.02039) | 2026；arXiv | system/tool | 业务需求及 OpenAPI→API 集成脚本 | 需求、接口规格、跨端点场景；与 2024 前身去重，失败定义需精读 | 摘要 |

## Oracle、后置条件及蜕变关系

| ID | 论文及来源 | 年份/状态 | 类型 | 核心产物/机制 | 综述应分析什么 | 核验 |
|---|---|---|---|---|---|---|
| O01 | [Can Large Language Models Transform Natural Language Intent into Formal Method Postconditions? — nl2postcond](https://arxiv.org/abs/2310.01831) | 2023/2024；FSE 关联版本 | pure method | 自然语言意图→后置条件；有/无参考代码变体 | 性质式 oracle、权限差异、有限测试验证与形式证明边界 | 摘要；变体区分使用既有精读记录 |
| O02 | [Towards Generating Executable Metamorphic Relations Using Large Language Models](https://arxiv.org/abs/2401.17019) | 2024；arXiv/关联正式版本 | pure method | 输入变换与输出关系→可执行蜕变关系 | 无精确输出时的 oracle；关系前提和适用域必须验证 | 摘要 |
| O03 | [Nexus: Execution-Grounded Multi-Agent Test Oracle Synthesis](https://arxiv.org/abs/2510.26423) | 2025；arXiv | pure method | 需求讨论、候选实现执行、oracle 修订 | 候选实现一致性与独立语义证据区分；摘要与表格数字需逐表核对 | 正文方法、评估与表格 |
| O04 | [TOGA: A Neural Method for Test Oracle Generation](https://arxiv.org/abs/2109.09262) | 2021/2022；ICSE 2022 | pure method | 神经生成异常和断言 oracle | 历史 oracle 方法与输入生成器组合 | 摘要、元数据 |
| O05 | [Neural-Based Test Oracle Generation: A Large-scale Evaluation and Lessons Learned](https://arxiv.org/abs/2307.16023) | 2023；关联正式 DOI | other（复制/评价） | 外部、扩展及概念复制 TOGA | 原方法效果与外部复制对照；误报、拒答、缺陷检出分别报告 | 摘要 |
| O06 | [Hallucination to Consensus: Multi-Agent LLMs for End-to-End JUnit Test Generation — CANDOR](https://arxiv.org/abs/2506.02943) | 2025/2026；arXiv v7 | pure method | 多 agent 完整测试生成、panel oracle 共识 | 覆盖、输入生成和 oracle 评审交叉归类；共识可靠性需独立证据 | 摘要、当前版本 |

## API、服务集成与 GUI 动作序列

| ID | 论文及来源 | 年份/状态 | 类型 | 生成机制 | 整合用途与边界 | 核验 |
|---|---|---|---|---|---|---|
| A01 | [AutoRestTest: A Tool for Automated REST API Testing Using LLMs and MARL](https://arxiv.org/abs/2501.08600) | 2025；arXiv/工具论文 | system/tool | 语义操作依赖图、MARL、LLM 参数/值生成 | 多端点状态与依赖；MARL agent 与 LLM agent 概念分开 | 摘要 |
| A02 | [SAINT: Service-level Integration Test Generation with Program Analysis and LLM-based Agents](https://arxiv.org/abs/2511.13305) | 2025；arXiv | pure method | 源码静态分析、端点模型、操作依赖图和 agent | 白盒服务场景生成；代码抽取 use case 不是独立需求 | 摘要 |
| A03 | [Autonomous Large Language Model Agents Enabling Intent-Driven Mobile GUI Testing — DroidAgent](https://arxiv.org/abs/2311.08649) | 2023；arXiv | system/tool | 设置任务、GUI 交互、短长期记忆 | 高层意图与状态探索；任务相关性不等于业务 oracle 正确率 | 摘要 |
| A04 | [Make LLM a Testing Expert: Bringing Human-like Interaction to Mobile GUI Testing via Functionality-aware Decisions — GPTDroid](https://arxiv.org/abs/2310.15780) | 2023；arXiv/扩展版本 | system/tool | GUI 状态→动作→反馈循环与功能记忆 | 功能探索及动作生成；与早期 2305.09434 按研究家族去重 | 摘要 |

## 模糊测试：输入、驱动、生成器和变异器

| ID | 论文及来源 | 年份/状态 | 类型 | LLM 的生成职责 | 整合用途与边界 | 核验 |
|---|---|---|---|---|---|---|
| F01 | [Large Language Models are Zero-Shot Fuzzers: Fuzzing Deep-Learning Libraries via Large Language Models — TitanFuzz](https://arxiv.org/abs/2212.14834) | 2022/2023；arXiv | pure method | 生成及补全变异 DL 库输入程序 | API 合法性约束；输入程序和完整测试分开 | 摘要 |
| F02 | [Large Language Models are Edge-Case Fuzzers: Testing Deep Learning Libraries via FuzzGPT](https://arxiv.org/abs/2304.02014) | 2023；arXiv | pure method | 历史触发 bug 的程序引导不寻常输入生成 | 历史知识与边界输入；历史模式外的缺陷检测 | 摘要 |
| F03 | [Fuzz4All: Universal Fuzzing with Large Language Models](https://arxiv.org/abs/2308.04748) | 2023/2024；arXiv | system/tool | autoprompting、输入生成/变异及迭代更新 | 多语言通用输入引擎；oracle 通常来自外部检测 | 摘要 |
| F04 | [Large Language Model guided Protocol Fuzzing — ChatAFL](https://www.ndss-symposium.org/wp-content/uploads/2024-556-paper.pdf) | 2024；NDSS | system/tool | 协议文法、种子、多消息序列 | 格式合法性与协议状态覆盖；不是精确输出预测 | 正式正文摘要、作者仓库 |
| F05 | [Prompt Fuzzing for Fuzz Driver Generation — PromptFuzz](https://arxiv.org/abs/2312.17677) | 2023/2024；CCS 2024 | pure method | coverage-guided prompt mutation→fuzz driver | 驱动程序是高层测试产物，后续输入由 fuzzer 产生 | 作者正式正文摘要 |
| F06 | [ELFuzz: Efficient Input Generation via LLM-driven Synthesis Over Fuzzer Space](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-chuyang) | 2025；USENIX Security | pure method | 覆盖引导、在 fuzzer 空间演化生成器 | 从生成单个输入到生成可复用输入生成器 | 官方摘要 |
| F07 | [Bulbasaur: Branch-Guided Online Mutator Generation for Greybox Fuzzing](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-yiyi) | 2026；USENIX Security | pure method | 分支选择、静态/动态上下文→在线定制变异器 | 2026 新进展；复用生成的变异器降低逐输入调用需求 | 官方摘要、正式元数据 |

## 模型训练、测试辅助代码生成及交互

| ID | 论文及来源 | 年份/状态 | 类型 | 机制/产物 | 整合用途与边界 | 核验 |
|---|---|---|---|---|---|---|
| T01 | [PyTester: Deep Reinforcement Learning for Text-to-Testcase Generation](https://arxiv.org/abs/2401.07576) | 2024/2025；JSS | pure method | SFT+PPO；语法、参考执行和覆盖奖励；描述→assert | 推理不读实现与训练使用参考代码同时标注；参考通过是对齐代理 | 正文奖励和评价定义 |
| T02 | [Learning to Generate Unit Test via Adversarial Reinforcement Learning — UTRL](https://proceedings.iclr.cc/paper_files/paper/2026/hash/efb02f96766a3b599c76852abf4d42dd-Abstract-Conference.html) | 2025/2026；ICLR 2026 | pure method | Tester/Coder 交替 RL；区分参考解与采样程序 | instruction–code 训练数据；fidelity、选择收益与规格符合性区分 | 官方摘要；arXiv 正文训练 |
| T03 | [ATGen: Adversarial Reinforcement Learning for Test Case Generation](https://proceedings.iclr.cc/paper_files/paper/2026/hash/eed25c037bc08afcbefab6f7a6b700e0-Abstract-Conference.html) | 2026；ICLR | pure method | 对抗代码生成器、动态课程、输出准确和攻击成功奖励 | 生成目标、oracle 验证来源及课程演化；详细奖励待精读 | 官方摘要 |
| T04 | [Learning to Solve and Verify: A Self-Play Framework for Code and Test Generation — Sol-Ver](https://arxiv.org/abs/2502.14948) | 2025/2026；arXiv v4 | pure method | 同一模型 solver/verifier 自博弈与数据筛选 | 自生成数据质量与错误积累；不把执行共识直接视作真值 | 摘要、当前版本 |
| T05 | [Learning to Generate Unit Tests for Automated Debugging — UTGen](https://arxiv.org/abs/2502.01619) | 2025；arXiv/正式关联版本 | pure method | 为调试训练揭错测试生成器 | 主设置读取 buggy code；不是严格需求-only 方法 | 摘要；输入权限使用既有正文核对 |
| T06 | [Dynamic Scaling of Unit Tests for Code Reward Modeling — CodeRM](https://aclanthology.org/2025.acl-long.343/) | 2025；ACL | pure method | 测试生成训练与动态预算，服务代码评分 | 标准提示含 code solution；代码排序收益与测试自身质量分别编码 | 正式摘要；提示权限使用既有正文核对 |
| T07 | [Two-Stage Reinforcement Learning for Sound and Adversarial Test Generation in Code LLMs — TCS](https://arxiv.org/abs/2609.03955) | 2026；作者页标注 Findings EMNLP 2026 接收 | pure method | 先参考解一致，再针对当前失败模式训练反例 | 2026-09 新进展；soundness 的操作性定义需核对 | 摘要、接收自述 |
| T08 | [SAGE: Specification-Aware Grammar Extraction for Automated Test Case Generation with LLMs](https://arxiv.org/abs/2506.11081) | 2025；arXiv | pure method | 需求→CCFG；SFT+GRPO、文法反馈 | 学习输入文法与输入生成；不能视为完整输出 oracle 生成 | 摘要 |
| T09 | [LogiCase: Effective Test Case Generation from Logical Description in Competitive Programming](https://www.ijcai.org/proceedings/2025/861) | 2025；IJCAI | method + benchmark | 输入描述→带计数器文法→输入 | 文法与约束提取；oracle 来源单列 | 官方页；机制细节使用既有精读记录 |
| T10 | [CodeT: Code Generation with Generated Tests](https://arxiv.org/abs/2207.10397) | 2022/2023；arXiv/正式关联版本 | pure method | 生成测试与候选代码，执行一致性排序 | 邻近用途：测试作为代码选择证据；下游 pass@1 不是 oracle 正确率 | 摘要 |
| T11 | [LLM-Based Test-Driven Interactive Code Generation: User Study and Empirical Evaluation — TiCoder](https://arxiv.org/abs/2404.10100) | 2024；arXiv/正式关联版本 | system/tool | 用户确认测试，澄清意图，筛选代码 | 人类提供 oracle 证据；与无人参与自动生成分层 | 摘要 |
| T12 | [Reinforcement Learning from Automatic Feedback for High-Quality Unit Test Generation — RLSQM](https://arxiv.org/abs/2310.02368) | 2023/2025；DeepTest 2025 | pure method | 静态质量/测试异味 reward model+PPO | 学习可维护性而非直接学习语义正确性；与误提交的 2412.14308 去重 | 摘要、版本说明 |

## 基准与实证评价

| ID | 论文及来源 | 年份/状态 | 类型 | 测量对象 | 主要边界 | 核验 |
|---|---|---|---|---|---|---|
| B01 | [TestGenEval: A Real World Unit Test Generation and Test Completion Benchmark](https://arxiv.org/abs/2410.00752) | 2024；arXiv | pure benchmark | 11 个 Python 仓库；测试生成、补全与覆盖改善 | 真实仓库上下文；覆盖不能独立证明 oracle 语义 | 摘要 |
| B02 | [TESTEVAL: Benchmarking Large Language Models for Test Case Generation](https://aclanthology.org/2025.findings-naacl.197.pdf) | 2024/2025；Findings NAACL | pure benchmark | 210 个 Python 程序；总体、目标行/分支及路径覆盖 | 重点是执行路径推理；不是完备需求测试基准 | 正式正文摘要 |
| B03 | [SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents](https://arxiv.org/abs/2406.12952) | 2024/2025；arXiv v3 | pure benchmark | issue→复现测试；修复前失败、修复后通过 | fail-to-pass 支持 issue 区分，完整语义正确性仍需额外证据 | 摘要；评估正文 |
| B04 | [Benchmarking LLMs for Unit Test Generation from Real-World Functions — ULT/PLT](https://arxiv.org/abs/2508.00408) | 2025；arXiv，页面标注 Under Review | pure benchmark | 复杂真实函数、已泄漏/未泄漏测试对照 | 降低特定污染风险；不能断言消除所有训练污染 | 摘要、元数据 |
| B05 | [RESTestBench: A Benchmark for Evaluating the Effectiveness of LLM-Generated REST API Test Cases from NL Requirements](https://arxiv.org/abs/2604.25862) | 2026；EASE 接收自述 | pure benchmark | 精确/模糊需求、需求相关变异、SUT 反馈修订 | 3 个 REST 服务；需求变异覆盖仍受错误模型限制 | 正文摘要、反馈结果 |
| E01 | [LLM vs. Human Unit Tests: Fault Detection on Real Python Bugs](https://arxiv.org/abs/2606.08588) | 2026；arXiv | other（实证） | 人工与 LLM 测试在历史 bug 和配对基准上的对照 | 用于真实缺陷评价分支；数值结论待全文审计 | 摘要 |
| E02 | [Evaluating LLM-Based Test Generation Under Software Evolution](https://arxiv.org/abs/2603.23443) | 2026；arXiv | other（实证） | 语义保持与语义改变条件下的测试生成 | 区分变更要求、oracle 适应和回归；不能将旧行为保留一律判错 | 摘要 |
| E03 | [On the Flakiness of LLM-Generated Tests for Industrial and Open-Source Database Management Systems](https://arxiv.org/abs/2601.08998) | 2026；ICSE SEIP | other（实证） | 数据库测试扩充后的不稳定性与模式传递 | 现有测试上下文可传播 flakiness；领域结果不直接外推全部项目 | 摘要、官方会议页 |
| G01 | [Large Language Models are Few-shot Testers: Exploring LLM-based General Bug Reproduction — LIBRO](https://arxiv.org/abs/2209.11515) | 2022/2023；arXiv/正式关联版本 | system/tool | 自然语言 bug report→复现测试→后处理排序 | 已知 bug 复现与未知缺陷发现分开；后续 2311.04532 作为研究家族扩展 | 摘要 |

## 下一轮全文编码字段

每篇建立一条 study 记录、多个 variant 记录：正式 DOI/arXiv 版本、家族 ID、类型、任务目标、测试层级、被测系统、语言、生成产物、推理可见源码/需求/测试/日志、训练监督、奖励来源、输入合法性来源、oracle 来源、反馈提供者、是否更改模型参数、停止条件、预算、基准拆分、语义正确性定义、合法实现误拒、真实缺陷检出、mutation 的生成与评价隔离、覆盖、flakiness、人工负担、成本、复现资源、检查到的具体章节。

本轮没有提取所有论文的作者、DOI、逐项模型配置与数值表格；这些字段在正式 SLR 的全文编码阶段补齐。尚未核对的细节用 unknown，而不是推断为没有使用。
