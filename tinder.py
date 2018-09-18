# -*- coding: UTF-8 -*-
import pynder
import variable

session = pynder.Session(facebook_id=variable.facebook_id, facebook_token=variable.facebook_auth_token)
session.update_location(variable.LAT, variable.LON)

print(session.profile)

users = session.nearby_users()

i = 0
for user in users:
    print('==名前=='),
    print(user.name)

    print('==年齢=='),
    print(user.age)

    print('==BIO=='),
    print(user.bio)

    print('==誕生日=='),
    print(user.birth_date)

    print('==最終ログイン時刻=='),
    print(user.ping_time)

    print('==距離=='),
    print(user.distance_km)

    print('==学校名=='),
    print(user.schools)

    print('==職業=='),
    print(user.jobs)

    print('==共通の友人数=='),
    print(len(user.common_connections))

    if user.common_connections == []: # 共通の知り合いがいるユーザーはLIKEしないようにしてます。
        user.like()
        print('LIKE!!!!!')

    print('==============================================================================')
    i += 1
    if i > 100:
        break
