from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "experiments" / "full_scale_tao_uncertainty.py"


if __name__ == "__main__":
    runpy.run_path(str(RUNNER), run_name="__main__")
