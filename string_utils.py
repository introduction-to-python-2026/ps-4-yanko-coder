def split_before_each_uppercases(formula):
  start, end = 0,0
  split_formula = []
  for i,value in enumerate(formula):
    if i == 0:
     continue
    if value.isupper():
      end = i
      split_formula.append(formula[start:end])
      start = end
      if i == len(formula)-1:
         split_formula.append(formula[-1])
    elif i == len(formula)-1:
       split_formula.append(formula[start:])
  return split_formula


def split_at_first_digit(formula):
  for i,value in enumerate(formula):
     x = value.isdigit()
     if x:
        break
  if x:
     letters = formula[:i]
     digits = int(formula[i:])
  else:
     letters = formula
     digits = 1
  return letters, digits
