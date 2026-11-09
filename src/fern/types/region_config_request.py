from __future__ import annotations
from pydantic import Field
from typing import Optional
from typing import Any
from .utils.base_model import BaseModel
from .twilio_region_id import TwilioRegionId
from .twilio_edge_location import TwilioEdgeLocation


class RegionConfigRequest(BaseModel):
    """RegionConfigRequest

    :param region_id: Valid Twilio region IDs.
    :type region_id: TwilioRegionId
    :param token: Auth Token for this region
    :type token: str
    :param edge_location: Valid Twilio edge locations.
    :type edge_location: TwilioEdgeLocation
    """

    region_id: TwilioRegionId = Field(description="Valid Twilio region IDs.")
    token: str = Field(description="Auth Token for this region")
    edge_location: TwilioEdgeLocation = Field(
        description="Valid Twilio edge locations."
    )
