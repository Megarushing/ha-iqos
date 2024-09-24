from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class IQOSBLEState:
    case_battery: int = 0
    pen_discharged: bool = True
    is_open: bool = False
