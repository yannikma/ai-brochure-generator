import gradio as gr
from chat_logic import chat

if __name__ == "__main__":
    gr.ChatInterface(fn=chat, type="messages").launch()
