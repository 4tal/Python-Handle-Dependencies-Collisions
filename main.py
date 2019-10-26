import os
import subprocess
import sys


def create_new_dep_file(deps, remove):
    pass

def install_one_by_one(deps=[], initial_deps_to_install=[]):
    try:
        dup_deps = deps[:]

        for prob_dep in initial_deps_to_install:
            os.system(f'pip3 install {prob_dep}')

            if prob_dep in dup_deps:
                dup_deps.remove(prob_dep)

        for dep in dup_deps:
            print(f'Dep: {dep}')

            if dep is not '':

                output = subprocess.check_output(["pip3", f'install', f'{dep}'])
                try:
                    output = subprocess.check_output(["python3", "jose_test.py"])
                    if output.decode('ascii').rstrip() == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJ2YWx1ZSJ9.JPIDicqvQ6GAh14yE2yZ3wnZQ0LiLNTTRDtJgLZcn98':
                        print(f'Dep: {dep} Passed.\n')
                        f.write(f'Dep: {dep} Passed.\n')
                    # print(f'dep {dep} pass jose test')
                    print(f'\n\n\n')
                except Exception as e:
                    f.write(f'Dep: {dep}, error:{e}\n')
                    print(f'Dep: {dep}, error:{e}\n')
                    print(e)
                    sys.exit()
    except Exception as e:
        print(f'Exception {e}')



def delete():
    os.system('pip3 uninstall -r req.txt -y')
    # subprocess.check_output(["pip3", f'uninstall', '-r', 'req.txt', '-y'])
    os.system('pip3 uninstall python-jose==3.0.1')
    # subprocess.check_output(["pip3", f'uninstall', 'python-jose==3.0.1'])


def shuffle(deps):
    import itertools
    jwt_string = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJ2YWx1ZSJ9.JPIDicqvQ6GAh14yE2yZ3wnZQ0LiLNTTRDtJgLZcn98'

    indexes = range(0, len(deps))
    combinations = list(itertools.permutations(indexes, 3))
    print(combinations)

    for tupple in combinations:
        for number in tupple:
            output = subprocess.check_output(["pip3", f'install', f'{deps[number]}'])
            try:
                output = subprocess.check_output(["python3", "jose_test.py"])
                if output.decode('ascii').rstrip() == jwt_string:
                    f.write(f'Inner, array: {deps} ,dep: {deps[number]} Passed.\n')
                    print(f'Dep: {tupple} Passed.\n')
                print(f'\n\n\n')
            except Exception as e:
                # f.write(f'Tupple: {tupple} failed, error:{e}\n')
                print(f'Tupple: {tupple} failed, array:{deps}, dep:{deps[number]} error:{e}\n')
                print(e)



        try:
            output = subprocess.check_output(["python3", "jose_test.py"])
            if output.decode('ascii').rstrip() == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJ2YWx1ZSJ9.JPIDicqvQ6GAh14yE2yZ3wnZQ0LiLNTTRDtJgLZcn98':
                f.write(f'Outer, tuppel: {tupple} Passed.\n')
                print(f'Dep: {tupple} Passed.\n')
            print(f'\n\n\n')
        except Exception as e:
            f.write(f'Tupple: {tupple} failed, error:{e}\n')
            print(f'Tupple: {tupple} failed, error:{e}\n')
            print(e)

        delete()



def detect_malfanctioning_deps():
    deps = data.split(',')
    delete()
    install_one_by_one(deps=deps, initial_deps_to_install=prob_deps)
    os.system('python3 jose_test.py')


# create_new_dep_file()

if __name__ == '__main__':
    # TODO make it run on virtualEnv and not on global env.
    # TODO Automate the version searching by try and catch.
    # TODO Make the logs much more helpfull.

    with open('req.txt', 'r') as file:
        data = file.read().replace('\n', ',')

    f = open("output.log", "a")

    # First put here the lib that throws the error and then run it.
    # On the catch_the_malfunctioning_dep() you will find more problematic libs and then you can add them as well untill you find certain collision.

    prob_deps = []
    prob_deps.append('python-jose==3.0.1')
    # prob_deps.append('cryptography==2.6.1')
    # prob_deps.append('asn1crypto==1.0.0')


    detect_malfanctioning_deps()

    delete() #clear pip3 environment after previous installations.

    # After you find the problematic deps, throw it here. That function will try to install it in different order to see if something is successful.

    # shuffle(prob_deps)

    f.close()
    pass

