import os
import shutil
import time
from bs4 import BeautifulSoup
import requests

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
    
    url = f"https://codeforces.com/problemset/problem/{contest}/{problem}"
    
    # Try Method 1: Simple requests with headers
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(response.text)
        else:
            raise Exception(f"Status code: {response.status_code}")
            
    except Exception as e:
                
        # Try Method 2: Selenium
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
            
            
        except Exception as e2:
            print(f"❌ Both methods failed: {e2}")
            print("\n💡 Please try:")
            print("   1. Check your internet connection")
            print("   2. Make sure Chrome is installed")
            print("   3. Try running: pip install --upgrade selenium webdriver-manager")
            exit(1)
else:
    print("✅ problem.html already exists")

# ---------- Parse samples from HTML ----------
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()
    soup = BeautifulSoup(html_content, "html.parser")

# Check if it's a Cloudflare block page
if "Cloudflare" in html_content and "blocked" in html_content:
    print("❌ Downloaded page is a Cloudflare block page")
    print("💡 Deleting and you can try again...")
    os.remove(html_path)
    exit(1)

inputs = soup.select("div.sample-test div.input pre")
outputs = soup.select("div.sample-test div.output pre")

if not inputs or not outputs:
    print("❌ No sample tests found in HTML")
    print("💡 The page might not have loaded correctly.")
    print(f"💡 Check the HTML file at: {html_path}")
    exit(1)

# ---------- Save test cases ----------
for i, (inp, out) in enumerate(zip(inputs, outputs), 1):
    in_file = os.path.join(problem_folder, f"input{i}.txt")
    exp_file = os.path.join(problem_folder, f"expected{i}.txt")

    with open(in_file, "w", encoding="utf-8") as f:
        f.write(inp.get_text("\n").strip() + "\n")

    with open(exp_file, "w", encoding="utf-8") as f:
        f.write(out.get_text("\n").strip() + "\n")

    print(f"✅ Test case {i} saved")

# ---------- Copy first input to judge/input.txt ----------
first_input = os.path.join(problem_folder, f"input1.txt")
if os.path.exists(first_input):
    shutil.copyfile(first_input, INPUT_TXT)
else:
    print("❌ Could not copy input1.txt")

print(f"\n📁 Test cases saved in: {problem_folder}")

if os.path.exists(html_path):
    os.remove(html_path)