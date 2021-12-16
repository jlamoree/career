import json

with open("skills.json") as skills_data_file:
    skills = json.load(skills_data_file)

print("Experience (Years)")
experience = {key: value["years"] for (key, value) in skills.items()}
for skill in sorted(experience, key=experience.get, reverse=True):
    print(f"{skill: >10} {'*' * experience[skill]} ({experience[skill]})")

print("\nCompetency (Out of Ten)")
competency = {key: value["competency"] for (key, value) in skills.items()}
for skill in sorted(competency, key=competency.get, reverse=True):
    print(f"{skill: >10} {'*' * competency[skill]} ({competency[skill]})")

print("\nInterest (Out of Ten)")
interest = {key: value["interest"] for (key, value) in skills.items()}
for skill in sorted(interest, key=interest.get, reverse=True):
    print(f"{skill: >10} {'*' * interest[skill]} ({interest[skill]})")

