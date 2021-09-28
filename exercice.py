#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0 :
        number *= -1

    return number   # En une seule ligne : return number if number > 0 else number * -1


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    names = []

    for elements in prefixes :
        names.append(elements + suffixe)

    return names


def prime_integer_summation() -> int:
    import math 
    first100_primes = [2, 3]
    prime_nb = 2
    test_value = 4
    while prime_nb < 100 :
      last_potentialDivider = int(math.sqrt(test_value))+1
      for potentialDividers in range(2 , last_potentialDivider) :
              if test_value % potentialDividers == 0 :
                    break
              elif potentialDividers < (last_potentialDivider-1) :
                    continue
              else: first100_primes.append(test_value)
              prime_nb += 1 
      test_value +=1
  
    return sum(first100_primes)


def factorial(number: int) -> int:
    result = 1
    while number > 1 :
        result *= number
        number -= 1

    return result


def use_continue() -> None:
    for number in range(1,11) :
        if number == 5 :
            continue
        print(number)
    


def verify_ages(groups: List[List[int]]) -> List[bool]:
    acceptency = []
    for group_nb in groups :
        members = len(group_nb)
        if members <= 3  :
            result = False
        elif members > 10 : 
            result = False
        else : 
            result = True
            for i, age in enumerate(group_nb) : 
                if age < 18 :
                    result = False
                    continue
                elif age == 25 : 
                    result = True
                    break
                elif age == 50 : 
                    for age in group_nb :
                        if age > 70 : 
                            result = False
                        else : break
                else : continue
        acceptency.append(result)
    return acceptency


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
