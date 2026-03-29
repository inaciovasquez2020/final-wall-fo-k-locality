from pathlib import Path

def test_core_schema_exists():
    assert Path("schema/core_invariants.schema.json").exists()

def test_end_to_end_example_exists():
    assert Path("examples/end_to_end.md").exists()
