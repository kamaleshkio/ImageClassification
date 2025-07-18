import torch
from torch import nn, optim
from torchvision import datasets, transforms
from torchvision.models import resnet18, ResNet18_Weights
import os

data_dir = "dataset"
save_path = "model_weights/oil_stage_classifier.pth"
os.makedirs(os.path.dirname(save_path), exist_ok=True)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

dataset = datasets.ImageFolder(data_dir, transform=transform)
train_loader = torch.utils.data.DataLoader(dataset, batch_size=16, shuffle=True)

model = resnet18(weights=ResNet18_Weights.DEFAULT)
model.fc = nn.Linear(model.fc.in_features, 5)  # 5 oil stages

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

model.train()
for epoch in range(5):  # Increase epochs for better accuracy
    total_loss = 0
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1} | Loss: {total_loss/len(train_loader)}")

torch.save(model.state_dict(), save_path)
print(f"Model saved to {save_path}")
