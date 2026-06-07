import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
import random


MAX_AGE = 80.0
MAX_HEIGHT = 600.0
BATCH_SIZE = 32
LEARNING_RATE = 0.01
EPOCHS = 200

raw_data = []
for i in range(1000): 
    age = random.uniform(1, MAX_AGE)
    gender = random.choice([1, 2])
    nutrition = random.uniform(1, 10)
    height = (age * 5) + 80 + (nutrition * 2) + random.uniform(-2, 2)
    
    raw_data.append([age, gender, nutrition, height])

df = pd.DataFrame(raw_data, columns=['age', 'gender', 'nutrition', 'height'])


df['age'] /= MAX_AGE
df['gender'] /= 2.0
df['nutrition'] /= 10.0
df['height'] /= MAX_HEIGHT


train_df = df.sample(frac=0.8, random_state=42)
val_df = df.drop(train_df.index)

class HeightDataset(Dataset):
    def __init__(self, dataframe):
        self.x = torch.tensor(dataframe[['age', 'gender', 'nutrition']].values, dtype=torch.float32)
        self.y = torch.tensor(dataframe[['height']].values, dtype=torch.float32)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

train_loader = DataLoader(HeightDataset(train_df), batch_size=BATCH_SIZE, shuffle=True)
val_loader = DataLoader(HeightDataset(val_df), batch_size=BATCH_SIZE)


class HeightModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )

    def forward(self, x):
        return self.net(x)

model = HeightModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)


train_losses = []
val_losses = []

for epoch in range(EPOCHS):
    model.train()
    batch_losses = []
    
    for inputs, targets in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        batch_losses.append(loss.item())
    
   
    model.eval()
    val_loss = 0
    with torch.no_grad():
        for v_inputs, v_targets in val_loader:
            v_outputs = model(v_inputs)
            val_loss += criterion(v_outputs, v_targets).item()
    
    train_losses.append(sum(batch_losses)/len(batch_losses))
    val_losses.append(val_loss/len(val_loader))

    if epoch % 20 == 0:
        print(f"Epoch {epoch} | Train Loss: {train_losses[-1]:.6f} | Val Loss: {val_losses[-1]:.6f}")


plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Train Loss')
plt.plot(val_losses, label='Val Loss')
plt.title('Training Progress')
plt.xlabel('Epoch')
plt.ylabel('MSE Loss')
plt.legend()
plt.show()


print("\n--- Test Prediction ---")
age_in = float(input("Age: ")) / MAX_AGE
gen_in = float(input("Gender (1/2): ")) / 2.0
nut_in = float(input("Nutrition (1-10): ")) / 10.0

model.eval()
with torch.no_grad():
    sample = torch.tensor([[age_in, gen_in, nut_in]], dtype=torch.float32)
    pred = model(sample).item() * MAX_HEIGHT
    print(f"Predicted Height: {pred:.2f} cm")

 

