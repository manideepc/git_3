def check_anagrams(s1, s2):
     
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.")
def check_element(lst, element):
    if element in lst:
        print("The element is in the list.")
    else:
        print("The element is not in the list.")

