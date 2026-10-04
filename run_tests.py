from pathlib import Path
import yaml

cases = yaml.safe_load(
    Path("test_cases.yaml").read_text(encoding="utf-8")
)

print(f"Loaded {len(cases)} test cases\n")

for case in cases:
    print(f"{case['id']} | {case['category']}")
    print(f"Input: {case['input']}")
    print(f"Expected: {case['expected']}")
    print("-" * 70)