#cli.py
import argparse
def read_user_cli_args():
    """Handle the cli arguments and options"""
    parser =argparse.ArgumentParser(
        prog= "rpchecker", description="Check the availability of websites"
    )

    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more wbsite URLs",
    )

    parser.add_argument(
        "-f",
        "--input-file",
        metavar= "FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    return parser.parse_args()

def display_check_result(result,url,error=""):
    """Display the result of a connectivity check."""
    print(f'The status of "{url}" is:',end=" ")
    if result:
        print('"Online!" 1')
    else:
        print(f'"Offline?" 0 \n Error: "{error}"')