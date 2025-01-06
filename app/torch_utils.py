import io
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image

# load model 

input_size = 784 # 28x28
hidden_size = 500 
num_classes = 10
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.input_size = input_size
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size, num_classes)  
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        # no activation and no softmax at the end
        return out
model = NeuralNet(input_size, hidden_size, num_classes)
PATH = "app\\mnist_ff.pth"
model.load_state_dict(torch.load(PATH)) #model is trained on cpu
model.eval()

# image -> tensor
def transform_image(image_bytes):
    transform = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0) # add a 1 in zero position dimension (simulating
    #a batch of 1 as our model expects first dim for batch size)

# predict
def get_prediction(image_tensor):
        images = image_tensor.reshape(-1, 28*28)
        outputs = model(images)
        # max returns (value ,index)
        _, predicted = torch.max(outputs.data, 1)
        return predicted
