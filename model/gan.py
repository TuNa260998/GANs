import torch
import torch.nn as nn
import torch.nn.functional as F
from pytorch_lightning.core import LightningModule

class Generator(nn.Module):
    def __init__(self, latent_dim, img_shape):
        super().__init__()
        
        
    def forward(self, z):
        return 0
    
class Discriminator(nn.Module):
    def __init__(self, img_shape):
        super().__init__()
     
    def forward(self, img):
        return 0
    


class GAN(LightningModule):
    def __init__(self):
        super().__init__()
        self.save_hyperparameters()
        

    def forward(self, x):
        return self.generator(z)
    