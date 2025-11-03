disk_ops = [
    {
        "action": "Move green disk from pole to table",
        "preconds": ["green-disk-on-pole", "green-disk-on-top"],
        "add": ["green-disk-on-table"],
        "delete": ["green-disk-on-pole", "green-disk-on-top"]
    },
    {
        "action": "Move blue disk from pole to table",
        "preconds": ["blue-disk-on-pole", "blue-disk-on-top"],
        "add": ["blue-disk-on-table"],
        "delete": ["blue-disk-on-pole", "blue-disk-on-top"]
    },
    {
        "action": "Move red disk from pole to table",
        "preconds": ["red-disk-on-pole", "red-disk-on-top"],
        "add": ["red-disk-on-table"],
        "delete": ["red-disk-on-pole", "red-disk-on-top"]
    },
    {
        "action": "Move green disk from table to pole",
        "preconds": ["green-disk-on-table"],
        "add": ["green-disk-on-pole", "green-disk-on-top"],
        "delete": ["green-disk-on-table"]
    },
    {
        "action": "Move blue disk from table to pole",
        "preconds": ["blue-disk-on-table"],
        "add": ["blue-disk-on-pole", "blue-disk-on-top"],
        "delete": ["blue-disk-on-table"]
    },
    {
        "action": "Move red disk from table to pole",
        "preconds": ["red-disk-on-table"],
        "add": ["red-disk-on-pole", "red-disk-on-top"],
        "delete": ["red-disk-on-table"]
    }
gps(
    ["red-disk-on-pole", "blue-disk-on-pole", "green-disk-on-pole", "green-disk-on-top"],
    ["green-disk-on-pole", "blue-disk-on-pole", "red-disk-on-pole", "red-disk-on-top"],
    disk_ops
)
]
