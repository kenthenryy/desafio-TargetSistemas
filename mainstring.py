def count_a(s):
    s = s.lower()
    count = s.count("a")
    if count > 0:
        print(f"A letra 'a' está presente {count} vezes na string.")
    else:
        print("A letra 'a' não existe na string.")


string_input = input("Informe a string: ")
count_a(string_input)