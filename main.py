from datetime import datetime
from pathlib import Path

Path("docs/").mkdir(parents=True, exist_ok=True)
now = datetime.now()
Path("docs/sample.txt").write_text(str(now))
