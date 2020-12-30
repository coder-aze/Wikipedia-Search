import wikipedia
answer=wikipedia.summary("Wikipedia").split(".")
for line in answer:
    print(line)

    