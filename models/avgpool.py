import torch
from torch.nn import Module, Conv2d, Parameter, Softmax
import torch.nn as nn
from torch.nn import functional as F


class model(nn.Module):
    """
    Avgpool Module 
    """

    def __init__(self, input_size=4096, num_classes=31):
        super().__init__()

        self.num_classes = num_classes

        self.avgpool_1d = nn.AdaptiveAvgPool1d(output_size=1)

        self.classifier = nn.Sequential(nn.Linear(input_size, num_classes), nn.Dropout(p=0.3))

    def forward(self, x):
        """
            inputs :
                x : input feature maps( B X C X L)
            returns :
                out : B X C
        """

        avg_out = self.avgpool_1d(x.transpose(2, 1))

        current_prob = self.classifier(avg_out.squeeze(2))

        return current_prob


if __name__ == "__main__":
    x = torch.randn(16, 4, 4096)
    avgpool_layer = model(input_size=4096)
    out = avgpool_layer(x)
