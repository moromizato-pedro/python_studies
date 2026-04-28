#!/usr/bin/env python3


from alchemy import elements as local_elem
from alchemy import potions
import elements as root_elem


def lead_to_gold():
    return (f"Recipe transmuting Lead to Gold: brew "
            f"'{local_elem.create_air()}' and '{potions.strength_potion()}' "
            f"mixed with '{root_elem.create_fire()}'")
