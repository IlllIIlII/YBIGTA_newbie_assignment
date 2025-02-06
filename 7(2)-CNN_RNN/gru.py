import torch
from torch import nn, Tensor


class GRUCell(nn.Module):
    def __init__(self, input_size: int, hidden_size: int) -> None:
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size

        self.reset_gate = nn.Linear(input_size + hidden_size, hidden_size)
        self.update_gate = nn.Linear(input_size + hidden_size, hidden_size)
        self.new_state = nn.Linear(input_size + hidden_size, hidden_size)

    def forward(self, x: Tensor, h: Tensor) -> Tensor:
        combined = torch.cat((x, h), dim=1)

        r = torch.sigmoid(self.reset_gate(combined))
        z = torch.sigmoid(self.update_gate(combined))
        n = torch.tanh(self.new_state(torch.cat((x, r * h), dim=1))) 

        h_next = (1 - z) * n + z * h  
        return h_next


class GRU(nn.Module):
    def __init__(self, input_size: int, hidden_size: int) -> None:
        super().__init__()
        self.hidden_size = hidden_size
        self.cell = GRUCell(input_size, hidden_size)

    def forward(self, inputs: Tensor) -> Tensor:
        h = torch.zeros(inputs.size(0), self.hidden_size).to(inputs.device)
        # 구현하세요!
        for t in range(inputs.size(1)):  
            h = self.cell(inputs[:, t, :], h)
        return h