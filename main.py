def main():
  list = [1, 2, 3]
  print(list)
  permutations = []
  for n in list:
    new_list = list.copy()
    new_list.remove(n)
    for i in range(len(new_list) + 1):
      perm = new_list.copy()
      perm.insert(i, n)
      permutations.append(perm)
  print(permutations)

main()
