# 贡献指南（CONTRIBUTING）

感谢你对 `gaokao-volunteer-agent` 的关注！本项目以 Apache License 2.0 开放源码，
欢迎以 Issue、PR、Discussion 等方式参与。

## 一、行为准则

请在所有互动中保持尊重与建设性。本项目服务于中国高考考生和家长，任何**可能误导考生**的贡献都不被接受：

- ❌ 提交伪造的录取线、位次、招生计划
- ❌ 提交把第三方数据当唯一依据的代码
- ❌ 提交会输出"保证录取""一定能上""百分百稳"等措辞的代码
- ❌ 提交默认联网抓取官方数据而未做合规评估的代码

## 二、提交流程

1. **Fork** 本仓库
2. 创建分支：`git checkout -b feat/your-feature`
3. 编写代码 + 测试 + 文档
4. 在本地通过测试：`pytest -q`
5. 在本地通过 demo：`gaokao-agent demo`
6. 提交：`git commit -m "feat: 你的功能描述"`
7. Push 并创建 PR

## 三、代码规范

- Python 3.10+
- 类型注解完整
- Pydantic 模型用于所有外部 schema
- 业务逻辑与 I/O 分离
- 路径使用 `pathlib.Path`
- 文件写入 UTF-8
- 中文错误信息

## 四、测试要求

- 新增业务逻辑必须附带 pytest 测试
- 整体测试保持 `pytest -q` 全部通过
- 不可降低现有测试覆盖率

## 五、提交信息规范

参考 Conventional Commits：

- `feat:` 新功能
- `fix:` 修复
- `docs:` 文档
- `test:` 测试
- `refactor:` 重构
- `chore:` 杂项

## 啬、合规

所有贡献默认遵循 Apache License 2.0。提交 PR 即表示你同意以 Apache 2.0 许可你的贡献。
