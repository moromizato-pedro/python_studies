import alchemy.grimoire as grim

def main():
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    light_spell_record = grim.light_spellbook.light_spell_record
    print(f"Testing record light spell: "
          f"{light_spell_record('Fantasy', 'Earth, wind and fire')}")
    print()


if __name__ == "__main__":
    main()
