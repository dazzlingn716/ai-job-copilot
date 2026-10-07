"""Minimal stdio MCP server for the AI Job Copilot experiment.

It exposes the project's explainable matching function as an external tool so
OpenCode can discover and call it through MCP without third-party credentials.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from job_copilot import analyse_match  # noqa: E402


TOOLS = [
    {
        "name": "analyse_job_match",
        "description": "Run the project's explainable job matching logic.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "profile": {"type": "string"},
                "job_description": {"type": "string"},
            },
            "required": ["profile", "job_description"],
            "additionalProperties": False,
        },
    },
    {
        "name": "project_summary",
        "description": "Return a concise summary of this project and its tests.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
]


def _response(message_id: object, result: dict[str, object]) -> dict[str, object]:
    return {"jsonrpc": "2.0", "id": message_id, "result": result}


def _handle(message: dict[str, object]) -> dict[str, object] | None:
    method = message.get("method")
    message_id = message.get("id")

    if method == "initialize":
        params = message.get("params") or {}
        protocol_version = params.get("protocolVersion", "2024-11-05")
        return _response(
            message_id,
            {
                "protocolVersion": protocol_version,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "ai-job-copilot-mcp", "version": "1.0.0"},
            },
        )

    if method == "tools/list":
        return _response(message_id, {"tools": TOOLS})

    if method == "tools/call":
        params = message.get("params") or {}
        name = params.get("name")
        arguments = params.get("arguments") or {}

        if name == "analyse_job_match":
            result = analyse_match(
                str(arguments.get("profile", "")),
                str(arguments.get("job_description", "")),
            )
            text = json.dumps(result.to_dict(), ensure_ascii=False, indent=2)
        elif name == "project_summary":
            test_count = sum(1 for _ in (PROJECT_ROOT / "tests").glob("test_*.py"))
            text = (
                "AI Job Copilot 是一个 Flask 岗位匹配 MVP；"
                f"当前包含 {test_count} 个测试文件，并使用 pytest、Docker 和 Git 管理。"
            )
        else:
            return {
                "jsonrpc": "2.0",
                "id": message_id,
                "error": {"code": -32601, "message": f"Unknown tool: {name}"},
            }

        return _response(message_id, {"content": [{"type": "text", "text": text}]})

    if message_id is not None:
        return {
            "jsonrpc": "2.0",
            "id": message_id,
            "error": {"code": -32601, "message": f"Unknown method: {method}"},
        }
    return None


def main() -> None:
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            response = _handle(json.loads(line))
        except Exception as exc:  # Keep protocol errors on stdout as JSON-RPC.
            response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": str(exc)},
            }
        if response is not None:
            print(json.dumps(response, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
