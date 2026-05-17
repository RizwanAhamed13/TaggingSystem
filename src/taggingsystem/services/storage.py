from pathlib import Path
from uuid import uuid4


class LocalStorage:
    def __init__(self, base_dir: str) -> None:
        self.base_path = Path(base_dir)
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save(self, filename: str, content: bytes) -> str:
        target = self.base_path / filename
        if target.exists():
            target = self.base_path / f"{target.stem}_{uuid4().hex[:8]}{target.suffix}"
        target.write_bytes(content)
        return f"file://{target.resolve()}"
