import pytest

from job_copilot import analyse_match


def test_match_result_is_explainable():
    result = analyse_match(
        "负责 AI 产品需求分析，完成用户访谈、PRD 和原型设计。",
        "招聘 AI 产品经理，需要用户研究、需求分析、PRD、原型设计和数据分析能力。",
    )

    assert result.score == 83
    assert result.matched == ["AI 产品设计", "PRD", "原型设计", "用户研究", "需求分析"]
    assert result.missing == ["数据分析"]
    assert len(result.evidence) == 5


def test_empty_profile_is_rejected():
    with pytest.raises(ValueError, match="候选人经历不能为空"):
        analyse_match("", "需要需求分析能力")


def test_unknown_job_description_returns_guidance():
    result = analyse_match("有产品经验", "积极主动，责任心强")

    assert result.score == 0
    assert result.matched == []
    assert "补充" in result.recommendations[0]


def test_compact_ai_product_keyword_is_recognised():
    """Chinese job descriptions often omit the space in "AI 产品"."""
    result = analyse_match(
        "参与AI产品设计与需求分析。",
        "负责AI产品规划，需要需求分析能力。",
    )

    assert result.score == 100
    assert result.matched == ["AI 产品设计", "需求分析"]

