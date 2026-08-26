import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion








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


    # parser generater
    parser = argparse.ArgumentParser(description="Chatbot")
      # user prompt
    parser.add_argument("user_prompt", type=str, help="User prompt")
      # verbose flag
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    messages = [ {
        "role": "user",
        "content": args.user_prompt
    },
]
    
    response = generate_response(messages, client) 

    result(messages, response, args.verbose)
    


def generate_response(messages: list[dict[str, str]], client: OpenAI) -> ChatCompletion:
    response = client.chat.completions.create(
            model = "openrouter/free",
            messages = messages,
            )   

    if response.usage is None:
        raise RuntimeError('No response was generated')
    
    return response



def result(messages: list[dict[str, str]], response: ChatCompletion, verbose: bool) -> None:
    if verbose:
       print(f'User prompt: {messages[0]["content"]}') 
       print(f'Prompt tokens: {response.usage.prompt_tokens}') 
       print(f'Response tokens: {response.usage.completion_tokens}') 
    
    print('Response:')
    print(f'{response.choices[0].message.content}')





if __name__ == "__main__":
    main()
