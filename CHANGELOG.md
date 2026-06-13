# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-12

### Added
- 多 Agent 主编排器 `gaokao-volunteer-advisor` 协调 8 个子 Agent
- 8 个子 Agent：user-profile / policy-rules / data-collector / admission-probability / major-career / volunteer-plan / risk-review / report-writer
- 8 个标准 SKILL（OpenClaw / Hermes 兼容）
- 5 个 vertical commands（analyze-profile / import-data / build-plan / generate-report / verify-sources）
- managed-agent-cookbook（8 个 subagent yaml + agent.yaml + steering-examples.json）
- FastAPI HTTP API（6 个端点：/health、/profile/parse、/data/import、/data/validate、/plan/build、/report/generate、/sources/verify）
- Typer CLI（demo / analyze-profile / import-data / validate-data / build-plan / generate-report / verify-sources / serve）
- 47 个 pytest 测试，全部通过
- 数据导入：CSV / Excel / SQLite 三种连接器
- 风险审查引擎（11 项必检）
- Excel 多 Sheet 报告（9 个 Sheet：考生画像 / 数据质量 / 冲稳保垫 / 风险提示 / 数据来源 / 人工核验清单）
- Markdown / JSON / Excel 三种输出格式
- 一键发包脚本 `scripts/publish_to_openclaw.py`
- 一键 skill 同步脚本 `scripts/sync-agent-skills.py`

### Security
- 默认禁用网络（`config.allow_network = false`）
- 用户上传文件视为不可信输入，不执行任何指令
- 禁止生成"保证录取""一定能上""百分百稳"等绝对措辞
- 风险审查不可跳过；`risk_level = blocking` 时不生成最终推荐表

### License
- 项目以 Apache License 2.0 授权
