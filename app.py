import openai
import streamlit as st
import re

openai.api_key = "EMPTY" # Key is ignored and does not matter
openai.api_base = "http://zanino.millennium.berkeley.edu:8000/v1"

#Query Gorilla Server
def get_gorilla_response(prompt, model):
    try:
        completion = openai.ChatCompletion.create(
            model = model,
            messages = [{"role": "user", "content": prompt}]
        )
        print("Response: ", completion)
        return completion.choices[0].message.content 
    except Exception as e:
        print("Sorry, something went wrong!")

def extract_code_from_output(output):
    # code_start_index = output.find("<<<code>>>:")
    # if code_start_index == -1:
    #     return None
    # code_start_index += len("<<<code>>>:")
    
    # code_end_index = output.find("<<<", code_start_index)
    # if code_end_index == -1:
    #     return None
    
    # code = output[code_start_index:code_end_index].strip()
    code =output.split("<<<code>>>:")[1]
    return code

st.set_page_config(layout="wide")

def main():
    st.title("Gorilla LLM Demo App 🦍‍👤")

    input_prompt = st.text_area("Enter your prompt below:")

    option = st.selectbox('Select a model option from the list:', ('gorilla-7b-hf-v1', "gorilla-mpt-7b-hf-v0"))

    if st.button("Gorilla Magic"):
        if len(input_prompt) > 0:
            col1, col2 = st.columns([1,1])
            with col1:
                if option == "gorilla-7b-hf-v1":
                    result = get_gorilla_response(prompt=input_prompt, model=option)
                    st.write(result)
                elif option == "gorilla-mpt-7b-hf-v0":
                    result = get_gorilla_response(prompt=input_prompt, model=option)
                    st.write(result)
                # elif option == "gorilla-mpt-7b-hf-v0":
                #     result = get_gorilla_response(prompt=input_prompt, model=option)
                #     st.write(result)

            with col2:
                # pass
                if option == "gorilla-7b-hf-v1":
                    # code_result = get_gorilla_response(prompt=input_prompt, model=option)
                    code_result = extract_code_from_output(result)
                    st.code(code_result, language='python')
                elif option == "gorilla-mpt-7b-hf-v0":
                    # code_result = get_gorilla_response(prompt=input_prompt, model=option)
                    code_result = extract_code_from_output(result)
                    # code_result = code_result.replace('\n', ' \n ')
                    lines = code_result.split('\\n')
                    for line in lines:
                        st.code(line, language='python')
                # elif option == "gorilla-mpt-7b-hf-v0":
                #     code_result = get_gorilla_response(prompt=input_prompt, model=option)
                #     code_result = extract_code_from_output(code_result)
                #     st.code(code_result)

if __name__ == "__main__":
    main()

