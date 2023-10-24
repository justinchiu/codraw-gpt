from codraw.complete import complete_code
from pathlib import Path
import re

outfile = Path("outputs/bicycle.py")

HEADER = """from colour import Color
from chalk import *

papaya = Color("#ff9700")
blue = Color("#005FDB")
"""

MODEL = "gpt-4"

response, prompt = complete_code(MODEL, "Please draw a bicycle in python and chalk for me.")
content = response.choices[0].message.content

regexpmatch = re.compile("```python.*```", flags=re.DOTALL).search(content)
code = content[slice(*regexpmatch.span())].replace("```python","").replace("```","").strip()

with outfile.open("w") as f:
    f.write(HEADER)
    f.write(code)



