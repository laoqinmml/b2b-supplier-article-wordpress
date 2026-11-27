# B2B Supplier Article → WordPress

面向外贸 B2B 网站的供应商采购榜单写作 Skill：从供应商事实核实，到带截图的英文或其他语言文章，再到 WordPress 草稿与配套字段。

## 能完成什么

- 根据产品、目标市场和采购人群建立供应商名单，区分制造商、经销商、海外 OEM 与材料来源。
- 核实官方网址与公司地址，编写商业模式、适合买家及询价/打样问题。
- 在供应商章节开头添加快速对比表，并在每家官网链接下放置无弹窗首页截图。
- 用户需要时，挑选与读者相关的 YouTube 视频放在文章前段并核实播放器显示。
- 接收用户提供的截图，语义化命名并真实转换为 WebP。
- 将 Meta description、Focus keyword、Excerpt 和 Featured image 写入各自字段，避免混进正文。
- 使用 WordPress REST API 保存草稿并回读检查；提供 Rank Math 接口参考。

默认保留草稿。发布或其他外部操作以用户当前授权为准。Skill 不包含账号、API 密钥、客户文章或图片素材，也不会自动安装 WordPress 插件。

## 安装

将仓库克隆到 Codex 的技能目录，目录名保持 `b2b-supplier-article-wordpress`。

```bash
git clone https://github.com/laoqinmml/b2b-supplier-article-wordpress.git ~/.codex/skills/b2b-supplier-article-wordpress
```

Windows PowerShell：

```powershell
git clone https://github.com/laoqinmml/b2b-supplier-article-wordpress.git "$HOME/.codex/skills/b2b-supplier-article-wordpress"
```

若设置了 `CODEX_HOME`，改用其下的 `skills` 目录。已存在同名技能时先检查，避免覆盖本地修改。刷新或重新打开客户端后调用。

## 使用

```text
使用 $b2b-supplier-article-wordpress，写一篇面向美国酒店采购和私人品牌商的
10 大记忆枕供应商文章，英文。每家附官网、地址和无弹窗首页截图，章节开头
加快速对比表。配置 SEO、摘要和特色图，保存到我指定的 WordPress 草稿。
```

提供目标站点、产品、目标市场、语言和现有文章 ID（如有）。通过本地配置提供凭据，不要粘贴到公开 issue。AI 配图需要独立可用且获授权的生图工具；JojoCode 仅在用户指定且安装了相应技能时使用，不是必需依赖。

## 图片转换工具

需要 Python 3 和 Pillow：

```bash
python -m pip install -r requirements.txt
python scripts/prepare_webp.py source.png brand-official-homepage.webp
python scripts/prepare_webp.py cover.png topic-featured.webp --lossy --quality 90 --max-width 1200
```

默认无损转换并验证像素一致性；保留源文件，拒绝覆盖已有输出。`--max-width` 只缩小、不放大。无损转换不能补回源文件已经丢失的细节。

## 文件

| 文件 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | Agent 执行流程和验收标准 |
| [references/wordpress.md](references/wordpress.md) | WordPress 与 Rank Math 接口细节 |
| [scripts/prepare_webp.py](scripts/prepare_webp.py) | 可独立使用的 WebP 转换工具 |
| [agents/openai.yaml](agents/openai.yaml) | Codex 展示信息与调用示例 |

网站访问限制、插件版本与站点自定义逻辑可能影响自动化。字段写入后应回读确认；无法核实的公司资料应标明缺口，不能用 AI 图冒充官网截图。
