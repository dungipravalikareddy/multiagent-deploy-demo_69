# app/agents.py
# Simple "Researcher" and "Writer" components using LangChain + OpenAI.
# Keep minimal: each "agent" is a prompt wrapper around an LLM call.

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    # If you want to fail fast on missing key when running locally
    # comment this out when running in environments that provide secrets separately.
    raise ValueError("Please set OPENAI_API_KEY in your environment or .env file")

# Create LLM once and share (explicit API key ensures env read)
_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2, api_key=OPENAI_API_KEY)

def researcher(topic: str) -> str:
    """
    Researcher agent: returns short bullet points about the topic.
    Simple prompt -> generator call.
    """
    prompt_tmpl = PromptTemplate.from_template(
        "You are a concise researcher. Provide 4 bullet points of factual information about: {topic}."
    )
    prompt = prompt_tmpl.format(topic=topic)
    # use the underlying LLM invoke to get content
    # ✅ new
    resp = _llm.invoke(prompt)  # just send the string directly
    return resp.content if hasattr(resp, "content") else str(resp)


def writer(research_notes: str, tone: str = "neutral") -> str:
    """Writer agent: turns notes into a short article."""
    prompt_tmpl = PromptTemplate(
        input_variables=["tone", "notes"],
        template="You are a {tone} writer. Turn these notes into a ~200 word article:\n\n{notes}"
    )
    prompt = prompt_tmpl.format(tone=tone, notes=research_notes)

    # Call LLM directly with string
    resp = _llm.invoke(prompt)

    return resp.content if hasattr(resp, "content") else str(resp)
