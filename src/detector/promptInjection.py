from src.llmWrapper.llmWrapper import LLMWrapper

async def detect_prompt_injection_with_llm(llm: LLMWrapper, prompt : str) -> dict:
    llm = LLMWrapper()
    response = await llm.analyse_prompts(prompt)
    
    keywords = ["ignore previous", "disregard", "forget", "override", "bypass", "nevermind", "stop following", "cancel", "void", "nullify"]

    keywordsFound = []
    for k in keywords:
        if k in prompt.lower():
            keywordsFound.append(k)


    return {"keywords_found": keywordsFound, "models": response}