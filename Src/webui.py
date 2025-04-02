import gradio as gr
import logging
from typing import Dict, Any
from pathlib import Path

class WebUI:
    def __init__(self, **components):
        self.components = components
        self.logger = logging.getLogger(__name__)
        self.current_recording = None

    def create_recording_tab(self):
        """UI elements for recording management"""
        with gr.Tab("Recording Manager"):
            with gr.Row():
                record_btn = gr.Button("Start Recording")
                stop_btn = gr.Button("Stop Recording")
                save_btn = gr.Button("Save Recording")
            
            video_output = gr.Video(label="Current Recording", visible=False)
            recording_gallery = gr.Gallery(label="Saved Recordings")

            record_btn.click(
                self.start_recording,
                outputs=video_output
            )
            
            stop_btn.click(
                self.stop_recording,
                outputs=[video_output, recording_gallery]
            )

    def start_recording(self):
        """Start a new recording session"""
        recording_path = self.components["recording"].start_session()
        self.current_recording = recording_path
        return gr.Video.update(value=recording_path, visible=True)

    def stop_recording(self):
        """Stop current recording"""
        if self.current_recording:
            final_path = self.components["recording"].stop_session()
            return gr.Video.update(value=None, visible=False), self.update_gallery()
        return gr.Video.update(), self.update_gallery()

    def update_gallery(self):
        """Refresh recording gallery"""
        return self.components["recording"].list_recordings()

    def create_interface(self):
        """Build complete Gradio interface"""
        with gr.Blocks(title="AI Agent Control Panel") as demo:
            gr.Markdown("# AI Agent Dashboard")
            
            with gr.Tabs():
                self.create_recording_tab()
                # Add other component tabs here
                
        return demo

    def launch(self, **kwargs):
        """Launch the web interface"""
        interface = self.create_interface()
        interface.launch(**kwargs)