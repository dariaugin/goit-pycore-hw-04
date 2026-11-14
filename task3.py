import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def print_tree(path, indent=""):
    """Recursively print the directory structure with colors."""
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{indent}{Fore.BLUE} {item.name}")
            print_tree(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN} {item.name}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Please provide a directory path!")
        return

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"{Fore.RED}!Path does not exist: {path}")
    elif not path.is_dir():
        print(f"{Fore.RED}!Not a directory: {path}")
    else:
        print(f"{Fore.BLUE}📦 {path.name}")
        print_tree(path)


if __name__ == "__main__":
    main()