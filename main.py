import os
from dotenv import load_dotenv
from openai import OpenAI









def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("Missing api key")

    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
