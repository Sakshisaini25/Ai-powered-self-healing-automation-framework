from difflib import get_close_matches

class SelfHealing:
    def __init__(self, elements):
        self.elements = elements

    def heal(self, locator):
        matches = get_close_matches(locator, self.elements, n=1, cutoff=0.5)
        if matches:
            print(f"[INFO] Healed locator: {matches[0]}")
            return matches[0]
        print("[ERROR] No match found")
        return None
