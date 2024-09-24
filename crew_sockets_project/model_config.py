from openai import OpenAI
import os
def yield_generation(messages: list[dict[str, str]]):
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model='gpt-4o',
        messages=messages
    )
    answer = completion.choices[0].message.content
    return answer

def get_config_messages(sequence:list[str]) -> list[dict[str, str]]:
    messages = []
    # <Suppose> sequence = ['You are a python expert developer', 'What is the best way to learn python?','Searching media for python tutorials']
    # <The output should be> messages = [{'role': 'system', 'content': 'You are a python expert developer'}, {'role': 'user', 'content': 'What is the best way to learn python?'}, {'role': 'assistant', 'content': 'Searching media for python tutorials'}]
    for idx, seq in enumerate(sequence):
        if idx == 0:
            messages.append({'role': 'system', 'content': seq})
        elif idx % 2 == 0:
            messages.append({'role': 'assistant', 'content': seq})
        else:
            messages.append({'role': 'user', 'content': seq})
    return messages