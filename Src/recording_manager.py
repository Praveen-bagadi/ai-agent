from pathlib import Path
from datetime import datetime
import subprocess
import logging
from typing import List, Optional
from utils import ConfigManager

class RecordingManager:
    def __init__(self):
        self.config = ConfigManager()
        self.recording_dir = Path(self.config.get("storage/local_path", "./recordings"))
        self.current_session = None
        self.logger = logging.getLogger(__name__)
        self._setup()

    def _setup(self):
        """Initialize recording directory"""
        self.recording_dir.mkdir(exist_ok=True)
        self.logger.info(f"Recording storage initialized at {self.recording_dir}")

    def start_session(self) -> Path:
        """Start new recording session"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.current_session = self.recording_dir / f"session_{timestamp}.mp4"
        self.logger.info(f"Started recording session: {self.current_session}")
        return self.current_session

    def stop_session(self) -> Optional[Path]:
        """Finalize current recording session"""
        if not self.current_session:
            return None
            
        self.logger.info(f"Stopped recording: {self.current_session}")
        final_path = self.current_session
        self.current_session = None
        return final_path

    def list_recordings(self) -> List[Path]:
        """List all available recordings"""
        return sorted(self.recording_dir.glob("*.mp4"))

    def cleanup_old_recordings(self):
        """Remove recordings older than retention period"""
        retention_days = self.config.get("recording/retention_days", 7)
        cutoff = datetime.now().timestamp() - (retention_days * 86400)
        
        for recording in self.recording_dir.glob("*"):
            if recording.stat().st_mtime < cutoff:
                recording.unlink()
                self.logger.info(f"Removed old recording: {recording.name}")