import os
import subprocess
import sys

# Move to .ENV
JWT_EXAMPLE = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJrZXkiOiJ2YWx1ZSJ9.JPIDicqvQ6GAh14yE2yZ3wnZQ0LiLNTTRDtJgLZcn98'
FAILED_DEP = 'python-jose==3.0.1'

def dep_file_from_subset(deps_array, deps_to_remove_array):
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

                output = subprocess.check_output(['pip3', 'install', '{dep}'])
                try:
                    output = subprocess.check_output(["python3", "dep_test.py"])
                    if output.decode('ascii').rstrip() == JWT_EXAMPLE:
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


def remove_deps_from_local_env():
    os.system(f'pip3 uninstall -r req.txt -y')
    os.system(f'pip3 uninstall {FAILED_DEP}')


def shuffle(deps):
    import itertools

    indexes = range(0, len(deps))
    order_options = list(itertools.permutations(indexes, 3))

    for order in order_options:
        for number in order:
            output = subprocess.check_output(['pip3', 'install', f'{deps[number]}'])
            try:
                output = subprocess.check_output(['python3', 'dep_test.py'])
                if output.decode('ascii').rstrip() == JWT_EXAMPLE:
                    f.write(f'Inner, array: {deps} ,dep: {deps[number]} Passed.\n')
                    print(f'Dep: {order} Passed.\n')
                print(f'\n\n\n')
            except Exception as e:
                print(f'Tupple: {order} failed, array:{deps}, dep:{deps[number]} error:{e}\n')
                print(e)

        try:
            output = subprocess.check_output(['python3', 'dep_test.py'])
            if output.decode('ascii').rstrip() == JWT_EXAMPLE:
                f.write(f'Outer, tuppel: {order} Passed.\n')
                print(f'Dep: {order} Passed.\n')
            print(f'\n\n\n')
        except Exception as e:
            f.write(f'Tupple: {order} failed, error:{e}\n')
            print(f'Tupple: {order} failed, error:{e}\n')
            print(e)

        remove_deps_from_local_env()


def detect_malfanctioning_deps(mal_deps):
    deps = data.split(',')
    remove_deps_from_local_env()
    install_one_by_one(deps=deps, initial_deps_to_install=mal_deps)
    os.system('python3 dep_test.py')


if __name__ == '__main__':
    # TODO make it run on virtualEnv and not on global env.
    # TODO Automate the version searching by try and catch.
    # TODO Make the logs much more helpfull.
    # TODO Add .env
    # TODO On shuffle function try to execute only if base dep installed.

    with open('req.txt', 'r') as file:
        data = file.read().replace('\n', ',')

    f = open("output.log", "a")

    # First put here the lib that throws the error and then run it.
    # On the catch_the_malfunctioning_dep() you will find more mal libs
    # and then you can add them as well untill you find certain collision.

    mal_deps = []
    mal_deps.append(FAILED_DEP)

    # prob_deps.append('cryptography==2.6.1')
    # ... Add much as you need.

    detect_malfanctioning_deps(mal_deps=mal_deps)

    remove_deps_from_local_env()

    # After you find the mal deps, throw it here. That function will try to
    # install it in different order to see if something is successful.


    # shuffle(prob_deps) -

    f.close()
    pass

