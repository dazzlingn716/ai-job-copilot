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

## Docker 运行

```bash
docker build -t ai-job-copilot:v1 .
docker run -d --name ai-job-copilot -p 8000:8000 ai-job-copilot:v1
```

浏览器仍访问 `http://localhost:8000`。可使用下面的命令查看状态和日志：

```bash
docker ps
docker logs ai-job-copilot
```

## Docker Compose 运行

在已经创建 `ai-job-data` 数据卷和 `ai-job-network` 网络后运行：

```bash
docker compose up -d
docker compose ps
```

Compose 版本使用 `http://localhost:8001`，停止时运行 `docker compose down`。

## 运行测试

```bash
python -m pytest -q
```

## 后续实验扩展

- 实验 3：加入 Dockerfile、Volume、网络和 Docker Compose；
- 实验 4：加入故障版本、pytest 调试过程、AGENTS.md、Skill、MCP 与权限控制。

详细产品设计见 [`docs/PRD.md`](docs/PRD.md)。
