"""
Protocol CRUD API endpoints.
Used by the Admin Panel for protocol management.
"""
from fastapi import APIRouter, HTTPException

from app.models.protocol import Protocol

router = APIRouter(prefix="/api/v1/protocols", tags=["protocols"])


@router.get("/", response_model=list[Protocol])
async def list_protocols():
    """List all protocols."""
    # TODO: Implement database query
    return []


@router.get("/{protocol_id}", response_model=Protocol)
async def get_protocol(protocol_id: str):
    """Get a specific protocol by ID."""
    # TODO: Implement database query
    raise HTTPException(status_code=404, detail=f"Protocol {protocol_id} not found")


@router.post("/", response_model=Protocol)
async def create_protocol(protocol: Protocol):
    """Create a new protocol."""
    # TODO: Implement database insert
    return protocol


@router.put("/{protocol_id}", response_model=Protocol)
async def update_protocol(protocol_id: str, protocol: Protocol):
    """Update an existing protocol."""
    # TODO: Implement database update
    return protocol


@router.delete("/{protocol_id}")
async def delete_protocol(protocol_id: str):
    """Delete a protocol."""
    # TODO: Implement database delete
    return {"deleted": protocol_id}
