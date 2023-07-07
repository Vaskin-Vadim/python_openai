import openai

openai.api_key = 'YOUR_API_KEY'

def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=3796,  # Максимальное количество токенов в каждом запросе
        temperature=0.8,
        n=1,
        stop=None,
        timeout=50  # Опционально: установите таймаут на запрос
    )
    return response.choices[0].text.strip()

while True:
    vopros = input("Введите запрос: ")
    if vopros == "no":
        break
    else:
        otvet = generate_response(vopros)
        print(otvet)
