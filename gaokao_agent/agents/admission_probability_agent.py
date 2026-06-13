# Copyright 2025-2026 Gaokao Volunteer Agent Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""录取概率分析 Agent"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from gaokao_agent.agents.base import BaseAgent
from gaokao_agent.connectors.local_db_connector import query_admissions
from gaokao_agent.models.admission import AdmissionAnalysis, AdmissionRecord
from gaokao_agent.models.student import StudentProfile
from gaokao_agent.services.admission_analyzer import analyze_records


class AdmissionProbabilityInput(BaseModel):
    profile: StudentProfile
    batch: str | None = "本科批"


class AdmissionProbabilityOutput(BaseModel):
    analyses: list[AdmissionAnalysis] = Field(default_factory=list)
    total_records_analyzed: int = 0
    sources: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)
    confidence: float = 0.0


class AdmissionProbabilityAgent(BaseAgent[AdmissionProbabilityInput, AdmissionProbabilityOutput]):
    name = "admission-probability-agent"
    description = "分析历史录取位次并进行风险分层"

    def run(self, input_data: AdmissionProbabilityInput) -> AdmissionProbabilityOutput:
        profile = input_data.profile
        # 在 session 内先把 ORM 对象转成 Pydantic，避免 detached instance
        from gaokao_agent.data.database import session_scope
        records: list[AdmissionRecord] = []
        with session_scope() as session:
            from gaokao_agent.data.repositories import AdmissionRecordORM
            q = session.query(AdmissionRecordORM)
            if profile.province:
                q = q.filter(AdmissionRecordORM.province == profile.province)
            if input_data.batch or profile.batch:
                q = q.filter(AdmissionRecordORM.batch == (input_data.batch or profile.batch))
            if profile.subject_type:
                q = q.filter(AdmissionRecordORM.subject_type == profile.subject_type)
            for r in q.all():
                records.append(AdmissionRecord(
                    province=r.province,
                    year=r.year,
                    school_code=r.school_code,
                    school_name=r.school_name,
                    major_group_code=r.major_group_code,
                    major_code=r.major_code,
                    major_name=r.major_name,
                    batch=r.batch,
                    subject_type=r.subject_type,
                    min_score=r.min_score,
                    min_rank=r.min_rank,
                    avg_score=r.avg_score,
                    avg_rank=r.avg_rank,
                    plan_count=r.plan_count,
                    tuition=r.tuition,
                    city=r.city,
                    school_level_tags=[t for t in (r.school_level_tags or "").split(",") if t],
                    major_tags=[t for t in (r.major_tags or "").split(",") if t],
                    selection_requirements=[t for t in (r.selection_requirements or "").split(",") if t],
                    source_name=r.source_name,
                    source_url=r.source_url,
                    source_date=r.source_date,
                    confidence=r.confidence,
                ))

        analyses = analyze_records(profile, records)

        warnings: list[str] = []
        if not records:
            warnings.append("未找到匹配的历史录取数据，请检查数据是否已导入。")
        if profile.rank is None:
            warnings.append("考生位次为空，无法进行可靠分析。")

        return AdmissionProbabilityOutput(
            analyses=analyses,
            total_records_analyzed=len(records),
            sources=["本地 SQLite 数据库"],
            warnings=warnings,
            confidence=min([a.confidence for a in analyses] or [0.0]),
        )
