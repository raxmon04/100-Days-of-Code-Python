with open("/mnt/d/Git/python/024_MailMerge/Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("/mnt/d/Git/python/024_MailMerge/Input/Letters/starting_letter.txt") as letter_file:
    starting_letter_content = letter_file.read()
    
    for name in names:
        name_stripped = name.strip()
        new_letter = starting_letter_content.replace("[name]", name_stripped)
        with open(f"/mnt/d/Git/python/024_MailMerge/Output/ReadyToSend/letter_for_{name_stripped}.txt", mode="w") as letter_file:
            letter_file.write(new_letter)