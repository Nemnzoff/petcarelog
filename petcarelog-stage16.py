# === Stage 16: Add argparse support for the most common commands ===
# Project: PetCareLog
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="PetCareLog - Household Pet Care Tracker")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Feed command
    feed_parser = subparsers.add_parser("feed", help="Log a feeding")
    feed_parser.add_argument("--pet", required=True)
    feed_parser.add_argument("--food", required=True)
    feed_parser.add_argument("--amount", default="1 cup")

    # Vet command
    vet_parser = subparsers.add_parser("vet", help="Log a vet visit")
    vet_parser.add_argument("--pet", required=True)
    vet_parser.add_argument("--date", required=True)
    vet_parser.add_argument("--notes", default="")

    # Meds command
    meds_parser = subparsers.add_parser("meds", help="Log medication")
    meds_parser.add_argument("--pet", required=True)
    meds_parser.add_argument("--med", required=True)
    meds_parser.add_argument("--dose", default="1 tablet")
    meds_parser.add_argument("--frequency", default="daily")

    # Weight command
    weight_parser = subparsers.add_parser("weight", help="Log weight")
    weight_parser.add_argument("--pet", required=True)
    weight_parser.add_argument("--lbs", type=float, required=True)
    weight_parser.add_argument("--date", default="today")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)
    print(f"{args.command} recorded for {args.pet}" if hasattr(args, 'pet') else "")

if __name__ == "__main__":
    main()
