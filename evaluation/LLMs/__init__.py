from LLMs.PaLM2 import PaLM2
from LLMs.Vicuna import Vicuna
from LLMs.GPT import GPT
from LLMs.Llama import Llama
import json

def load_json(file_path):
    with open(file_path) as file:
        results = json.load(file)
    return results

def create_model(config_path):
    """
    Factory method to create a LLM instance
    """
    config = load_json(config_path)

    provider = config["model_info"]["provider"].lower()
    if provider == 'palm2':
        model = PaLM2(config)
    elif provider == 'vicuna':
        model = Vicuna(config)
    elif provider == 'gpt':
        model = GPT(config)
    elif provider == 'llama':
        model = Llama(config)
    else:
        raise ValueError(f"ERROR: Unknown provider {provider}")
    return model