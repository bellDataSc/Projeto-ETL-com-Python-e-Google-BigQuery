# Brazilian Demographics & Economic Data Pipeline

**Modern ETL pipeline for Brazilian demographic and economic data analysis using IBGE APIs**

[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/brazilian-data-etl)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Data Source](https://img.shields.io/badge/Data-IBGE%20API-green.svg)](https://servicodados.ibge.gov.br/api/docs/)

## Project Overview

This project demonstrates a comprehensive ETL (Extract, Transform, Load) pipeline for Brazilian government data, featuring interactive visualizations, economic analysis, and modern data engineering practices. 

### Key Features

- **Multi-source Data Extraction**: Brazilian states, municipalities, and economic indicators
- **Advanced Data Transformation**: Cleaning, normalization, and feature engineering  
- **Interactive Visualizations**: Plotly-based charts, maps, and dashboards
- **Economic Analysis**: Clustering, ranking, and correlation analysis
- **Cloud-Ready**: Google Colab optimized with BigQuery integration support
- **International Standards**: English documentation and modern coding practices

##  Repository Structure

```
brazilian-data-etl/
├── notebooks/
│   ├── brazilian_demographics_etl.ipynb      # Main ETL pipeline
│   └── brazilian_economic_analysis.ipynb     # Economic analysis & clustering
├── README.md                                  # Project documentation
└── requirements.txt                          # Python dependencies
```

## Quick Start

### Option 1: Google Colab (Recommended)

1. Click the "Open in Colab" badge above
2. Run all cells in the notebook
3. Data will be automatically downloaded and processed
4. Interactive visualizations will be generated inline

### Option 2: Local Environment

```bash

git clone https://github.com/bellDataSc/Projeto-ETL-com-Python-e-Google-BigQuery
cd 

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

## Data Sources

All data is sourced from official Brazilian government APIs:

- **IBGE API**: Brazilian Institute of Geography and Statistics
  - States and municipalities data
  - Population estimates
  - Geographic boundaries

- **SIDRA API**: IBGE's Automatic Recovery System
  - Economic indicators
  - Demographic statistics
  - Time series data

## Technologies Used

- **Python 3.8+**: Main programming language
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations
- **Requests**: API data extraction
- **Scikit-learn**: Machine learning and clustering
- **Google BigQuery** (optional): Cloud data warehouse

## Analysis Features

### 1. Demographic Analysis
- Population distribution by state and region
- Geographic data processing
- Name pattern analysis

### 2. Economic Analysis  
- GDP per capita analysis
- Human Development Index (HDI) correlations
- Economic clustering using K-means
- Comprehensive ranking system

### 3. Interactive Visualizations
- Population distribution maps
- Economic performance comparisons
- Correlation matrices
- 3D clustering plots

## Key Insights

The analysis reveals:
- **Regional Disparities**: Significant economic differences between Brazilian regions
- **Development Patterns**: Clear correlations between GDP, HDI, and economic diversity
- **Growth Opportunities**: Identification of high-potential development areas

## Why This Project?

- **Professional Portfolio**: Demonstrates modern data engineering skills
- **Real-World Data**: Uses authentic government datasets
- **International Appeal**: English documentation for global audience
- **Cloud-Native**: Ready for deployment and scaling
- **Best Practices**: Clean code, comprehensive documentation, reproducible analysis

## Educational Value

Perfect for learning:
- ETL pipeline development
- API data extraction
- Data visualization with Plotly
- Economic data analysis
- Machine learning clustering
- Google Colab development

## Contributing

Contributions are welcome! Areas for improvement:
- Additional data sources (economic sectors, environmental data)
- Advanced predictive models
- Geographic visualizations with maps
- Real-time data updates
- Performance optimizations

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links & Resources

- [IBGE Official Website](https://www.ibge.gov.br/en/)
- [IBGE API Documentation](https://servicodados.ibge.gov.br/api/docs/)
- [SIDRA Database](https://sidra.ibge.gov.br/)
- [Plotly Documentation](https://plotly.com/python/)

## Contact

Created by **Bel** - [isabel.gon.adm@gmail.com](mailto:isabel.gon.adm@gmail.com)

LinkedIn: [http://www.linkedin.com/in/belcruz](http://www.linkedin.com/in/belcruz)  
Portfolio: 

---

⭐ **If you found this project useful, please give it a star!** ⭐

*Made with ☕ by Isabel Cruz | in Google Colab | in Brazil | Data from IBGE*
