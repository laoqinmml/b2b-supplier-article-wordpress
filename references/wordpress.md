# WordPress REST 操作要点

Application Password 可用于 HTTPS REST Basic Auth，不是网页登录密码。只向用户指定的站点发送对应凭据，不输出 header。先用 `GET /wp-json/wp/v2/users/me?context=edit` 验证身份和权限；有权限时通过 `/wp/v2/plugins` 确认 SEO 插件，用 `/wp-json/` 和 OPTIONS 发现路由与 schema。

优先使用已有 post ID。无 ID 时按题目/slug/状态查找，一次空搜索不能证明没有草稿。部分站点 `status=any` 或草稿查询可能返回 500，应核实已有记录或编辑器，避免重复 POST。网络超时后先查已知 ID，不盲目重建。

本次环境出现 Python urllib 默认请求 403、PowerShell `Invoke-RestMethod` 成功的差异；检查请求/服务响应，不把换客户端当成绕过安全防护。401 先检查凭据解析，403/500 检查接口能力；有限重试后说明阻碍并继续本地工作。

```text
POST /wp-json/wp/v2/posts
  title, slug, content, status="draft", excerpt
POST /wp-json/wp/v2/posts/{id}
  只传本次修改字段
GET /wp-json/wp/v2/posts/{id}?context=edit
  回读 content.raw、excerpt.raw、status、featured_media
POST /wp-json/wp/v2/media
  Content-Type: image/webp
  Content-Disposition: attachment; filename="brand-official-homepage.webp"
  body: 文件真实字节
POST /wp-json/wp/v2/media/{id}
  alt_text, title, post
POST /wp-json/wp/v2/posts/{id}
  featured_media: 封面媒体 ID
```

保存媒体响应的 id、source_url、mime_type；不要推测 URL，WordPress 可能缩放或加后缀。先保存媒体状态再继续，重试前核实副作用。JSON 结构化序列化并按 UTF-8 发送，不拼接未转义正文。

部分站点的自定义处理可能在只更新特色图时清空 excerpt。本次站点实测出现过这一行为，随后将期望的 excerpt 与 featured_media 同时提交并回读恢复。更新前保留当前内容、摘要与状态，更新后比较相关字段；若发现这种副作用，只恢复任务涉及且确认应保留的字段，不把此现象当成所有 WordPress 站点的标准行为。

Markdown 转 HTML 要用支持表格的解析器，可用时采用 PowerShell `ConvertFrom-Markdown`。主题通常显示文章标题，正文避免重复 H1。局部替换采用唯一锚点或现有区块，确认仅命中预期位置。

## Rank Math

确认当前路由与权限后向 `POST /wp-json/rankmath/v1/updateMeta` 发送：

```json
{
  "objectType": "post",
  "objectID": 123,
  "meta": {
    "rank_math_description": "Article-specific search description.",
    "rank_math_focus_keyword": "primary keyword"
  }
}
```

插件元数据可能未在文章接口 meta schema 注册，直接传给 `/wp/v2/posts` 不一定保存。类似 `{"slug":true,"schemas":[]}` 的响应不能独立证明描述/关键词已保存，须用官方读取方式或编辑器确认。不要为方便读写擅自安装插件、改 PHP、暴露全部 meta 或降低权限限制。

## 状态记录

记录 site、post_id、edit_url、status、媒体来源/输出/id/url、excerpt、SEO 期望值及验证状态、featured_media、缺口。不得包含凭据。本次成功的写入方式只能作为环境参考，不能把站点、文章 ID、旧名单或凭据路径固定成通用脚本默认目标。
