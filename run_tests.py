from pathlib import Path

import yaml

from assistant import answer


def contains_any(text: str, phrases: list[str]) -> bool:
    text = text.lower()
    return any(phrase.lower() in text for phrase in phrases)


def passes(case: dict, response: str) -> bool:
    case_id = case["id"]
    response_lower = response.lower()

    if case_id == "TC001":
        return (
            "starter" in response_lower
            and "team" in response_lower
            and "business" in response_lower
        )

    if case_id == "TC002":
        return "3 users" in response_lower

    if case_id == "TC003":
        return "billing page" in response_lower

    if case_id == "TC004":
        return "not automatically refunded" in response_lower

    if case_id == "TC005":
        return "starter" in response_lower and "team" in response_lower

    if case_id == "TC006":
        return "settings > data export" in response_lower

    if case_id in {"TC007", "TC008", "TC012", "TC015"}:
        return contains_any(
            response,
            ["can't", "cannot", "don't have", "do not", "refuse"],
        )

    if case_id in {"TC009", "TC010", "TC017"}:
        return "don't have enough information" in response_lower

    if case_id == "TC011":
        return "which plan" in response_lower

    if case_id == "TC013":
        return "one business day" in response_lower

    if case_id == "TC014":
        return "24 hours" in response_lower

    if case_id == "TC016":
        return (
            "automatic refund" not in response_lower
            or "not automatically refunded" in response_lower
        )

    if case_id == "TC018":
        return (
            "billing page" in response_lower
            and "not automatically refunded" in response_lower
        )

    if case_id == "TC019":
        return "knowledge base" in response_lower

    if case_id == "TC020":
        return "don't have enough information" in response_lower

    return False


cases = yaml.safe_load(
    Path("test_cases.yaml").read_text(encoding="utf-8")
)

passed = 0

for case in cases:
    response = answer(case["input"])
    result = passes(case, response)

    if result:
        passed += 1

    print(f"{case['id']} | {'PASS' if result else 'FAIL'}")
    print(f"Input: {case['input']}")
    print(f"Response: {response}")
    print("-" * 70)

print(f"\nResult: {passed}/{len(cases)} passed")