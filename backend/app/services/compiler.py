"""
JSON Bundle Compiler
Exports database contents to a versioned JSON file for frontend consumption.
"""
import json
from pathlib import Path

from app.models.bundle import ProtocolBundle


class BundleCompiler:
    """Compiles protocol data into offline-ready JSON bundle."""
    
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def compile(self, bundle: ProtocolBundle) -> Path:
        """
        Compile and save the protocol bundle.
        Returns path to the generated JSON file.
        """
        version = bundle.meta.version.replace(".", "_")
        filename = f"pwc_protocols_v{version}.json"
        output_path = self.output_dir / filename
        
        with open(output_path, "w") as f:
            json.dump(bundle.model_dump(), f, indent=2)
        
        return output_path
    
    def compile_minified(self, bundle: ProtocolBundle) -> Path:
        """Compile minified version for production use."""
        version = bundle.meta.version.replace(".", "_")
        filename = f"pwc_protocols_v{version}.min.json"
        output_path = self.output_dir / filename
        
        with open(output_path, "w") as f:
            json.dump(bundle.model_dump(), f, separators=(",", ":"))
        
        return output_path
