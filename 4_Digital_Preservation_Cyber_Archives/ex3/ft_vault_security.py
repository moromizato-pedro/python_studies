#!/usr/bin/env python3


def secure_archive(file_name: str, write: int = 0,
                   content: str = "") -> tuple[bool, str]:
    try:
        if not write:
            with open(file_name, "r") as f:
                content = f.read()
        else:
            with open(file_name, "w") as f:
                f.write(content)
        return (True, content)
    except (FileNotFoundError, PermissionError) as err:
        return (False, str(err))


def main() -> None:
    write = 1
    print("=== Cyber Archives Security ===")
    #
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))
    #
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("old_fragment.txt"))
    #
    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)
    #
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", write, result[1]))


if __name__ == "__main__":
    main()
