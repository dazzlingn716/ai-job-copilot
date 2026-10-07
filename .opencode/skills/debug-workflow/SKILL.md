---
name: debug-workflow
description: Diagnose and fix Python test failures with an evidence-based Observe-Hypothesize-Plan-Execute-Verify workflow. Use when pytest fails or application behavior differs from expectations.
---

# Debug Workflow

1. **Observe**：运行最小相关测试，记录失败用例、断言、实际值和期望值。
2. **Hypothesize**：根据代码和证据提出最可能的根因，不要在没有证据时同时修改多个位置。
3. **Plan**：列出最小修复方案、需要保留的回归测试以及可能影响的已有行为。
4. **Execute**：只修改解决根因所需的代码，不删除失败测试，不降低断言。
5. **Verify**：先运行失败用例，再运行全部测试；报告通过数量和仍存在的风险。

每次调试都输出以下小结：

- 失败现象
- 根因假设
- 修改内容
- 验证命令与结果
- 是否存在未解决风险

