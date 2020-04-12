import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.datasets as datasets

import matplotlib.pyplot as plt
import numpy as np

import torch.nn as nn
import torch.nn.functional as F

from tqdm import tqdm

from torch.optim.lr_scheduler import StepLR
import torch.optim as optim

from torch.optim.lr_scheduler import MultiStepLR
from torch.optim.lr_scheduler import ReduceLROnPlateau

import albumentations
from albumentations import (
    HorizontalFlip, IAAPerspective, Rotate, CLAHE, RandomRotate90, Crop, Normalize,
    Transpose, ShiftScaleRotate, Blur, OpticalDistortion, GridDistortion, HueSaturationValue,
    IAAAdditiveGaussianNoise, GaussNoise, MotionBlur, MedianBlur, IAAPiecewiseAffine,
    IAASharpen, IAAEmboss, RandomContrast, RandomBrightness, Flip, OneOf, Compose,
    ElasticTransform,ChannelShuffle, Cutout, CoarseDropout
)
from albumentations.pytorch import ToTensor
