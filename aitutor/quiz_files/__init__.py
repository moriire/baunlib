stx = "yes"
from django.conf import settings
import pandas as pd
import json
base = settings.BASE_DIR
f = base / "aitutor/quiz_files/q_robotics.csv"

def read_file(f=f):
    res = []
    csv = pd.read_csv(f)
    #jsond = csv[csv.a=="a"].to_json(orient="records")
    jsond = csv.to_json(orient="records")
    return json.loads(jsond)

__all__ = ("read_file", "stx")