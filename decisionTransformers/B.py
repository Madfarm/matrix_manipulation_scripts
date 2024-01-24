import torch
import torch.nn as nn

class DecisionTransformer(nn.Module):
    def __init__(self, state_dim, action_dim, max_seq_length, hidden_dim, n_heads, n_layers):
        super(DecisionTransformer, self).__init__()
        
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.max_seq_length = max_seq_length
        self.hidden_dim = hidden_dim
        
        # Embedding layers for states, actions, and timestep positions
        self.state_embedding = nn.Linear(state_dim, hidden_dim)
        self.action_embedding = nn.Linear(action_dim, hidden_dim)
        self.position_embedding = nn.Embedding(max_seq_length, hidden_dim)
        
        # Transformer encoder
        encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=n_heads)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        
        # Output head for action prediction
        self.action_head = nn.Linear(hidden_dim, action_dim)
        
    def forward(self, states, actions, timesteps):
        # Embed the states and actions
        state_embeds = self.state_embedding(states)
        action_embeds = self.action_embedding(actions)
        
        # Combine state and action embeddings
        input_embeds = state_embeds + action_embeds
        
        # Add positional encodings
        positions = torch.arange(timesteps.size(1), device=timesteps.device).unsqueeze(0).expand(timesteps.size(0), -1)
        position_embeds = self.position_embedding(positions)
        input_embeds += position_embeds
        
        # Pass the sequence through the transformer
        transformer_out = self.transformer_encoder(input_embeds)
        
        # Predict the next action
        action_preds = self.action_head(transformer_out)
        
        return action_preds

# Example usage
state_dim = 10
action_dim = 5
max_seq_length = 50
hidden_dim = 128
n_heads = 4
n_layers = 3

# Create a Decision Transformer instance
dt = DecisionTransformer(state_dim, action_dim, max_seq_length, hidden_dim, n_heads, n_layers)

# Example input tensors
batch_size = 2
sequence_length = 10

states = torch.randn(batch_size, sequence_length, state_dim)
actions = torch.randn(batch_size, sequence_length, action_dim)
timesteps = torch.arange(sequence_length).unsqueeze(0).expand(batch_size, -1)

# Forward pass through the Decision Transformer
action_preds = dt(states, actions, timesteps)

print(action_preds.shape)  # Expected shape: (batch_size, sequence_length, action_dim)