import json
from pathlib import Path
from typing import Dict, Any

def run_config_wizard(config_path: Path) -> Dict[str, Any]:
    print("\nAI Agent Configuration Wizard\n" + "="*30)
    
    config = {
        "recording": {
            "retention_days": int(input("Recording retention days (7): ") or "7"),
            "resolution": input("Recording resolution (1280x720): ") or "1280x720"
        },
        "storage": {
            "local_path": input("Storage path (./recordings): ") or "./recordings"
        }
    }
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\nConfiguration saved to {config_path}")
    return config