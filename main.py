from difflib import SequenceMatcher

with open("1.txt", encoding="utf-8") as file1, open("2.txt", encoding="utf-8") as file2:
    fil1data = file1.read()
    fil2data = file2.read()
    similarity = SequenceMatcher(None, fil1data, fil2data).ratio()
    print(similarity * 100)
