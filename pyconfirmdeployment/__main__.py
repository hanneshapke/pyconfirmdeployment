import sys
import argparse
import confirm


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description=(
            'Checks webservers after a deployment and emails '
            'the given email addresses a screenshot')
        )
    parser.add_argument(
        '-u', '--url', help='URL to check',
        required=True)
    parser.add_argument(
        '-t', '--to', help='Receiving emails of the screenshot',
        required=True)
    parser.add_argument(
        '-f', '--fromemail', help='From email address',
        required=True)

    args = parser.parse_args()
    sys.exit(confirm.get_confirmation(
        args.url, to_emails=[args.to, ], from_email=args.fromemail,)
    )

if __name__ == "__main__":
    main()
