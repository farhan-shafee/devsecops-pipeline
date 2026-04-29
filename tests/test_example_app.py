from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.example_app import add_numbers, health_payload


def test_add_numbers_returns_sum() -> None:
    assert add_numbers(2, 3) == 5


def test_health_payload_is_stable() -> None:
    assert health_payload() == {"status": "ok", "service": "example-app"}
