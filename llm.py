'''
This file will prompt the user, call the llm, and respond to the user.
'''
#import libraries
from transformers import pipeline



def prompt_user(user_prompt: str) -> str:
    '''
    args:
    prompt (str)    : The prompt the user wants to use for the llm.
    returns:
    (str)           : This is the response from the user
    '''
    get_user_input = input(user_prompt)
    return get_user_input

def call_model(llm_prompt: str) -> str:
    '''
    '''
    pipe = pipeline("text2text-generation", model="google/flan-t5-base")
    result = pipe(llm_prompt, max_new_tokens=100)
    return result[0]["generated_text"]

    '''OPTION 1; YIELDS MANY HALLUCINATIONS'''
    # pipe = pipeline("text-generation", model="crumb/nano-mistral")
    # result = pipe(llm_prompt)
    # return result[0]['generated_text'] #the generated text

if __name__ == '__main__':
    string = 'Enter a question: '
    user_query = prompt_user(string)

    # call_model(user_query)
    ans = call_model(user_query)
    print(f'The answer from the llm: {ans}')

