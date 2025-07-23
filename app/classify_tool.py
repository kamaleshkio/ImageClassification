import torch
import torch.nn as nn
from torchvision.models import resnet18
from torchvision import transforms
from PIL import Image
import sys

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model
model = resnet18(weights=None)
model.fc = nn.Linear(model.fc.in_features, 5)
model.load_state_dict(torch.load("model_weights/oil_stage_classifier.pth", map_location=device))
model.to(device)
model.eval()

# Class labels
classes = [f"Stage {i+1}" for i in range(5)]

# Image transform (same as training)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

# Prediction function
def classify_image(image_path: str) -> str:
    try:
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        return f"Error loading image: {e}"

    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(input_tensor)
        _, predicted = torch.max(outputs, 1)
        return f"Predicted Oil Stage: {classes[predicted.item()]}"

# Optional CLI usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python classify.py <image_path>")
    else:
        print(classify_image(sys.argv[1]))
