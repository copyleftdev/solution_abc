# Generate sample log
import uuid
import string
import random
import unittest


# creating a list to store generated actions, users_ids
actions = []
users = []

####################################
# Stores all log records
records = []
####################################

# Creating  Action list
for char in string.ascii_uppercase:
    actions.append(char)

# random number
number_of_users = random.randint(1,999)

# Creating user UUID and append to users list
for x in range(number_of_users):
    users.append(uuid.uuid4())

for u in users:
    user_record = {}
    user_record["user"] = str(u) # casting to string
    user_record['action'] = random.choice(actions) # Injecting Random uuid
    records.append(user_record) # Appending all records created

# injecting the usecase that will trigger the issue
static_records1 = [{"user": "1","action":"A"},
                  {"user": "1","action":"B"},
                  {"user": "1","action":"C"} ]

static_records2 = [{"user": "4","action":"A"},
                  {"user": "4","action":"B"},
                  {"user": "4","action":"C"} ]

static_records3 = [{"user": "8","action":"C"},
                  {"user": "8","action":"B"},
                  {"user": "8","action":"A"} ]
for each_s_record in static_records1:
    records.append(each_s_record)
for each_s_record in static_records2:
    records.append(each_s_record)
for each_s_record in static_records3:
    records.append(each_s_record)

# End of usecase injection

# List to store users/action details
a_steps  = []
b_steps  = []
c_steps = []



# Loginc to append to lists above depending on the action
for r in records:
    if r['action'] == 'A':
        a_steps.append(r['user'])
    if r['action'] == 'B':
        b_steps.append(r['user'])
    if r['action'] == 'C':
        c_steps.append(r['user'])

def detect_a_b_c():
    # Logic to return 1, 4 , 8 with users that have triggered A->B->C
    affected_users = []
    for u in records:
        if u['user'] in a_steps and u['user'] in  b_steps and u['user'] in c_steps:
            affected_users.append(u)

    return affected_users


class TestABC(unittest.TestCase):

    def test_users_1_4_8_return(self):
        test_date = records
        collected_records = detect_a_b_c()
        desired_result =[{'action': 'A', 'user': '1'},
         {'action': 'B', 'user': '1'},
         {'action': 'C', 'user': '1'},
         {'action': 'A', 'user': '4'},
         {'action': 'B', 'user': '4'},
         {'action': 'C', 'user': '4'},
         {'action': 'C', 'user': '8'},
         {'action': 'B', 'user': '8'},
         {'action': 'A', 'user': '8'}]
        self.assertEquals(collected_records, desired_result)


if __name__ == '__main__':
    unittest.main()
