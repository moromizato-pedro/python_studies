#!/usr/bin/env python3


def secure_archive(file_name: str, operation: int, content: str="") -> tuple[bool, str]:
    write = 0
    read = 1
    try:
        if operation == read:
            with open(file_name, "r") as f:
                content = f.read()
                return (True, content)
        elif operation == write:
            with open(file_name, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
    except OSError as err:
        return (False, str(err))



def main():
    write = 0
    read = 1
    print("=== Cyber Archives Security ===")
    #
    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", read))
    #
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("old_fragment.txt", read))
    #
    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", read)
    print(result)
    #
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", write, result[1]))


if __name__ == "__main__":
    main()
