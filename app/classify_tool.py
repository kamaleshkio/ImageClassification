
from torchvision.models import resnet18
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

model = resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 5)
model.load_state_dict(torch.load("model_weights/oil_stage_classifier.pth"))
model.eval()

# Class labels
classes = [f"Stage {i+1}" for i in range(5)]

# Prediction function
def classify_image(image_path: str) -> str:
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image = Image.open(image_path).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted = torch.max(outputs, 1)
        return f"Predicted Oil Stage: {classes[predicted.item()]}"
