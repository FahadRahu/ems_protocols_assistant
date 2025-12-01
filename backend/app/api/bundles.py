"""
Bundle API endpoints.
Serves the compiled JSON bundle to the frontend PWA.
"""
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.config import settings

router = APIRouter(prefix="/api/v1/bundles", tags=["bundles"])


@router.get("/latest")
async def get_latest_bundle():
    """
    Get the latest protocol bundle.
    Frontend calls this on startup to check for updates.
    """
    bundle_dir = settings.bundle_output_dir
    bundles = sorted(bundle_dir.glob("pwc_protocols_v*.json"), reverse=True)
    
    if not bundles:
        raise HTTPException(status_code=404, detail="No bundles available")
    
    return FileResponse(
        bundles[0],
        media_type="application/json",
        headers={"Cache-Control": "max-age=3600"}
    )


@router.get("/version")
async def get_bundle_version():
    """Get current bundle version without downloading full bundle."""
    bundle_dir = settings.bundle_output_dir
    bundles = sorted(bundle_dir.glob("pwc_protocols_v*.json"), reverse=True)
    
    if not bundles:
        raise HTTPException(status_code=404, detail="No bundles available")
    
    # Extract version from filename
    version = bundles[0].stem.replace("pwc_protocols_v", "").replace("_", ".")
    return {"version": version, "filename": bundles[0].name}
