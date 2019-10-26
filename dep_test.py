def test_dep(dep_name='default'):
    import jose
    try:
        from jose import jwt
    except Exception as e:
        print(e)
        # f.write(f'Dep: {dep_name}. Error:{e}')

    token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')
    return token

test_dep()