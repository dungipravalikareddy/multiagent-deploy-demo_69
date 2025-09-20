import gradio as gr
from app.pipeline import run_workflow
from app.utils import check_openai_key

def run_demo(topic, tone):
    check_openai_key()
    outputs = run_workflow(topic, tone)
    return outputs["notes"], outputs["draft"]

iface = gr.Interface(
    fn=run_demo,
    inputs=[
        gr.Textbox(label="Topic", value="Impact of AI on Education"),
        gr.Radio(["neutral","friendly","formal"], label="Tone", value="neutral")
    ],
    outputs=[
        gr.Textbox(label="Researcher notes"),
        gr.Textbox(label="Writer draft")
    ],
    title="Multi-Agent Demo",
    description="Researcher -> Writer pipeline using LangChain + OpenAI"
)

if __name__ == "__main__":
    # Remove server_name/port and share
    iface.launch()
