# AI Job Copilot Agent Guide

## 项目目标

这是一个面向 AI 产品经理求职者的可解释岗位匹配 MVP。输入个人经历和岗位 JD，输出匹配分数、已匹配能力、待补能力、证据和行动建议。

## 技术栈

- Python 3.11+
- Flask
- pytest
- HTML/CSS
- Docker 与 Docker Compose

## 目录结构

- `app.py`：Flask 路由与页面入口
- `job_copilot/`：核心匹配逻辑
- `tests/`：pytest 自动化测试
- `templates/`、`static/`：页面模板与样式
- `docs/`：PRD、实验记录和调试证据
- `.opencode/`：OpenCode Skill、Agent 与自定义命令

## 常用命令

```bash
.venv/bin/python -m pytest -q
python app.py
docker build -t ai-job-copilot:v1 .
docker compose up -d
```

## 开发规范

1. 使用中文解释分析结论，代码标识符保持英文。
2. 修改匹配逻辑前先补充或更新测试。
3. 保持算法可解释，每个匹配结果都必须能追溯到关键词证据。
4. 优先进行小而明确的修改，避免无关重构。
5. 修改完成后运行全部 pytest 测试。
6. 不在代码中保存真实密码、API Key、Cookie 或个人隐私。

## 禁止操作

- 不得直接删除整个项目、`.git` 或测试目录。
- 不得使用 `git reset --hard`、强制推送或覆盖他人提交。
- 未经用户确认不得执行 `git push`、删除容器/数据卷或安装系统软件。
- 不得为了让测试通过而删除测试或降低断言强度。

