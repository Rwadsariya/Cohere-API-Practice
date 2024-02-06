import cohere
co = cohere.Client('9SGUDhcVgm6ZuLxdRLvEQDSnMxPiu6nLuxnThE0u')

response = co.generate(
  prompt='Please explain to me how LLMs work',
)
print(response)