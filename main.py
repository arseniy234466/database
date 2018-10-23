from db import user_controller as uc

uc.add_user(user_id=1, user_name="test", first_name="alex", last_name="ivanov")

all_user = uc.get_all_users()


for users in all_user:
    print(users)