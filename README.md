# ISIS Twitter Network Analysis

A network-based approach to analyzing and disrupting ISIS communication patterns on Twitter using social network analysis techniques. This research presents methodologies for identifying key influencers and communication patterns in terrorist networks, with the goal of developing effective disruption strategies.

## Abstract

This research analyzes ISIS Twitter networks to identify and disrupt communication patterns. Using techniques such as Social Network Cluster Analysis, Community Detection, and Temporal/Spatial Analysis, we've created networks with scaled nodes of users making pro-ISIS tweets. Our analysis has identified top active ISIS accounts, primary communication zones, and key discussion topics in pro-ISIS tweets.

## Features

- Construction of weighted directed graphs from Twitter data
- Community detection using Louvain modularity algorithm
- Identification of key network influencers (hubs and authorities)
- Analysis of temporal patterns in relation to real-world events
- Visualization of network structures and distributions
- Path length and clustering coefficient analysis
- Hub and authority score calculations

## Requirements

- Python 3.8+
- NetworkX
- Pandas
- Matplotlib
- Community Detection Library
- Gephi (for visualization)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/isis-twitter-network-analysis.git
cd isis-twitter-network-analysis
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Basic network analysis:

```python
from src.network_analysis import TwitterNetworkAnalyzer

analyzer = TwitterNetworkAnalyzer('data/tweets.csv')
G, mentions_df = analyzer.create_network()
community_info = analyzer.analyze_communities()
```

2. Visualization:

```python
from src.visualization import NetworkVisualizer

visualizer = NetworkVisualizer()
visualizer.plot_degree_distribution(G)
visualizer.plot_path_length_distribution(G)
```

## Research Paper

The complete research paper can be found in `docs/isis-twitter-network-analysis-report.pdf`. Key findings include:

- Identification of 30 distinct communities with modularity Q of 0.5479
- Analysis of key network influencers and their roles
- Correlation between network activity and real-world events
- Recommendations for network disruption strategies

## Key Findings

1. Network Structure:

   - Multiple interconnected communities
   - Scale-free network properties
   - Short average path lengths

2. Influential Nodes:

   - Identified key authorities and information hubs
   - Mapped information flow patterns
   - Located critical communication bridges

3. Temporal Patterns:
   - Correlation with real-world events
   - Activity spikes during significant incidents
   - Communication pattern changes over time

## Authors

- Elion Sufaj
- Kanika Parikh
- Zeel Patel
- Omar Saeed

_York University, Toronto, Ontario, Canada_

## Citation

If you use this code or research in your work, please cite:

```bibtex
@article{sufaj2022network,
  title={A Network Based Approach to Disrupting ISIS' Lines of Communication via Twitter Analysis},
  author={Sufaj, Elion and Parikh, Kanika and Patel, Zeel and Saeed, Omar},
  institution={York University},
  year={2022}
}
```

## Data Access

Dataset can be found on Kaggle or simply take it from this repo.

## Contributing

We welcome contributions to improve the analysis methods and code. Please submit pull requests or open issues for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimers

1. This research is conducted for academic purposes to understand and counter terrorist communication networks.
2. The data used in this research was collected after the events and used solely for analysis purposes.
3. This project does not promote or endorse any extremist ideologies or activities.

## Contact

For research-related queries:

- Elion Sufaj - esufaj@yahoo.com
