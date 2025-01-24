import argparse
import re
import traceback

from utils.password_gen import PasswordGenerator
from utils.port_scanner import PortScanner


def main() -> None:
    """Main function for the CLI selection"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--pass_gen", action="store_true", help="Password Generator")
    parser.add_argument("--scanner", action="store_true", help="Port Scanner")
    args = parser.parse_args()

    try:
        if args.pass_gen:
            password_length = int(input("Please state the password length: "))

            while password_length < 12 or password_length > 250:
                password_length = int(input("Please try again (min: 12, max: 250): "))

            gen_pass = PasswordGenerator().gen_pass(password_length)
            print(f"Generated Password:\n{gen_pass}")

        elif args.scanner:
            host_to_scan = input("Please state the hostname: ")
            if re.search(r"https|:|/|www\.", host_to_scan):
                host_to_scan = re.sub(r"https|:|/|www\.", "", host_to_scan)

            PortScanner().scan(host_to_scan)

    except KeyboardInterrupt:
        print("\n\nExiting program...")
        exit(0)
    except Exception:
        traceback.print_exc()
        exit(1)


if __name__ == "__main__":
    main()
