import requests
from bs4 import BeautifulSoup
import subprocess
import os
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JUDGE_DIR = os.path.join(BASE_DIR, "..", "judge")

os.makedirs(JUDGE_DIR, exist_ok=True)

def normalize(s):
    return s.split()

contest = input("Contest ID: ").strip()
problem = input("Problem letter: ").strip().upper()

url = f"https://codeforces.com/contest/{contest}/problem/{problem}"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

inputs = soup.select(".sample-test .input pre")
outputs = soup.select(".sample-test .output pre")

all_ok = True

for i, (inp, out) in enumerate(zip(inputs, outputs), 1):
    in_file = os.path.join(JUDGE_DIR, f"input{i}.txt")
    exp_file = os.path.join(JUDGE_DIR, f"output{i}.txt")  # store expected output permanently

    # Save input and expected output
    with open(in_file, "w", encoding="utf-8") as f:
        f.write(inp.get_text("\n").strip() + "\n")
    with open(exp_file, "w", encoding="utf-8") as f:
        f.write(out.get_text("\n").strip() + "\n")

    # Copy inputN.txt → input.txt for test.py
    temp_input = os.path.join(JUDGE_DIR, "input.txt")
    shutil.copyfile(in_file, temp_input)

    # Run test.py
    subprocess.run(["python", "test.py"], cwd=BASE_DIR)

    # Read program output
    temp_output = os.path.join(JUDGE_DIR, "output.txt")
    with open(temp_output, "r", encoding="utf-8") as f:
        actual = f.read()

    with open(exp_file, "r", encoding="utf-8") as f:
        expected = f.read()

    if normalize(actual) == normalize(expected):
        print(f"✅ Sample {i}: OK")
    else:
        print(f"❌ Sample {i}: WA")
        print("Expected:")
        print(expected)
        print("Got:")
        print(actual)
        all_ok = False

print("\n" + ("🎉 ACCEPTED" if all_ok else "💥 WRONG ANSWER"))
