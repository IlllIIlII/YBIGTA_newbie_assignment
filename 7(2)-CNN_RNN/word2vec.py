import torch
from torch import nn, Tensor, LongTensor
from torch.optim import Adam

from transformers import PreTrainedTokenizer

from typing import Literal

# 구현하세요!


class Word2Vec(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        d_model: int,
        window_size: int,
        method: Literal["cbow", "skipgram"]
    ) -> None:
        super().__init__()
        self.embeddings = nn.Embedding(vocab_size, d_model)
        self.weight = nn.Linear(d_model, vocab_size, bias=False)
        self.window_size = window_size
        self.method = method
        # 구현하세요!
        self.method = method
        pass

    def embeddings_weight(self) -> Tensor:
        return self.embeddings.weight.detach()

    def fit(
        self,
        corpus: list[str],
        tokenizer: PreTrainedTokenizer,
        lr: float,
        num_epochs: int
    ) -> None:
        criterion = nn.CrossEntropyLoss()
        optimizer = Adam(self.parameters(), lr=lr)
        # 구현하세요!
        for epoch in range(num_epochs):
            total_loss = 0
            for sentence in corpus:
                tokens = tokenizer(sentence, return_tensors='pt').input_ids.squeeze(0)
                if self.method == "cbow":
                    loss = self._train_cbow(tokens)
                elif self.method == "skipgram":
                    loss = self._train_skipgram(tokens)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                total_loss += loss.item()
            print(f"Epoch {epoch+1}/{num_epochs}, Loss: {total_loss}")
        pass

    def _train_cbow(self, tokens: Tensor) -> Tensor:
        loss = 0
        # 구현하세요!
        for center_word_idx in range(self.window_size, len(tokens) - self.window_size):
            context = tokens[center_word_idx - self.window_size:center_word_idx].tolist() + \
                     tokens[center_word_idx + 1:center_word_idx + self.window_size + 1].tolist()
            target = tokens[center_word_idx]
            context_emb = self.embeddings(torch.tensor(context))
            context_avg = context_emb.mean(dim=0)
            output = self.weight(context_avg)
            loss += F.cross_entropy(output.unsqueeze(0), torch.tensor([target]))
        return loss

    def _train_skipgram(self, tokens: Tensor) -> Tensor:
        loss = 0
        # 구현하세요!
        for center_word_idx in range(self.window_size, len(tokens) - self.window_size):
            target = tokens[center_word_idx]
            context = tokens[center_word_idx - self.window_size:center_word_idx].tolist() + \
                     tokens[center_word_idx + 1:center_word_idx + self.window_size + 1].tolist()
            center_emb = self.embeddings(target)
            output = self.weight(center_emb)
            loss += F.cross_entropy(output.unsqueeze(0), torch.tensor(context))
        return loss

    # 구현하세요!
    pass