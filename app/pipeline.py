# app/pipeline.py
# Orchestration that runs researcher -> writer and returns outputs.

from app.agents import researcher, writer

def run_workflow(topic: str, tone: str = "neutral"):
    """
    Run the simple multi-agent workflow.
    Returns: dict with researcher_notes and final_draft
    """
    notes = researcher(topic)
    draft = writer(notes, tone=tone)
    return {"notes": notes, "draft": draft}
