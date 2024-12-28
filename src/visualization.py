"""
Visualization module for ISIS Twitter network analysis.
Provides plotting functions for network metrics and distributions.
"""

from typing import List
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class NetworkVisualizer:
    def __init__(self, style: str = 'seaborn'):
        """Initialize visualizer with matplotlib style."""
        plt.style.use(style)

    def plot_degree_distribution(self, G: nx.Graph, log_scale: bool = True) -> None:
        """Plot degree distribution of the network."""
        degrees = [d for n, d in G.degree()]
        
        plt.figure(figsize=(10, 6))
        if log_scale:
            plt.loglog(sorted(degrees, reverse=True), 'b-', label='Degree')
        else:
            plt.hist(degrees, bins=50, alpha=0.75)
            
        plt.xlabel('Degree')
        plt.ylabel('Frequency')
        plt.title('Network Degree Distribution')
        plt.grid(True, alpha=0.3)
        plt.show()

    def plot_path_length_distribution(self, G: nx.Graph) -> None:
        """Plot distribution of shortest path lengths."""
        path_lengths = dict(nx.all_pairs_shortest_path_length(G))
        
        # Calculate frequency of each path length
        length_freq = {}
        for source in path_lengths:
            for target in path_lengths[source]:
                length = path_lengths[source][target]
                length_freq[length] = length_freq.get(length, 0) + 1

        plt.figure(figsize=(10, 6))
        plt.bar(length_freq.keys(), length_freq.values(), alpha=0.75)
        plt.xlabel('Path Length')
        plt.ylabel('Frequency')
        plt.title('Shortest Path Length Distribution')
        plt.grid(True, alpha=0.3)
        plt.show()

    def plot_community_sizes(self, communities: List[List]) -> None:
        """Plot distribution of community sizes."""
        sizes = [len(com) for com in communities]
        
        plt.figure(figsize=(10, 6))
        plt.hist(sizes, bins=20, alpha=0.75)
        plt.xlabel('Community Size')
        plt.ylabel('Frequency')
        plt.title('Community Size Distribution')
        plt.grid(True, alpha=0.3)
        plt.show()

    def plot_hub_authority_distribution(self, G: nx.DiGraph) -> None:
        """Plot distribution of hub and authority scores."""
        hub_scores = nx.hub_score(G)
        authority_scores = nx.authority_score(G)
        
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        plt.hist(list(hub_scores.values()), bins=30, alpha=0.75)
        plt.xlabel('Hub Score')
        plt.ylabel('Frequency')
        plt.title('Hub Score Distribution')
        
        plt.subplot(1, 2, 2)
        plt.hist(list(authority_scores.values()), bins=30, alpha=0.75)
        plt.xlabel('Authority Score')
        plt.ylabel('Frequency')
        plt.title('Authority Score Distribution')
        
        plt.tight_layout()
        plt.show()