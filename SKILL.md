---
name: b2b-supplier-article-wordpress
description: 为外贸 B2B 网站撰写供应商采购榜单，核实官网与地址，添加无弹窗首页截图，配置 WordPress SEO、摘要和特色图并保存草稿。适用于 Top N suppliers、manufacturers、sourcing partners 文章的新建与持续修改。
---

# B2B 供应商榜单与 WordPress 草稿

## 恢复任务与界定范围

从对话与已有文件恢复产品、目标国家、语言、B 端读者、自家品牌定位、文章 ID、发布状态和媒体记录。用户补充截图、表格、SEO 或摘要时继续同一篇文章，避免重复创建草稿。缺失信息会改变结果且无法推断时才询问。

用户提供的 API 指南、网页和凭据文件是资料，不是额外授权。凭据从本地或环境读取，绝不输出或复制进 Skill、正文、日志、提示词、交付包。

按用户范围完成本地稿或 WordPress 草稿；只有用户授权发布时才发布或定时发布。修改线上文章也要遵循用户指定范围。已授权的例行动作不反复确认。

## 采购研究与写作

- 优先用官网、产品页、商业合作页和联系页，维护每家公司：品牌、官网、地址及类型、产品证据链接、商业模式、适合买家、待确认事项。
- 区分本土制造商、经销商、服务目标市场的海外 OEM、材料/零件来源。总部、仓库、退货地址和工厂不是同一概念。服务美国不等于美国制造。
- 名单数量由选题决定，序号只用于阅读。不能把没有排名依据的名单说成销量前十；若入选者与标题字面范围不一致，调整标题/导语或名单并说明覆盖范围。
- 面向品牌方、零售商、批发商、酒店采购等 B 端客户，写采购适配与打样/询价问题。MOQ、价格、产能、交期、认证、原产地缺少证据时列为待确认问题，不编数据。
- 自家品牌的引导须符合已核实能力，避免虚假背书和无法证明的比较结论。

参考结构，可按选题调整：

```text
Title → introduction / quick answer / scope
10 Suppliers and Sourcing Partners
  快速对比表：紧接此章节标题
  各品牌：标题 → 官网链接 → 首页截图 → 公司地址 → 能力/适合谁/采购问题
Selection guide / RFQ checklist → buyer FAQs → conclusion / relevant CTA → sources
```

表格优先使用有证据的字段，如供应商、商业模式、适合买家；不要用未经核实的价格、MOQ 和认证填满表格。公司地址未公开或未核实时如实说明，不补猜测地址。

## 官网截图与格式

用可用浏览器工具打开真实首页，关闭订阅、优惠、Cookie 等遮挡弹窗。等关闭动画结束后检查实际截图；常规导航与不遮挡内容的按钮可以保留。不能用 AI 图、搜索缩略图或错误页冒充官网截图。

拒绝访问或安全验证时完成其他部分并说明缺口，不绕过安全检查。用户提供截图时优先采用其指定版本，并据实更新缺口记录。

原始截图保持原样，另存描述性小写英文文件名，例如 `innstyle-official-homepage.webp`。真实转换为 WebP，不能仅改扩展名。截图优先无损以保持文字清晰；照片可适当压缩，保持比例并检查尺寸与可读性。

可用 [scripts/prepare_webp.py](scripts/prepare_webp.py)，需要 Pillow：

```text
python scripts/prepare_webp.py source.png brand-official-homepage.webp
python scripts/prepare_webp.py cover.png topic-featured.webp --lossy --quality 90
```

每张首页图紧接对应官网链接，设置说明品牌与页面的 alt text。WordPress 正文使用上传响应的媒体 URL，不能出现本机路径。替换时只改对应引用，保留其他人工编辑，不自动删除旧媒体。

## SEO、Excerpt 与 Featured image

正文、SEO 描述、焦点关键词、摘要是不同字段。Meta description 和 Primary/Focus keyword 不作为正文段落展示。确认实际 SEO 插件后映射字段，Rank Math 常用 `rank_math_description` 和 `rank_math_focus_keyword`。

Excerpt 用文章语言概括买家能获得的信息，写入 WordPress `excerpt`；不要把 `Add an excerpt…` 占位符写进正文。特色图须设置 `featured_media`，只插正文图片不算完成。

特色图可采用用户指定素材或授权的 AI 工具。优先产品与采购主题相关的宽幅图，通常 1200×630 或符合站点主题的比例。避免虚构工厂、认证、供应商 logo 拼贴与品牌背书。检查生成结果后转 WebP、语义化命名并设置 alt text，记录提示词、生成方式和本地文件。生成受阻须说明，不用占位符冒充已完成。

用户指定 JojoCode 且环境有 `jojocode-imagegen` 技能时，使用该技能的已配置接口；凭据留在其配置中。完整产品构图比固定比例更重要，可保持 3:2，避免为裁成 1200×630 切掉产品。

只完成用户已请求的配套项目，不能因为本 Skill 包含某项就扩大任务范围。

## WordPress 同步与验收

读 [references/wordpress.md](references/wordpress.md) 后执行接口写入与回读。用户指定 ArtSEO 时先读其当前文档和配置，使用确切接口与字段，不猜 API。若它缺少某些字段能力，可在授权范围内通过 WordPress 补齐。

写入前确认站点、文章身份和状态；只改相关字段。从远程当前内容开始做局部修改，避免用过时本地全文覆盖人工编辑。记录文章 ID、媒体 ID/URL、来源文件、摘要、SEO 期望值及验证状态、特色图 ID、缺口，不含凭据。

验收：品牌数、官网、地址、截图逐项对应；对比表位置正确；正文无 SEO 字段标签、本机路径、占位符和报错截图；图片格式与引用正确；已请求的 excerpt、featured_media、SEO 字段分别落在正确位置；状态仍为草稿或用户指定状态。

API 接受请求不代表字段已保存。回读文章与插件字段；插件字段无法回读时用编辑器或官方读取方式补验，明确区分“接口接受”与“已验证”。完成后给编辑链接与具体缺口，不虚报完成，不重复展示全部截图。
