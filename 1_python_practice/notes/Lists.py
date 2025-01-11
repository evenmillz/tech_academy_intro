Python 3.11.7 (v3.11.7:fa7a6f2303, Dec  4 2023, 15:22:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
Best_bands_list = ["The Beatles", "Rolling Stones", "Led Zeppelin", "Beach Boys"]
print(Best_Bands_list)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(Best_Bands_list)
NameError: name 'Best_Bands_list' is not defined. Did you mean: 'Best_bands_list'?
print(Best_bands_list)
['The Beatles', 'Rolling Stones', 'Led Zeppelin', 'Beach Boys']
Run
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Run
NameError: name 'Run' is not defined
>>> print(Best_bands_list)
['The Beatles', 'Rolling Stones', 'Led Zeppelin', 'Beach Boys']
>>> print(Best_bands_list + "These are the best bands from the 1960s!")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(Best_bands_list + "These are the best bands from the 1960s!")
TypeError: can only concatenate list (not "str") to list
>>> Best_bands_list = ["The Beatles", "Rolling Stones", "Led Zepplin", "Beach Boys"]
>>> print(Best_bands_list[0] + " is an awsome band!")
The Beatles is an awsome band!
>>> print(Best_bands_list[0] + " is an awesome band!")
The Beatles is an awesome band!
>>> print(Best_bands_list[0, 1, 2, 3] + " is an awesome band!")
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(Best_bands_list[0, 1, 2, 3] + " is an awesome band!")
TypeError: list indices must be integers or slices, not tuple
>>> Best_bands_list.append("The Temptations")
>>> print(Best_bands_list)
['The Beatles', 'Rolling Stones', 'Led Zepplin', 'Beach Boys', 'The Temptations']
>>> Best_bands_list[2] = "The Supremes"
>>> print(Best_bands_list)
['The Beatles', 'Rolling Stones', 'The Supremes', 'Beach Boys', 'The Temptations']
>>> import time
>>> Best_80s_bands_list = ["A-ha", "Depeche Mode", "Tears For Fears", "The Cure"]
>>> for band in Best_80s_bands_list:
...     print(band+ " is a radical band!")
...     time.sleep(.5)
... 
...     
A-ha is a radical band!
Depeche Mode is a radical band!
Tears For Fears is a radical band!
The Cure is a radical band!
