import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI









def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("Missing api key")


    # established connect with llm
    client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            )


    # generate a user prompt 
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    messages = [ {
        "role": "user",
        "content": args.user_prompt
    },
]
    
    # generatea llm responce
    response = client.chat.completions.create(
            model = "openrouter/free",
            messages = messages,
            )   

    if response.usage is None:
        raise RuntimeError('No responce was generated')
    
    print(f'User prompt: {messages[0]["content"]}') 
    print(f'Prompt tokens: {response.usage.prompt_tokens}') 
    print(f'Response tokens: {response.usage.completion_tokens}') 
    print(f'Response:')
    print(f'{response.choices[0].message.content}')

if __name__ == "__main__":
    main()
