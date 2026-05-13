import torch
import torch.nn as nn

class RecommenderNet(nn.Module):

    def __init__(self, num_users, num_movies, embedding_size=50):

        super(RecommenderNet, self).__init__()

        # Embeddings
        self.user_embedding = nn.Embedding(num_users, embedding_size)
        self.movie_embedding = nn.Embedding(num_movies, embedding_size)

        # Fully connected layers
        self.fc1 = nn.Linear(embedding_size * 2 + 1, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)

        self.relu = nn.ReLU()

    def forward(self, user, movie, context):

        user_embed = self.user_embedding(user)
        movie_embed = self.movie_embedding(movie)

        # Concatenate all features
        x = torch.cat([user_embed, movie_embed, context], dim=1)

        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))

        output = self.fc3(x)

        return output