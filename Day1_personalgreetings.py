# personalised_greeting.py
# Run with:  python personalised_greeting.py

# ---- tiny look‑up tables ----
COLOUR_TRAITS = {
    "red":    "passion and bold energy",
    "blue":   "calm confidence and depth",
    "green":  "growth, balance, and renewal",
    "yellow": "sunny optimism and creativity",
    "purple": "imagination and quiet strength",
    "orange": "warmth and enthusiastic spirit",
    "pink":   "kindness and heartfelt compassion",
    "black":  "elegance, mystery, and focus",
    "white":  "clarity and fresh beginnings"
}

NAME_MEANINGS = {
    "alice":  "noble and truthful",
    "arjun":  "bright, shining, and courageous",
    "carlin": "little champion with a big heart",   # example
    "david":  "beloved and steadfast",
    "john":   "gracious and full of mercy",
    "maria":  "wished‑for child, deeply loved",
    "sophia": "wisdom and insight"
}

# ---- gather details ----
name  = input("What's your name? ").strip()
age   = input("How old are you? ").strip()
colour = input("What's your favourite colour? ").strip().lower()

# ---- figure out meanings ----
meaning = NAME_MEANINGS.get(name.lower(),
            "unique qualities the world is still discovering")
trait   = COLOUR_TRAITS.get(colour,
            "a one‑of‑a‑kind hue that matches your individuality")

# ---- craft the 4–5‑line message ----
message = (
    f"\nHi {name}! At {age} years young, you carry the meaning of “{meaning}.”\n"
    f"Your love for {colour.title()} speaks of {trait}.\n"
    f"Together, your name and colour hint at a personality that stands out.\n"
    f"Keep shining in your own brilliant way — the world needs your vibe!\n"
)

print(message)
