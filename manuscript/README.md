# LLM-Based Test Generation — FSE-format survey draft

英文综述，沿用 survey-plan.md 的十章组织及“信息来源—生成机制—质量证据”主线。2026-09-29 已将补充检索的 35 条记录整合进正文，当前共有 95 条正文引用、3 张概念图和 4 张比较表。

## 阅读与编辑

- main.pdf：22 页阅读版，正文与 Data Availability 截至第 18 页，参考文献位于第 19–22 页。
- main.tex：入口文件；十个章节保存在 sections/ 的九个文件中。
- references.bib：95 条文献，引用键与登记表 ID 对应。
- main.bbl：当前编译的参考文献，随源码包保留。
- [revision-notes.md](revision-notes.md)：补充文献的章节整合、关键证据边界与验证记录。
- outline-audit.md：原大纲对照及历史图表调整记录。
- acmart.cls、ACM-Reference-Format.bst、LICENSE：用户模板中的原始文件，未修改。

## 格式与内容状态

采用 acmsmall,screen,review,anonymous 单栏数字引用布局，依据 [FSE 2027 主研究轨道说明](https://conf.researchr.org/track/fse-2027/fse-2027-papers)，于 2026-09-29 再次核验：正文上限 18 页，参考文献 4 页，Data Availability 不计页限。会议字段使用已核实的 FSE 2027 日期与地点，不填写虚构 DOI、ISBN、作者或录用信息。

页眉页脚为原始 acmart 默认样式；未修改模板字体、字号、页边距和行距。默认卷、期、文章号及出版日期仍是模板占位字段，录用后应根据 ACM 元数据填写。

当前定位为 structured narrative survey。95 条来源包含 7 条综述/路线图和 88 条其他研究记录，登记数不是系统综述的最终纳入数。多数来源检查了摘要和元数据；选定研究检查了具体正文片段。没有虚构 PRISMA 数字、独立双人筛选、一致性统计、实验复现或跨研究效果排名。正文说明来源限制及 AI 辅助的实际范围。

引用保留经检查的原始来源；已知 DOI 优先保留 DOI，arXiv 文献使用可点击标识，避免同时打印相同链接。预印本年份沿用首次公开年份，不能据此推断最终发表年份。部分正式出版字段仍待规范化。

## 编译

在本目录运行：

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

需要支持 acmart 的完整 TeX 环境。本机使用已有 MiKTeX 编译；内置编辑器用于修改入口文件。本轮内置编译器报环境目录错误，输出 PDF 由本机 MiKTeX 生成，未新增安装。

## 本轮验证

全部 95 个唯一书目键都有正文引用；无未定义引用、overfull 警告。已检查全部页面缩略图及主图、信息权限表和基准表的放大图。正文与 Data Availability 位于第 18 页，参考文献独立为 4 页，总计 22 页。

BibTeX 仍有 21 项出版地、页码等缺失字段提示。已保留真实来源和已验证标识，没有为消除提示补造元数据。source-metadata.json 保存此前来源核查；新增 35 条的来源状态、版本与检查深度保存在上一级的 supplemental-search.json。

## 图与材料

主图保持用户确认的 figures/construction-overview-illustrated.pdf，含可编辑 SVG 与 PNG；模型以匹配的紫色芯片图标表示。图 2、3 分别为代表性文献地图和质量证据关系图，不是全量频率统计。主图在第 3 页，其余两图在第 6、14 页。

矢量重绘源为 figures/illustrated_vector.py；其他两图由 figures/draw_figures.py 生成。main-figure-concept.png 是早期构图草图，不是正文中的最终图。三个矢量 PDF 保持更新前的文件内容。

调研材料已在用户创建的公开开发仓库发布。匿名审稿访问端点尚未配置；当前 Data Availability 如实说明此状态，未将作者身份链接放入匿名稿件。提交前仍需完成匿名访问配置及完整研究编码验证。
