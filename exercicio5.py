import requests
from bs4 import BeautifulSoup
from threading import Thread

url = "https://www.geeksforgeeks.org/touch-command-in-linux-with-examples/"

search_word = "linux"
occurrences = 0

def search_webpage(fullstring, cur_thread):
    global occurrences
    global search_word

    print("[Thread %d] Total occurrences until now: %d" %(cur_thread, occurrences))

    cur_occurrences = fullstring.count(search_word.lower())

    print("[Thread %d] Total occurrences in this thread: %d" %(cur_thread, cur_occurrences))

    occurrences += cur_occurrences

    print("[Thread %d] Total occurrences after checking: %d" %(cur_thread, occurrences))


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
body_text = soup.body.text.lower()

length = len(body_text)
part1_end = length // 3
part2_end = 2 * length // 3

part1 = body_text[:part1_end]
part2 = " " + body_text[part1_end:part2_end]
part3 = " " + body_text[part2_end:]

threads = [
    Thread(target=search_webpage, args=(part1, 1)), 
    Thread(target=search_webpage, args=(part2, 2)),
    Thread(target=search_webpage, args=(part3, 3))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"The word '{search_word}' appears {occurrences} times on the webpage.")
