# === Stage 53: Add command help text and usage examples ===
# Project: PetCareLog
HELP_TEXT = (
    "PetCareLog — Household Pet Care Log\n"
    "Usage:\n"
    "  python PetCareLog.py add feeding --pet <name> --time <HH:MM> --amount <g> --note <text>\n"
    "  python PetCareLog.py add vet --pet <name> --date YYYY-MM-DD --symptom <text>\n"
    "  python PetCareLog.py add medication --pet <name> --dose <mg> --frequency <times/day> --note <text>\n"
    "  python PetCareLog.py add weight --pet <name> --weight <kg> --date YYYY-MM-DD\n"
    "  python PetCareLog.py show feeding [--pet <name>]\n"
    "  python PetCareLog.py show vet [--pet <name>]\n"
    "  python PetCareLog.py show medication [--pet <name>]\n"
    "  python PetCareLog.py show weight [--pet <name>]\n"
    "  python PetCareLog.py list pets\n"
    "  python PetCareLog.py help\n"
    "  python PetCareLog.py --version\n"
)


def print_help():
    print(HELP_TEXT)


def show_usage():
    print(HELP_TEXT)


def show_examples():
    print("Examples:\n")
    print("  python PetCareLog.py add feeding --pet Biscuit --time 08:00 --amount 45 --note breakfast")
    print("  python PetCareLog.py add weight --pet Biscuit --weight 3.2 --date 2025-01-10")
    print("  python PetCareLog.py show weight --pet Biscuit")
    print("  python PetCareLog.py list pets")
