"""执行 demo 流程的脚本入口"""

from __future__ import annotations

import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE))

from gaokao_agent.main import run_demo


def main() -> int:
    out_dir = BASE / "out"
    result = run_demo(str(out_dir))
    print(f"Demo 完成，文件数：{len(result['written_files'])}")
    for f in result["written_files"]:
        print(f"  - {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
