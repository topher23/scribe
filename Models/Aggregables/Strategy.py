from enum import Enum


class Strategy(Enum):
    DISTRESSED = "Distressed"
    GROWTH = "Growth"
    INDUSTRY_FOCUSED = "Industry Focused"
    VENTURE_CAPITAL = "Venture Capital"
    MIDDLE_BUYOUT = "Middle Buyout"
    LARGE_BUYOUT = "Large Buyout"