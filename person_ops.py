person_ops = [
    {"action": "P&Q side1->side2", "preconds": ["P side1", "Q side1", "Lantern side1"],
     "add": ["P side2", "Q side2", "Lantern side2"], "delete": ["P side1", "Q side1", "Lantern side1"]},

    {"action": "P&R side1->side2", "preconds": ["P side1", "R side1", "Lantern side1"],
     "add": ["P side2", "R side2", "Lantern side2"], "delete": ["P side1", "R side1", "Lantern side1"]},

    {"action": "P&S side1->side2", "preconds": ["P side1", "S side1", "Lantern side1"],
     "add": ["P side2", "S side2", "Lantern side2"], "delete": ["P side1", "S side1", "Lantern side1"]},

    {"action": "Q&R side1->side2", "preconds": ["Q side1", "R side1", "Lantern side1"],
     "add": ["Q side2", "R side2", "Lantern side2"], "delete": ["Q side1", "R side1", "Lantern side1"]},

    {"action": "Q and S side1 to side2", "preconds": ["Q side1", "S side1", "Lantern side1"],
     "add": ["Q side2", "S side2", "Lantern side2"], "delete": ["Q side1", "S side1", "Lantern side1"]},

    {"action": "R and S side1 to side2", "preconds": ["R side1", "S side1", "Lantern side1"],
     "add": ["R side2", "S side2", "Lantern side2"], "delete": ["R side1", "S side1", "Lantern side1"]},

    {"action": "P and Q side2 to side1", "preconds": ["P side2", "Q side2", "Lantern side2"],
     "add": ["P side1", "Q side1", "Lantern side1"], "delete": ["P side2", "Q side2", "Lantern side2"]},

    {"action": "P and R side2 to side1", "preconds": ["P side2", "R side2", "Lantern side2"],
     "add": ["P side1", "R side1", "Lantern side1"], "delete": ["P side2", "R side2", "Lantern side2"]},

    {"action": "P and S side2 to side1", "preconds": ["P side2", "S side2", "Lantern side2"],
     "add": ["P side1", "S side1", "Lantern side1"], "delete": ["P side2", "S side2", "Lantern side2"]},

    {"action": "Q and R side2 to side1", "preconds": ["Q side2", "R side2", "Lantern side2"],
     "add": ["Q side1", "R side1", "Lantern side1"], "delete": ["Q side2", "R side2", "Lantern side2"]},

    {"action": "Q and S side2 to side1", "preconds": ["Q side2", "S side2", "Lantern side2"],
     "add": ["Q side1", "S side1", "Lantern side1"], "delete": ["Q side2", "S side2", "Lantern side2"]},

    {"action": "R and S side2 to side1", "preconds": ["R side2", "S side2", "Lantern side2"],
     "add": ["R side1", "S side1", "Lantern side1"], "delete": ["R side2", "S side2", "Lantern side2"]},

    {"action": "P side1 to side2", "preconds": ["P side1", "Lantern side1"],
     "add": ["P side2", "Lantern side2"], "delete": ["P side1", "Lantern side1"]},
    {"action": "Q side1 to side2", "preconds": ["Q side1", "Lantern side1"],
     "add": ["Q side2", "Lantern side2"], "delete": ["Q side1", "Lantern side1"]},
    {"action": "R side1 to side2", "preconds": ["R side1", "Lantern side1"],
     "add": ["R side2", "Lantern side2"], "delete": ["R side1", "Lantern side1"]},
    {"action": "S side1 to side2", "preconds": ["S side1", "Lantern side1"],
     "add": ["S side2", "Lantern side2"], "delete": ["S side1", "Lantern side1"]},

    {"action": "P side2 to side1", "preconds": ["P side2", "Lantern side2"],
     "add": ["P side1", "Lantern side1"], "delete": ["P side2", "Lantern side2"]},
    {"action": "Q side2 to side1", "preconds": ["Q side2", "Lantern side2"],
     "add": ["Q side1", "Lantern side1"], "delete": ["Q side2", "Lantern side2"]},
    {"action": "R side2 to side1", "preconds": ["R side2", "Lantern side2"],
     "add": ["R side1", "Lantern side1"], "delete": ["R side2", "Lantern side2"]},
    {"action": "S side2->side1", "preconds": ["S side2", "Lantern side2"],
     "add": ["S side1", "Lantern side1"], "delete": ["S side2", "Lantern side2"]}
]
gps(['P side1','Q side1','R side1','S side1','Lantern side1'],
 ['P side2','Q side2','R side2','S side2','Lantern side2'],
 person_ops)
