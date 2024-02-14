import json

c = []

with open("classes/classes.json", 'r') as file:
    contents = json.loads(file.read())
    for level in contents["artificer"]["spell_slots"]:
        for spell_level in level:
            if spell_level == "1st":
                c["1"] =spell_level["1st"]
            for spell in contents["cantrips"]:
                add_data = {"spell_id": int(spell), "spell_level": 0}
                add_data.update(contents["cantrips"][spell])
                c.append(add_data)
        else:
            for spell in contents["1st"]:
                add_data = {"spell_id": int(spell)+31, "spell_level": 1}
                add_data.update(contents["1st"][spell])
                c.append(add_data)

with open("spells.json", "w", encoding='utf8') as outfile:
    json.dump(c, outfile, indent=2, ensure_ascii=False)

