from alchemy.grimoire.dark_spellbook import dark_spell_record


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    print(f"Testing record light spell: "
          f"{dark_spell_record('Curse', 'Eyeball, arsenic and bat')}")
    print()


if __name__ == "__main__":
    main()
