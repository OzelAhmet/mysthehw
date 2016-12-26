def hyphenate(word):
  pivot = 0
  word = list(word)
  vowel = ["a","e","I","i","o","O","u","U"]
  while True:
    if word[pivot] not in vowel :
      if pivot+1 == len(word) : 
        return "".join(word).split("-")
      else:
        pivot += 1
        continue
    else:
      if pivot+1 == len(word) :
        return "".join(word).split("-")
      pivot += 1
      if word[pivot] in vowel:
        word.insert(pivot,"-")
        pivot += 1
        continue
      else:
        while True: 
          if pivot+1 == len(word):
            return "".join(word).split("-")
          else:
            pivot += 1
            if word[pivot] not in vowel:
              continue
            else :
              word.insert(pivot-1,"-")
              pivot -= 1
              break
        
  
print hyphenate("kuyruksallayangillersizleStiricileStiriveremeyebileceklerimizdenmiSsinizcesine")
