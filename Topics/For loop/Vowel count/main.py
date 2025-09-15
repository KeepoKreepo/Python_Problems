string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
counter = 0
for character in string:
    if character in vowels:
        counter += 1
print(counter)