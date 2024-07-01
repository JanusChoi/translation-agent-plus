import ollama
from typing import Union

system_message = f"You are an expert linguist, specializing in translation from English to Chinese."

def get_completion(
    prompt: str,
    system_message: str = "You are a helpful assistant.",
    model: str = "llama3",
    temperature: float = 0.3,
    json_mode: bool = False,
) -> Union[str, dict]:

    if json_mode:
        response = ollama.chat(
            model=model,
            # temperature=temperature,
            # top_p=1,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
            options={"temperature": temperature, "top_p": 1}
        )
        return response
        # return response["message"]["content"]
    else:
        response = ollama.chat(
            model=model,
            # temperature=temperature,
            # top_p=1,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt},
            ],
            options={"temperature": temperature, "top_p": 1}
        )
        return response
        # return response["message"]["content"]

print("starting")
# 调用Llama3模型进行对话
prompt="将以下文本翻译为中文：Almost any discussion of quantum computing—whether in a research article, popular science magazine, or business journal—invokes some comparison to what is called “classical” computing. It’s nearly impossible to talk about quantum computing without using the phrase, so we better start there."

translation = get_completion(prompt, system_message=system_message)
# response = ollama.chat(
#     model="llama3",
#     messages=[
#         {
#             "role": "user",
#             "content": "告诉我一个关于大象的有趣事实"
#         }
#     ]
# )

# 打印模型的响应
print(translation)