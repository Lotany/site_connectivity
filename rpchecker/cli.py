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
    return parser.parse_args()