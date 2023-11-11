import openai

openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "Whatever"

messages = [
    {'role': 'system', 'content': 'you are a helpful assistant  named  Emma'}
]


def ReplyBrain(question, chat_log=None):
    FileLog = open("DataBase\\chat_log.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template
    prompt = f'{chat_log}Emma : {question}\nEmma :'

    messages.append({'role': 'user', 'content': question})

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )

    answer = response.choices[0].message['content'].strip()
    chat_log_template_update = chat_log_template + \
        f" \nEmma : {question} \nEmma:{answer}"
    FileLog = open("DataBase\\chat_log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()

    messages.append(
        {'role': 'assistant', 'content': answer})

    return answer
