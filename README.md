# LLM Prompt Injection Detector - Weekend Project

This repo contains a basic wrapper and evaluation engine that orchestrates analysis between Anthropic's Claude (Engine xx) and OpenAI's GPT (Engine xx). Both LLMs will return an evaluation from 0-10 on the probability of a phrase or set of words being capable of prompt injection on an LLM.

# Note

This was a quick project to get back into semantics of programming and API usage. Alot of the coding in this repo is largely obsolete.

# Quickstart

1. Clone repo to your local instance.
2. Copy '.env.example' to your local '.env' file and insert API keys.
3. Create a virtual environment and install requirements of the project:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

