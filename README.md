# RAG-Based Anime Recommendation Engine


![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1+-green.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Database-orange.svg)
![Groq](https://img.shields.io/badge/Groq-Llama3-purple.svg)
![Docker](https://img.shields.io/badge/Docker-Container-blue.svg)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326ce5.svg)

## Overview

The **RAG-Based Anime Recommendation Engine** is a sophisticated recommendation system that moves beyond simple keyword matching. By leveraging **Vector Search** (ChromaDB) and **Large Language Models** (Groq/Llama 3), it understands the *context* and *nuance* of your requests. 

Whether you want "a dark psychological thriller like Death Note" or "a lighthearted rom-com with a sci-fi twist," this engine retrieves relevant anime from a curated dataset and provides personalized, naturally phrased recommendations.



## Architecture

The system operates in two distinct phases: **Data Ingestion** (Offline) and **Inference** (Online).

```
Phase 1: Ingestion
    RawCSV[("Raw Data (CSV)")] --> DataLoader["Data Loader"]
    DataLoader -->|Processed Text| VectorBuilder["Vector Store Builder"]
    VectorBuilder -->|all-MiniLM-L6-v2| ChromaDB[("Chroma Vector DB")]

Phase 2: Inference
    User((User)) -->|Query| StreamlitApp["Streamlit UI"]
    StreamlitApp --> Pipeline["Recommendation Pipeline"]
    Pipeline -->|MMR Search (k=10)| ChromaDB
    ChromaDB -->|Retrieved Context| Pipeline
    Pipeline -->|Prompt + Context| GroqLLM["Groq API (Llama 3.1)"]
    GroqLLM -->|Response| StreamlitApp
```

---

## Getting Started

### Prerequisites

-   **Python 3.11+**
-   **Groq API Key**: You need an API key from [Groq Cloud](https://console.groq.com/).
-   **Huggingface API Key**: You need an API key from [Huggingface](https://huggingface.co/).

### Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/RAG-Based-Anime-Recommendation-Engine.git
    cd RAG-Based-Anime-Recommendation-Engine
    ```

2.  **Install Dependencies with `uv`**:
    This project uses [uv](https://github.com/astral-sh/uv) for fast package management.
    ```bash
    # Install uv if you haven't already
    pip install uv

    # Sync dependencies (creates .venv and installs packages from uv.lock)
    uv sync
    ```

3.  **Configuration**:
    Create a `.env` file in the root directory:
    ```bash
    touch .env
    ```
    Add your API keys:
    ```env
    # Required for LLM inference
    GROQ_API_KEY=gsk_your_api_key_here

    # Required for downloading models 
    HF_TOKEN=hf_your_huggingface_token_here
    ```

---

## Usage

### 1. Build the Vector Database (Ingestion)

Before running the app, you must process the raw data and build the vector index. This step reads the CSV data, creates embeddings, and saves them to the `./chroma_db` directory.

```bash
# Using uv to run in the virtual environment
uv run python pipeline/build_pipeline.py
```
*Wait for the process to complete. You should see logs indicating successful vector store creation.*

### 2. Run the Application

Launch the Streamlit interface:

```bash
uv run streamlit run app/app.py
```

The app will start at `http://localhost:8501`.



## Project Structure

```text
├── .dockerignore         # Docker build exclusion list
├── .env                  # Environment variables (API keys)
├── .github/              # GitHub Actions definitions
├── .gitignore            # Git exclusion list
├── .python-version       # Python version pin
├── .venv/                # Virtual environment directory
├── Dockerfile            # Container definition
├── LICENSE               # MIT License
├── README.md             # This file
├── anime-k8s.yaml        # Kubernetes deployment manifest
├── app/                  # Streamlit frontend application
│   └── app.py            # Main UI entry point
├── chroma_db/            # Persisted Vector Database
├── config/               # Configuration settings
│   ├── config.py         # Environment variable loader
│   └── __init__.py       # Package marker
├── data/                 # Data storage
│   ├── anime_updated.csv # Processed dataset for RAG
│   └── anime_with_synopsis.csv # Raw dataset
├── logs/                 # Application logs
├── pipeline/             # Orchestration scripts
│   ├── build_pipeline.py # Data ingestion script
│   ├── pipeline.py       # Recommendation logic pipeline
│   └── __init__.py       # Package marker
├── project_workflow.md   # Detailed architectural workflow
├── pyproject.toml        # Project metadata & strict dependencies
├── requirements.txt      # Legacy pip requirements
├── setup.py              # Package installation script
├── src/                  # Core logic modules
│   ├── data_loader.py    # CSV processing logic
│   ├── prompt_template.py# LLM prompt templates
│   ├── recommender.py    # RAG chain implementation
│   ├── vector_store.py   # ChromaDB & Embedding management
│   └── __init__.py       # Package marker
├── utils/                # Utility functions
│   ├── custom_exception.py # Custom error handling
│   ├── logger.py         # Logging configuration
│   └── __init__.py       # Package marker
└── uv.lock               # Exact dependency lockfile
```

---


## License

Distributed under the MIT License. See `LICENSE` for more information.