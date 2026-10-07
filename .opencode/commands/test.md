---
description: 按 Debug Skill 运行测试并修复失败
agent: build
---

加载 `debug-workflow` Skill，然后使用 `.venv/bin/python -m pytest -q` 运行项目测试。若测试失败，严格执行 Observe、Hypothesize、Plan、Execute、Verify 流程，直到全部测试通过或明确说明阻塞原因。最后总结测试结果和修改内容。

