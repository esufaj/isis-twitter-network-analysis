"""
Network analysis module for ISIS Twitter communication patterns.
Handles network construction and analysis of Twitter interaction data.
"""

from typing import Dict, List, Tuple
import pandas as pd
import networkx as nx
import community.community_louvain as community_louvain

class TwitterNetworkAnalyzer:
    def __init__(self, data_path: str):
        """Initialize the network analyzer with path to tweet data."""
        self.data_path = data_path
        self.graph = None
        self.undirected_graph = None
        self.mentions_df = None

    def create_network(self) -> Tuple[nx.DiGraph, pd.DataFrame]:
        """
        Create network from Twitter data.
        
        Returns:
            Tuple containing directed graph and mentions DataFrame
        """
        try:
            # Read and process data
            df = pd.read_csv(self.data_path)
            mentions = self._extract_mentions(df)
            self.mentions_df = self._create_mentions_dataframe(mentions)
            
            # Create directed and undirected graphs
            self.graph = nx.from_pandas_edgelist(
                self.mentions_df, 
                'User', 
                'Mentions',
                create_using=nx.DiGraph(), 
                edge_attr='Weight'
            )
            self.undirected_graph = nx.from_pandas_edgelist(
                self.mentions_df, 
                'User', 
                'Mentions',
                create_using=nx.Graph(), 
                edge_attr='Weight'
            )
            
            return self.graph, self.mentions_df
            
        except Exception as e:
            print(f"Error creating network: {e}")
            raise

    def analyze_communities(self) -> Dict:
        """
        Perform community detection using Louvain algorithm.
        
        Returns:
            Dict containing modularity and community information
        """
        if self.undirected_graph is None:
            raise ValueError("Network not created. Call create_network() first.")
            
        partition = community_louvain.best_partition(self.undirected_graph)
        modularity = community_louvain.modularity(partition, self.undirected_graph, weight='Weight')
        
        communities = []
        for com in set(partition.values()):
            nodes = [node for node, com_id in partition.items() if com_id == com]
            communities.append(nodes)
            
        return {
            'modularity': modularity,
            'num_communities': len(communities),
            'communities': communities
        }

    def identify_key_actors(self) -> Dict:
        """
        Identify network hubs and authorities.
        
        Returns:
            Dict containing top hubs and authorities
        """
        if self.mentions_df is None:
            raise ValueError("Network not created. Call create_network() first.")
            
        # Calculate in-degree (authorities)
        authorities = self.mentions_df.groupby(
            by=['Mentions'], 
            as_index=False
        )['Weight'].sum().nlargest(10, 'Weight')
        
        # Calculate out-degree (hubs)
        hubs = self.mentions_df.groupby(
            by=['User'], 
            as_index=False
        )['Weight'].sum().nlargest(10, 'Weight')
        
        return {
            'authorities': authorities,
            'hubs': hubs
        }

    def _extract_mentions(self, df: pd.DataFrame) -> pd.DataFrame:
        """Extract mentions from tweets."""
        mentions_mask = df['tweets'].str.contains('@', na=False)
        return df[mentions_mask].reset_index(drop=True)

    def _create_mentions_dataframe(self, mentions: pd.DataFrame) -> pd.DataFrame:
        """Create mentions DataFrame with weights."""
        mentions['Mentioned-User'] = mentions['tweets'].str.findall(r'@([A-Za-z0-9_]+)')
        
        # Create edge list with weights
        edge_list = []
        for _, row in mentions.iterrows():
            for mentioned_user in row['Mentioned-User']:
                edge_list.append({
                    'User': row['username'],
                    'Mentions': mentioned_user,
                    'Weight': 1
                })
        
        mentions_df = pd.DataFrame(edge_list)
        return mentions_df.groupby(
            by=['User', 'Mentions'], 
            as_index=False
        )['Weight'].sum()