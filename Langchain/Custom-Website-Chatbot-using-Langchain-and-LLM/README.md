# Custom Website Chatbot Using LangChain and LLM

This project demonstrates a modular implementation of a custom chatbot that interacts with website content using LangChain and a large language model (LLM). The chatbot extracts text from specified URLs, processes it, stores embeddings in a vector database, and provides a question-answering system with sources.

---

## Features

- **Text Extraction:** Extracts and processes data from website URLs using `UnstructuredURLLoader`.
- **Text Splitting:** Splits extracted data into manageable chunks for embedding and processing.
- **Embeddings Creation:** Generates embeddings using OpenAI's embeddings API.
- **Vector Database Storage:** Stores embeddings in the FAISS vector database for efficient retrieval.
- **Chatbot Pipeline:** Uses LangChain to create a question-answering system with source retrieval.
- **Modular Design:** Each functionality is encapsulated in a separate function for better maintainability.

---

## Tech Stack

- **Programming Language:** Python
- **Frameworks and Libraries:**
  - LangChain
  - FAISS
  - OpenAI API
  - dotenv for environment variables

---


## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MalavikaGowthaman/Custom-Website-Chatbot-using-LangChain-and-LLM.git
   cd Custom-Website-Chatbot-using-LangChain-and-LLM
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv customchatbot
   source customchatbot/bin/activate  # Linux/Mac
   customchatbot\Scripts\activate     # Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Your API Key:**
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key_here
     ```

---

## Usage

1. **Add URLs to `urls.py`:**
   Specify the URLs to process as a list:
   ```python
   URLs = ["https://example.com/article1", "https://example.com/article2"]
   ```

2. **Run the Pipeline:**
   Execute the `helper.py` script to process URLs and create the chatbot:
   ```bash
   python src/helper.py
   ```

3. **Interact with the Chatbot:**
   Use the chain returned by `llm_pipeline` to ask questions and retrieve answers.

---

## Example Output

```plaintext
Question: What is the purpose of the website?
Answer: The website focuses on providing high-quality resources for developers.
Source: https://example.com/article1
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
