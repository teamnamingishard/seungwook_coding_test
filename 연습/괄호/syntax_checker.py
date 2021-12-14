pair = {")": "(", "}": "{", "]":"["}

def syntax_checker(input: str) -> bool:
  stack = []
  for character in input:
    if character in pair.values():
      stack.append(character)
    elif character in pair.keys():
      if not stack or pair[character] != stack.pop():
        return False
  return not stack