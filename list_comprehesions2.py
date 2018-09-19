words = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog"]
answer = [[x.upper(), x.lower(), len(x)] for x in words]
print(answer)