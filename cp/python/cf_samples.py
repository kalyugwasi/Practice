import requests
from bs4 import BeautifulSoup

def download_samples(contest_id, problem_letter):
    url = f"https://codeforces.com/contest/{contest_id}/problem/{problem_letter}"
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    inputs = soup.select(".sample-test .input pre")
    outputs = soup.select(".sample-test .output pre")

    for i, (inp, out) in enumerate(zip(inputs, outputs), 1):
        with open(f"input{i}.txt", "w") as f:
            f.write(inp.get_text("\n").strip() + "\n")

        with open(f"output{i}.txt", "w") as f:
            f.write(out.get_text("\n").strip() + "\n")

    print(f"Downloaded {len(inputs)} sample test(s).")


if __name__ == "__main__":
    contest_id = input("Contest ID: ").strip()
    problem_letter = input("Problem letter: ").strip().upper()

    download_samples(contest_id, problem_letter)
