from openai import OpenAI

from GPTneo import extract_mika_response, generate_response, get_user_input


def get_response(user_input:str, user:str)->str:
    lower:str=user_input.lower()
    #This is the part where the LLM model will be implemented
    if lower=='':
        return 'Say something Sensei!'
    elif 'hello' in lower:
        return 'Hello {} Sensei!'.format(user)

def mikaGPT_response(user_input: str, user: str) -> str:
    if user_input == '':
        return 'Say something {}-Sensei!'.format(user)
    else:
        response = extract_mika_response(generate_response(get_user_input(user_input, user)))
        return response[12:]
