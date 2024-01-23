import json, requests, base64, io, argparse


def query_image(encoded_string: str, prompt: str) -> json:
    url = "http://ollama:11434/api/generate"
    data = {
        "model": "llava",
        "prompt": prompt,
        "stream": False,
        "images": [encoded_string]
    }

    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code


def generate_image_base64(image_file: str) -> str:
    with open(image_file, 'rb') as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    parser.add_argument('--prompt', type=str)

    args = parser.parse_args()
    image_file = args.path
    prompt = args.prompt

    encoded_string = generate_image_base64(image_file)
    response = query_image(encoded_string, prompt)
    print(response)


if __name__ == "__main__":
    main()