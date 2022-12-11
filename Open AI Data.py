import openai

openai.api_key = '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'

prompt = input("Enter your command: ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

text = response.get('choices')[0].get('text')
print(text)