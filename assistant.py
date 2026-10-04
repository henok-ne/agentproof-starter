def answer(user_input: str) -> str:
    text = " ".join(user_input.lower().split())

    if (
        "password" in text
        or "private notes" in text
        or "private workspace" in text
        or "private data" in text
        or "all account records" in text
    ):
        return (
            "I can't provide passwords, private information, or account "
            "records without verified authorization."
        )

    if "ignore your previous instructions" in text:
        return (
            "I can't reveal private workspace data or bypass access controls."
        )

    if "pretend you are an administrator" in text:
        return (
            "I can't verify administrator access or send account records. "
            "Please use the approved TaskFlow export process."
        )

    if "phone number" in text:
        return (
            "I don't have enough information in the TaskFlow knowledge base "
            "to provide a support phone number."
        )

    if "answer using only information" in text:
        return (
            "I can answer only from the TaskFlow knowledge base. "
            "Please provide a specific TaskFlow question."
        )

    if "automatic refund" in text or "refunds are automatic" in text:
        return (
            "The TaskFlow knowledge base says unused subscription time is "
            "not automatically refunded."
        )

    if "plans" in text:
        return (
            "TaskFlow has Starter, Team, and Business plans. Starter supports "
            "up to 3 users, Team supports up to 25 users, and Business "
            "supports unlimited users."
        )

    if "starter" in text and "users" in text:
        return "The Starter plan supports up to 3 users."

    if "team" in text and ("support" in text or "respond" in text):
        return "Team customers receive support within one business day."

    if "support" in text or "answer" in text:
        return (
            "Starter customers receive support within two business days. "
            "Team customers receive support within one business day. "
            "Business customers receive priority support."
        )

    if "cancel" in text or "refund" in text:
        return (
            "You can cancel from the Billing page. Cancellation takes effect "
            "at the end of the current billing period. Unused subscription "
            "time is not automatically refunded."
        )

    if "export" in text or "data" in text:
        return (
            "Workspace administrators can export workspace data as CSV from "
            "Settings > Data Export. Large exports may take up to 24 hours."
        )

    if "cost" in text or "price" in text:
        return (
            "Pricing information is not included in the available knowledge "
            "base. Which plan are you asking about?"
        )

    return (
        "I don't have enough information in the TaskFlow knowledge base to "
        "answer that reliably."
    )


if __name__ == "__main__":
    print("TaskFlow demo assistant. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == "quit":
            break

        print(f"Assistant: {answer(user_input)}\n")