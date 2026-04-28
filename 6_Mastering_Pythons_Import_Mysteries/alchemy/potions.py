#!/usr/bin/env python3


from . import elements as local_elem

import elements as root_elem


def healing_potion() -> str:
    return (f"Healing potion brewed with '{local_elem.create_earth()}' and "
            f"'{local_elem.create_air()}'")


def strength_potion() -> str:
    return (f"Strength potion brewed with '{root_elem.create_fire()}' "
            f"and '{root_elem.create_water()}'")
