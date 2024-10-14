from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "영어를 한국어로 번역해야합니다."},
              {"role": "system", "content": "dog 는 한국어로 개"},
              {"role": "system", "content": "cat은 한국어로 고양이"},
              {"role": "system", "content": "lion 은 한국어로 사자"},
              {"role": "system", "content": "tiger 는 한국어로 호랑이"},
              {"role": "user", "content": "dog 가 한국어로 뭐야?"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
