"""The iqos integration models."""

from __future__ import annotations

from dataclasses import dataclass

from .api import IQOSBLE

from .coordinator import IQOSBLECoordinator


@dataclass
class IQOSBLEData:
    """Data for the IQOS integration."""

    title: str
    device: IQOSBLE
    coordinator: IQOSBLECoordinator
