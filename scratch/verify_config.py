import os
import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from config_loader import load_config

def test_config():
    # Mock environment variables
    os.environ["PORT"] = "9999"
    os.environ["WEB_HOST"] = "0.0.0.0"
    
    config = load_config()
    
    print(f"Web Host: {config.web_dashboard.host}")
    print(f"Web Port: {config.web_dashboard.port}")
    
    assert config.web_dashboard.host == "0.0.0.0"
    assert config.web_dashboard.port == 9999
    print("Verification SUCCESS: Config loaded correctly from environment variables.")

if __name__ == "__main__":
    test_config()
