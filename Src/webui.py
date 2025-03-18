import gradio as gr
import subprocess
import os
import psutil

# Track processes
process_adf = None  
process_upwork = None  
process_github = None  

def start_monitoring():
    """Start the ADF monitoring script"""
    global process_adf
    if process_adf is None:
        script_path = os.path.join(os.path.dirname(__file__), "adf_monitor.py")
        process_adf = subprocess.Popen(["python", script_path], shell=True)
        return "✅ ADF Monitoring started!"
    return "⚠️ ADF Monitoring is already running."

def stop_monitoring():
    """Stop the ADF monitoring script"""
    global process_adf
    if process_adf:
        process_adf.terminate()
        process_adf.wait()
        process_adf = None
        return "❌ ADF Monitoring stopped!"
    return "⚠️ No active ADF Monitoring process found."

def start_upwork():
    """Start the Upwork automation"""
    global process_upwork
    if process_upwork is None:
        script_path = os.path.join(os.path.dirname(__file__), "upwork_bot.py")
        process_upwork = subprocess.Popen(["python", script_path], shell=True)
        return "✅ Upwork Automation started!"
    return "⚠️ Upwork Automation is already running."

def stop_upwork():
    """Stop the Upwork automation"""
    global process_upwork
    if process_upwork:
        process_upwork.terminate()
        process_upwork.wait()
        process_upwork = None
        return "❌ Upwork Automation stopped!"
    return "⚠️ No active Upwork Automation found."

def run_github_process():
    """Run GitHub process and return output"""
    global process_github
    if process_github is None:
        script_path = os.path.join(os.path.dirname(__file__), "github_integration.py")
        process_github = subprocess.Popen(["python", script_path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process_github.communicate()
        process_github = None  # Reset after execution
        return f"✅ GitHub Process Result:\n{stdout}\n{stderr}" if stdout or stderr else "✅ GitHub Process Completed!"
    return "⚠️ GitHub Process is already running."

def send_email_alert():
    """Trigger an email alert"""
    script_path = os.path.join(os.path.dirname(__file__), "email_alerts.py")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    return f"📧 Email Alert Sent!\n{result.stdout if result.stdout else result.stderr}"

def check_status():
    """Check status of all processes"""
    status = []
    
    if process_adf and psutil.pid_exists(process_adf.pid):
        status.append("🔵 ADF Monitoring: Running")
    else:
        status.append("⚪ ADF Monitoring: Not Running")

    if process_upwork and psutil.pid_exists(process_upwork.pid):
        status.append("🔵 Upwork Automation: Running")
    else:
        status.append("⚪ Upwork Automation: Not Running")

    if process_github and psutil.pid_exists(process_github.pid):
        status.append("🔵 GitHub Process: Running")
    else:
        status.append("⚪ GitHub Process: Not Running")

    return "\n".join(status)

# Create WebUI
with gr.Blocks() as ui:
    gr.Markdown("## 🚀 **ADF & Upwork Automation Control Panel**")

    with gr.Row():
        start_adf_btn = gr.Button("Start ADF Monitoring ✅")
        stop_adf_btn = gr.Button("Stop ADF Monitoring ❌")
    
    with gr.Row():
        start_upwork_btn = gr.Button("Start Upwork Automation 🚀")
        stop_upwork_btn = gr.Button("Stop Upwork Automation ❌")

    with gr.Row():
        github_btn = gr.Button("Run GitHub Process 🔄")
        email_alert_btn = gr.Button("Send Email Alert 📧")

    status_btn = gr.Button("Check Status 📌")
    output = gr.Textbox(label="Status & Output", interactive=False)

    # Click Actions
    start_adf_btn.click(start_monitoring, outputs=output)
    stop_adf_btn.click(stop_monitoring, outputs=output)
    start_upwork_btn.click(start_upwork, outputs=output)
    stop_upwork_btn.click(stop_upwork, outputs=output)
    github_btn.click(run_github_process, outputs=output)
    email_alert_btn.click(send_email_alert, outputs=output)
    status_btn.click(check_status, outputs=output)

# Launch WebUI
ui.launch()
