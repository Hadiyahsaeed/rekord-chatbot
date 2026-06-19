# chatbot

An offline, local AI chatbot leveraging Llama 3.2 and Retrieval Augmented Generation (RAG) to provide intelligent answers based on a specialized product catalog. This project offers both a Streamlit web interface for interactive chat and a FastAPI backend for flexible integration.

## Features

*   **Offline Operation**: Runs entirely locally, ensuring data privacy and reducing reliance on external services.
*   **Llama 3.2 Integration**: Utilizes the powerful Llama 3.2 Large Language Model for generating coherent and contextually relevant responses.
*   **Retrieval Augmented Generation (RAG)**: Enhances AI responses by dynamically retrieving and incorporating information from a curated product description database.
*   **Streamlit Web Interface**: Provides a user-friendly and interactive front-end for direct engagement with the chatbot.
*   **FastAPI Backend**: Offers a robust RESTful API endpoint for chatbot interactions, with CORS enabled for seamless integration with other applications (e.g., WordPress).
*   **Product Catalog Integration**: Specifically designed to process and provide answers based on detailed product descriptions.

## Tech Stack

*   **Python**: The core programming language.
*   **Streamlit**: For building the interactive web user interface.
*   **FastAPI**: For creating the high-performance RESTful API backend.
*   **Ollama**: Used for running Large Language Models locally.
*   **Llama 3.2**: The specific Large Language Model employed for AI inference.
*   **Retrieval Augmented Generation (RAG)**: The architectural pattern used for enhanced knowledge retrieval.

## Installation

Follow these steps to set up and run the chatbot project locally:

1.  **Clone the Repository (Placeholder)**
    ```bash
    git clone <repository-url>
    cd chatbot
    ```

2.  **Create and Activate a Python Virtual Environment**
    ```bash
    python -m venv .venv
    # On Windows:
    .\.venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Install Python Dependencies**
    ```bash
    pip install streamlit fastapi uvicorn ollama
    ```

4.  **Install and Run Ollama**
    *   Download and install Ollama from [ollama.ai](https://ollama.ai/).
    *   Pull the Llama 3.2 model:
        ```bash
        ollama pull llama3.2
        ```
    *   Ensure the Ollama server is running in the background.

5.  **Data Setup**
    *   Ensure the `data` directory exists at the project root.
    *   Place your `product_descriptions.txt` file inside the `data` directory.
    *   **Important**: The `rag_backend.py` and `local_bridge.py` files contain hardcoded absolute paths (e.g., `E:\AI_Lab\Projects\chatbot\data\product_descriptions.txt`). **You must update these paths** to reflect the actual location of your `product_descriptions.txt` file on your system.

## Usage

Once installed and configured, you can start the chatbot's components:

1.  **Start the FastAPI Backend**
    This will launch the API server, typically accessible at `http://127.0.0.1:8000`.
    ```bash
    uvicorn local_bridge:app --reload
    ```

2.  **Start the Streamlit User Interface**
    This will open the web interface in your default browser, typically at `http://localhost:8501`.
    ```bash
    streamlit run app.py
    ```

You can now interact with the chatbot through the Streamlit interface, or make requests to the FastAPI endpoint for programmatic access.