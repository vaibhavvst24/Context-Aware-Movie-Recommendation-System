import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader

from preprocess import load_data
from model import RecommenderNet

# Load data
df, user_encoder, movie_encoder = load_data()

# Inputs
users = torch.tensor(df['user'].values, dtype=torch.long)
movies = torch.tensor(df['movie'].values, dtype=torch.long)

# Context feature
context = torch.tensor(
    df[['time_context']].values,
    dtype=torch.float32
)

ratings = torch.tensor(
    df['rating'].values,
    dtype=torch.float32
).view(-1, 1)

# Dataset
dataset = TensorDataset(users, movies, context, ratings)

loader = DataLoader(dataset, batch_size=64, shuffle=True)

# Model
num_users = df['user'].nunique()
num_movies = df['movie'].nunique()

model = RecommenderNet(num_users, num_movies)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training
epochs = 5

for epoch in range(epochs):

    total_loss = 0

    for user, movie, ctx, rating in loader:

        optimizer.zero_grad()

        predictions = model(user, movie, ctx)

        loss = criterion(predictions, rating)

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

# Save model
torch.save(model.state_dict(), "models/recommender.pth")

print("Model saved successfully!")