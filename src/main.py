from src.network_analysis import TwitterNetworkAnalyzer
from src.visualization import NetworkVisualizer

def main():
    # Initialize analyzer and visualizer
    analyzer = TwitterNetworkAnalyzer('data/tweets.csv')
    visualizer = NetworkVisualizer()
    
    # Create and analyze network
    G, mentions_df = analyzer.create_network()
    
    # Analyze communities
    community_info = analyzer.analyze_communities()
    print(f"Number of communities: {community_info['num_communities']}")
    print(f"Modularity: {community_info['modularity']:.4f}")
    
    # Identify key actors
    key_actors = analyzer.identify_key_actors()
    print("\nTop Authorities:")
    print(key_actors['authorities'])
    print("\nTop Hubs:")
    print(key_actors['hubs'])
    
    # Create visualizations
    visualizer.plot_degree_distribution(G)
    visualizer.plot_path_length_distribution(G)
    visualizer.plot_community_sizes(community_info['communities'])
    visualizer.plot_hub_authority_distribution(G)

if __name__ == "__main__":
    main()