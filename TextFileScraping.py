import bs4
import requests
import io

print ("program started")
data = open('saksham.txt').readlines()

savefile = io.open('CGS.txt', 'a', encoding="utf-8")
url = "https://www.cgscoaching.com/blog/social-studies-pedagogy-quiz-cgs-coaching/"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
webdata = soup.find_all('div', {'class': 'col-md-8'})

for para in webdata:
    savefile.write(para.text)

for n, line in enumerate(data):
    if "Pradyut" in line:
            data[n] = "\n......pradyut encountered......"

    if line.startswith("Q") or line[0].isdigit():
        data[n] = "\n" + line.rstrip()

    if line.startswith("(a)"):
        data[n] = "\n" + line.rstrip()

    if line.startswith("(b)"):
        data[n] = "\n" + line.rstrip()
    if line.startswith("(c)"):
        data[n] = "\n" + line.rstrip()
    if line.startswith("(d)"):
        data[n] = "\n" + line.rstrip()

print " ".join(data)

savefile.close()
print ("Program ends")
