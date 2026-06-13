"""pytest fixtures"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE))


@pytest.fixture()
def examples_dir() -> Path:
    return BASE / "examples"


@pytest.fixture()
def out_dir(tmp_path) -> Path:
    d = tmp_path / "out"
    d.mkdir(parents=True, exist_ok=True)
    return d


@pytest.fixture()
def sample_profile(examples_dir) -> dict:
    import json
    return json.loads((examples_dir / "sample_student_profile.json").read_text(encoding="utf-8"))
