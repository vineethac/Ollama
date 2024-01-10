from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default="llama2")

args = parser.parse_args()
model = args.model

llm = Ollama(
        model=model, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]), base_url="http://ollama:11434"
)

while True:
    print(f"Model: {model}")
    prompt = input("Ask me anything: ")

    if prompt=="/bye":
        break

    llm(prompt)
    print("\n \n")