import sys
import os
import numpy
import nltk
import torch
import textwrap
from src.config import OPENAI_API_KEY
from src.document_loader import load_documents
from src.text_processor import process_text
from src.chain_handler import create_chain



# Add the project's root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    urls = [
    "https://medium.com/@malavikagowthaman/the-ultimate-roadmap-to-becoming-an-ai-engineer-f8b262c6ecb6",
    "https://www.linkedin.com/pulse/introduction-gen-ai-malavika-gowthaman-nlxmc/?trackingId=hzYLZuX7S2qy%2FbNR1kbhZg%3D%3D",
    "https://www.linkedin.com/pulse/end-pipeline-generative-ai-malavika-gowthaman-sckwc/?trackingId=hzYLZuX7S2qy%2FbNR1kbhZg%3D%3D",
    "https://www.linkedin.com/pulse/essential-text-preprocessing-techniques-generative-ai-gowthaman-o34lc/?trackingId=hzYLZuX7S2qy%2FbNR1kbhZg%3D%3D"
]
    
    documents = load_documents(urls)
    vectorstores = process_text(documents)
    chain = create_chain(vectorstores)
    
    while True: 
        query = input(f"Prompt: ")
        # print("Question: ",query)
        if query == 'q':
            print("Exiting")
            sys.exit()
            q
        if query == "":
            continue
        result=chain({'question':query})
        print("Question: ",query)
        print(f"Answer: " +result["answer"])
        
        
if __name__ == "__main__":
    main()