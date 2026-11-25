def mismatched_words(sentence_a: str, sentence_b: str) -> list[str]:
  sa = sentence_a.split(" ")
  sb = sentence_b.split(" ")
  return (
    [a for a in sa if a not in sb]
    +
    [b for b in sb if b not in sa]
  )
