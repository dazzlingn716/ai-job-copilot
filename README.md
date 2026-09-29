# AI Job Copilot

一个面向求职者的可解释岗位匹配 MVP，也是实验 2—4 的统一实践项目。

## 当前版本：实验 2

- 在 Linux/WSL 中运行 Python Web 项目；
- 使用 Git 管理代码并推送远程仓库；
- 输入个人经历和岗位 JD；
- 输出匹配能力、能力缺口、依据和行动建议；
- 使用 pytest 验证核心匹配逻辑。

## 本地运行

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

浏览器访问 `http://localhost:8000`。

## 运行测试

```bash
python -m pytest -q
```

## 后续实验扩展

- 实验 3：加入 Dockerfile、Volume、网络和 Docker Compose；
- 实验 4：加入故障版本、pytest 调试过程、AGENTS.md、Skill、MCP 与权限控制。

详细产品设计见 [`docs/PRD.md`](docs/PRD.md)。
