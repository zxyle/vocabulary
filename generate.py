import string
from datetime import datetime

with open("./words.txt") as f1, open("./README.md", "w") as f2:
    lines = f1.readlines()
    non_repeating_words = {line.strip() for line in lines}

    # sorted
    words = list(non_repeating_words)
    words.sort()
    print(words)

    # write file
    f2.write("# Computer Science Vocabulary\n")
    update_time = datetime.now().strftime("%Y-%m-%d %X")
    f2.write(f"*update time: {update_time}*\n")
    for alp in string.ascii_uppercase:
        print(len(words))
        headline = f"\n## {alp}\n"
        f2.write(headline)

        for word in words:
            if str(word).startswith(alp.lower()):
                f2.write(f"- {word}\n")
                words = words[1:]
