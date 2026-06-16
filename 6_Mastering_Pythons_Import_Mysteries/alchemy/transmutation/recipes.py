#!/usr/bin/env python3


from ..elements import create_air
from alchemy import potions
from elements import create_fire


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew "
            f"'{create_air()}' and '{potions.strength_potion()}' "
            f"mixed with '{create_fire()}'")
