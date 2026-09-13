# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: PetCareLog
def dry_run(self, action: str) -> None:
        """Simulate a mutating operation without persisting state.
        Prints an informational message to stdout so the user sees
        what would happen if the command were executed for real."""
        print(f"[DRY RUN] {action} — no state change applied.")
        if self._log is not None:
            self._log.append(f"[DRY RUN] {action} — no state change applied.")
