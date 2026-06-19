# Chatbot: Local AI Lab Terminal

This project provides an offline, local AI chatbot experience, designed to answer queries based on a specialized RAG (Retrieval Augmented Generation) database. It leverages a local Large Language Model (LLM) for processing and a Streamlit interface for user interaction, alongside a FastAPI backend for API access.

## Features

*   **Offline RAG Chatbot:** Operates completely offline, utilizing a local RAG database sourced from `product_descriptions.txt`.
*   **Llama 3.2 Integration:** Powered by a local Llama 3.2 model via Ollama for natural language understanding and generation.
*   **Streamlit User Interface:** A clean, intuitive "Local AI Lab Terminal" web interface for direct user interaction.
*   **FastAPI Backend:** Exposes an API for programmatic access, complete with CORS enabled for secure integration with external applications (e.g., WordPress).
*   **Configurable Data Source:** Easily integrates with local text files for domain-specific knowledge retrieval.

## Tech Stack

*   **Python**
*   **Streamlit:** For the interactive web UI.
*   **FastAPI:** For the backend API and inter-application communication.
*   **Ollama:** To serve and manage local LLM inference (Llama 3.2).
*   **RAG (Retrieval Augmented Generation):** Core architecture for context-aware responses.

## Installation

To set up and run the chatbot locally, follow these steps:

### Prerequisites

1.  **Python 3.8+:** Ensure Python is installed on your system.
2.  **Ollama:**
    *   Download and install Ollama from [ollama.com](https://ollama.com/).
    *   Pull the Llama 3.2 model (or a compatible version if Llama 3.2 is not available yet, as indicated by the project's checkpoint name "Test7?") by running:
        ```bash
        ollama run llama3.2 # (Adjust model name if different, e.g., ollama run llama3)
        ```
        This command will download the model if it's not already present.

### Project Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/chatbot.git # (Replace with actual repo URL)
    cd chatbot
    ```
2.  **Install Python dependencies:**
    ```bash
    pip install streamlit fastapi uvicorn ollama
    ```
3.  **Prepare Data:**
    *   Ensure the `data` directory exists at the root of the project.
    *   Place your product descriptions in `data/product_descriptions.txt`.
        *(Note: The `DATA_PATH` in `rag_backend.py` and `local_bridge.py` is currently configured to an absolute path `E:\AI_Lab\Projects\chatbot\data\product_descriptions.txt`. You will need to **update this path** in both `rag_backend.py` and `local_bridge.py` to match your local project directory for correct operation.)*

## Usage

The project can be run in two main ways: via the Streamlit UI or by starting the FastAPI backend API.

### 1. Running the Streamlit Chatbot UI

To launch the interactive chat terminal:

```bash
streamlit run app.py
```

This will open the "🤖 Local AI Lab Terminal" in your web browser, where you can interact with the RAG chatbot.

### 2. Running the FastAPI Backend

To start the API server for external applications:

```bash
uvicorn local_bridge:app --reload
```

The API will be available at `http://127.0.0.1:8000` (or another port if configured). You can then send requests to its endpoints (e.g., for chatbot queries from a WordPress site, as hinted by the CORS configuration).