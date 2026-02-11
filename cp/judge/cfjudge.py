import os
import shutil
import time
from bs4 import BeautifulSoup
# ----------------------- PATHS -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JUDGE_DIR = BASE_DIR
INPUT_TXT = os.path.join(JUDGE_DIR, "input.txt")
# ----------------------------------------------------
contest = input("Contest ID: ").strip()
problem = input("Problem letter: ").strip().upper()
problem_folder = os.path.join(JUDGE_DIR, f"{contest}{problem}")
os.makedirs(problem_folder, exist_ok=True)
html_path = os.path.join(problem_folder, "problem.html")
# ---------- Download problem.html ----------
if not os.path.exists(html_path):
    print("🌐 Downloading problem HTML...")
    urls = [
        f"https://codeforces.com/problemset/problem/{contest}/{problem}",
        f"https://codeforces.com/contest/{contest}/problem"
    ]
    success = False
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        for url_idx, url in enumerate(urls, 1):
            if success:
                break
            print(f"Trying URL {url_idx}: {url}")
            try:
                driver = webdriver.Chrome(
                    service=Service(ChromeDriverManager().install()),
                    options=chrome_options
                )
                driver.get(url)
                time.sleep(4)
                page_source = driver.page_source
                driver.quit()
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(page_source)
                success = True
                print(f"✅ Successfully downloaded using URL {url_idx}")
                break
                
            except Exception as e:
                print(f"⚠️  URL {url_idx} failed: {e}")
                try:
                    driver.quit()
                except:
                    pass
        if not success:
            print("\n❌ All URLs failed")
            print("\n💡 Please try:")
            print("   1. Check your internet connection")
            print("   2. Verify the contest ID and problem letter are correct")
            exit(1)
    except ImportError as e:
        exit(1)
else:
    print("✅ problem.html already exists")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()
    soup = BeautifulSoup(html_content, "html.parser")
if "Cloudflare" in html_content and "blocked" in html_content:
    print("❌ Downloaded page is a Cloudflare block page")
    print("💡 Deleting and you can try again...")
    os.remove(html_path)
    exit(1)
inputs = soup.select("div.sample-test div.input pre")
outputs = soup.select("div.sample-test div.output pre")
if not inputs or not outputs:
    print("❌ No sample tests found in HTML")
    print(f"💡 Check the HTML file at: {html_path}")
    exit(1)
for i, (inp, out) in enumerate(zip(inputs, outputs), 1):
    in_file = os.path.join(problem_folder, f"input{i}.txt")
    exp_file = os.path.join(problem_folder, f"expected{i}.txt")
    with open(in_file, "w", encoding="utf-8") as f:
        f.write(inp.get_text("\n").strip() + "\n")
    with open(exp_file, "w", encoding="utf-8") as f:
        f.write(out.get_text("\n").strip() + "\n")
    print(f"✅ Test case {i} saved")
first_input = os.path.join(problem_folder, f"input1.txt")
if os.path.exists(first_input):
    shutil.copyfile(first_input, INPUT_TXT)
else:
    print("❌ Could not copy input1.txt")
print(f"📁 Test cases saved in: {problem_folder}")
if os.path.exists(html_path):
    os.remove(html_path)