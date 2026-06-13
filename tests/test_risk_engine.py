"""测试风险审查"""

from __future__ import annotations

from gaokao_agent.models.volunteer_plan import VolunteerCandidate, VolunteerPlan
from gaokao_agent.services.risk_engine import review_plan, review_text_for_prohibited, scan_prohibited_phrases


def _make_volunteer(school="示例大学", code="10001", has_source=True, requires_review=False):
    from gaokao_agent.models.source import SourceRef
    sources = [SourceRef(name="示例", is_official=False)] if has_source else []
    return VolunteerCandidate(
        school_code=code, school_name=school, risk_band="match", risk_score=0.5,
        sources=sources, requires_human_review=requires_review,
    )


def test_review_passing_plan():
    volunteers = [_make_volunteer() for _ in range(3)]
    plan = VolunteerPlan(
        student_province="广东", student_year=2026,
        risk_preference="conservative",
        total_slots=3, rush_count=1, match_count=1, safe_count=1,
        volunteers=volunteers, sources=["示例数据"],
    )
    res = review_plan(plan)
    assert res.passed
    assert res.risk_level in ("low", "medium")


def test_review_blocking_when_no_sources():
    plan = VolunteerPlan(
        student_province="广东", student_year=2026,
        risk_preference="conservative",
        total_slots=3, rush_count=1, match_count=1, safe_count=1,
        volunteers=[_make_volunteer(has_source=False)],
    )
    res = review_plan(plan)
    assert not res.passed
    assert res.risk_level == "blocking"
    assert not res.safe_to_generate_report


def test_review_blocking_when_no_volunteers():
    plan = VolunteerPlan(
        student_province="广东", student_year=2026,
        risk_preference="conservative",
    )
    res = review_plan(plan)
    assert not res.passed
    assert res.risk_level == "blocking"


def test_scan_prohibited_phrases_detects():
    found = scan_prohibited_phrases("这个学校保证录取，肯定能上")
    assert "保证录取" in found
    assert "肯定能上" in found


def test_scan_prohibited_phrases_clean():
    found = scan_prohibited_phrases("这是一个普通的志愿建议")
    assert found == []


def test_review_text_for_prohibited():
    blocking, warns = review_text_for_prohibited("百分百稳")
    assert len(blocking) > 0
    assert len(warns) > 0


def test_high_rush_ratio_warning():
    # 冲志愿占比 > 50%
    volunteers = [_make_volunteer() for _ in range(4)]
    for v in volunteers:
        v.risk_band = "rush"
    plan = VolunteerPlan(
        student_province="广东", student_year=2026,
        risk_preference="aggressive",
        total_slots=4, rush_count=4,
        volunteers=volunteers, sources=["x"],
    )
    res = review_plan(plan)
    assert any("冲志愿占比" in w for w in res.warnings)
