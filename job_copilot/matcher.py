from __future__ import annotations

from dataclasses import asdict, dataclass
import re


SKILL_ALIASES: dict[str, tuple[str, ...]] = {
    "AI 产品设计": ("ai 产品", "ai product", "智能产品"),
    "用户研究": ("用户研究", "用户访谈", "user research"),
    "需求分析": ("需求分析", "需求拆解", "requirement"),
    "PRD": ("prd", "产品需求文档"),
    "原型设计": ("原型", "prototype", "figma", "axure"),
    "数据分析": ("数据分析", "sql", "指标体系", "埋点"),
    "大模型": ("大模型", "llm", "prompt", "提示词"),
    "Agent": ("agent", "智能体", "mcp", "skill"),
    "效果评估": ("评测", "效果评估", "evaluation", "eval"),
    "项目管理": ("项目管理", "跨团队", "协同", "推进落地"),
    "Python": ("python",),
    "Git": ("git", "github", "版本控制"),
    "Docker": ("docker", "容器"),
}


@dataclass(frozen=True)
class MatchResult:
    score: int
    matched: list[str]
    missing: list[str]
    evidence: list[str]
    recommendations: list[str]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def _normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def _detected_skills(text: str) -> set[str]:
    normalised = _normalise(text)
    return {
        skill
        for skill, aliases in SKILL_ALIASES.items()
        if any(alias.lower() in normalised for alias in aliases)
    }


def analyse_match(candidate_profile: str, job_description: str) -> MatchResult:
    """Compare a candidate profile with a job description.

    The first version intentionally uses an explainable keyword baseline. This
    makes every score traceable and creates a benchmark for a later LLM-based
    implementation.
    """

    if not candidate_profile.strip():
        raise ValueError("候选人经历不能为空")
    if not job_description.strip():
        raise ValueError("岗位描述不能为空")

    candidate_skills = _detected_skills(candidate_profile)
    required_skills = _detected_skills(job_description)

    if not required_skills:
        return MatchResult(
            score=0,
            matched=[],
            missing=[],
            evidence=["岗位描述中没有识别到预设能力关键词。"],
            recommendations=["补充更完整的岗位职责和任职要求后重新分析。"],
        )

    matched = sorted(candidate_skills & required_skills)
    missing = sorted(required_skills - candidate_skills)
    score = round(len(matched) / len(required_skills) * 100)

    evidence = [f"个人经历和岗位描述都提到了“{skill}”。" for skill in matched]
    if not evidence:
        evidence = ["当前未找到双方明确重合的能力关键词。"]

    recommendations = [
        f"如果确有相关经历，请在简历中补充“{skill}”的项目证据和结果。"
        for skill in missing[:3]
    ]
    if not recommendations:
        recommendations = ["能力关键词覆盖较完整，下一步应强化量化结果和个人贡献。"]

    return MatchResult(
        score=score,
        matched=matched,
        missing=missing,
        evidence=evidence,
        recommendations=recommendations,
    )

