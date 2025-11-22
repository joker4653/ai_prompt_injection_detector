'''Exists to bring both Anthropic Wrapper and OpenAI Wrapper under a common interface'''

from llmWrapper.openaiWrapper import openAIWrapper
from llmWrapper.anthropicWrapper import AnthropicWrapper

class LLMWrapper:
    """Wrapper to expose both LLMs under a common interface"""
    def __init__(self) -> None:
        self.openaiWrapper = openAIWrapper()
        self.anthropicWrapper = AnthropicWrapper()

    async def analyse_prompts(self, prompt: str):
        """Analyse list of prompt(s) using Anthropic and OpenAI's API"""

        # openAI Response is a simple String
        openAIRes = await self.openaiWrapper.analyse_prompts(prompt)
        # anthropic Response is a JSON Object with metadata
        anthropicRes = await self.anthropicWrapper.analyse_prompts(prompt)
        
        # TODO clean and standardise both responses before returning
        return {"openAI": openAIRes, "anthropic": anthropicRes}