# program to merge two dictionaries
info = {
    "name": "gulzar",
    "class": "btech",
    "roll": 59,
}

program = {
    "language": "python",
    "project": "school management"

}

info.update(program)
print(info)

reesult = info | program
print(reesult)
