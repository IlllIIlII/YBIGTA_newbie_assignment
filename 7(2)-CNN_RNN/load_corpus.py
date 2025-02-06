def load_corpus() -> list[str]:
    corpus: list[str] = []

    with open("poem_dataset.txt", "r") as f:
        for line in f:
            corpus.append(line.strip())  
    return corpus