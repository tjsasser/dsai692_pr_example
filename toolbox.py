"""Team Toolbox - a tiny CLI that runs small text utilities.

Every teammate adds ONE tool:
  1. create tools/<your_tool>.py
  2. import it in the IMPORT BLOCK below
  3. register it in the TOOL REGISTRY below

Steps 2 and 3 touch lines that your teammates also touch.
That is on purpose - this is where you will practice resolving conflicts.
"""

import sys

# --- IMPORT BLOCK --------------------------------------------------
# Add your import at the END of this block, on the line above the dashes.
from tools.shout import shout
# -------------------------------------------------------------------


# --- TOOL REGISTRY -------------------------------------------------
# Add your tool at the END of this dict, on the line above the closing brace.
TOOLS = {
    "shout": shout,
}
# -------------------------------------------------------------------


def main():
    if len(sys.argv) < 3:
        print("Team Toolbox")
        print("usage: python toolbox.py <tool> <text>")
        print("tools:", ", ".join(sorted(TOOLS)))
        return
    tool, text = sys.argv[1], " ".join(sys.argv[2:])
    if tool not in TOOLS:
        print(f"unknown tool: {tool}")
        print("tools:", ", ".join(sorted(TOOLS)))
        return
    print(TOOLS[tool](text))


if __name__ == "__main__":
    main()
