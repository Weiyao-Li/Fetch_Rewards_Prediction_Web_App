import torch
import torch.nn as nn

class LSTMModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        self.linear = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        if len(out.shape) == 2:
            out = out.unsqueeze(1)
        out = self.linear(out[:, -1, :])
        return out


input_dim = 1
hidden_dim = 32
num_layers = 1

model = LSTMModel(input_dim, hidden_dim, num_layers)
# Load the trained model
model = LSTMModel(1, 32, 1)
# model refers to the one
# model path example:/Users/weiyaoli/Desktop/Fetch_Rewards_Prediction_Web_App/djangoProject/model
model.load_state_dict(torch.load("/Users/weiyaoli/Desktop/Fetch_Rewards_Prediction_Web_App/djangoProject/model"))
model.eval()
