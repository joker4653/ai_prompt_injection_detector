"""Simple Engine to determine if a response contains prompt injection."""

from statistics import fmean

def evaluate_response(prompt_injection_responses: dict, output_validation_responses: dict) -> dict:
    """Evaluate responses from both LLMs using a rudimentary scoring system."""
    models = prompt_injection_responses.get("models", {})
    openAI = models.get("openAI", {}).get("score", {})
    anthropic = models.get("anthropic", {}).get("score", {})

    result = fmean([openAI, anthropic])

    match result:
        case r if r >= 7.0:
            evaluation = "Block"
        case r if 4.0 <= r < 7.0:
            evaluation = "Review"
        case r if r < 4.0:
            evaluation = "Ok"
        case _:
            evaluation = "Unable to determine likelihood of prompt injection."

    return {"evaluation": evaluation, "score": result}