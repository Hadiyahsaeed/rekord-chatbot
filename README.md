```markdown
# Chatbot: Local AI Lab Terminal

This project provides an offline, Retrieval Augmented Generation (RAG) chatbot leveraging a local Llama 3.2 Large Language Model. It features a user-friendly Streamlit interface and an optional FastAPI bridge for broader integration. The chatbot is designed to answer questions based on a specific, localized knowledge base, exemplified here with product descriptions from WnsFeild Pharmaceuticals.

## Features

*   **Offline Operation:** Runs entirely on your local machine, ensuring data privacy and no internet dependency.
*   **Llama 3.2 Integration:** Utilizes the Llama 3.2 model for advanced natural language understanding and generation, powered by Ollama.
*   **Retrieval Augmented Generation (RAG):** Augments LLM responses by retrieving relevant information from a local document store (`data/product_descriptions.txt`).
*   **Streamlit Web UI:** Provides an intuitive and sleek web-based chat interface for direct interaction.
*   **FastAPI Bridge:** Exposes RAG functionality via a robust FastAPI endpoint, enabling easy integration with other applications (e.g., WordPress front-ends).
*   **Custom Knowledge Base:** Configurable to query specific domain data, demonstrated with WnsFeild Pharmaceuticals product descriptions.

## Tech Stack

*   **Python:** The core programming language.
*   **Streamlit:** For building interactive web applications.
*   **Ollama:** Platform for running local large language models.
*   **Llama 3.2:** The specific large language model used for AI capabilities.
*   **FastAPI:** For creating the high-performance API bridge.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url> # Replace with your actual repository URL
    cd chatbot
    ```

2.  **Set up a Python Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows: .\venv\Scripts\activate
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install streamlit fastapi uvicorn "python-multipart[standard]"
    ```

4.  **Install and Configure Ollama:**
    *   Download and install the Ollama application from [ollama.com](https://ollama.com/).
    *   Pull the Llama 3.2 model using Ollama. For example:
        ```bash
        ollama pull llama3 # Ensure a 'llama3.2' compatible version is available or adapt as needed.
        ```

5.  **Adjust Data Path (Crucial):**
    The `DATA_PATH` is currently hardcoded in `rag_backend.py` and `local_bridge.py`. **You must update this path** to reflect the absolute location of your `data/product_descriptions.txt` file on your local system.
    *   Open `rag_backend.py` and `local_bridge.py`.
    *   Modify `DATA_PATH = r"E:\AI_Lab\Projects\chatbot\data\product_descriptions.txt"` to point to the correct path on your machine.

## Usage

You can run the chatbot using either the Streamlit web interface or the FastAPI bridge. Ensure all installation steps, especially the data path configuration and Ollama model setup, are completed first.

### 1. Streamlit Web Interface

To start the interactive chat terminal:

```bash
streamlit run app.py
```
Open your web browser to the address provided by Streamlit (usually `http://localhost:8501`). You can then interact with the chatbot directly through the web UI.

### 2. FastAPI Bridge

To launch the API endpoint:

```bash
uvicorn local_bridge:app --reload --host 0.0.0.0 --port 8000
```
The API will be accessible at `http://localhost:8000`. Specific endpoints for interaction (e.g., for sending chat messages and receiving responses) are defined within the `local_bridge.py` file.
```