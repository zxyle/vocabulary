import string

with open("./words.txt") as f1, open("./README.md", "w") as f2:
    lines = f1.readlines()
    words = list({line.strip() for line in lines})
    words.sort()

    f2.write("# Computer Science Vocabulary\n")
    for alphabet in string.ascii_uppercase:
        f2.write(f"\n## {alphabet}\n")

        for word in words:
            if str(word).startswith(alphabet.lower()):
                f2.write(f"- {word}\n")
                words = words[1:]
            else:
                break
