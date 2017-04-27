import sys


def main(method):
    if method == '1':
        # parameter is equals 1 - then use QUICK UNION
        print("Using QUICK UNION method - simple tree")
        from quick_union import QUICK_UNION as UF
    elif method == '2':
        # parameter is equals 2 - then use QUICK UNION OPTIMIZED
        print("Using QUICK UNION OPTIMIZED method - weighted tree")
        from quick_union import QUICK_UNION_OPTIMIZED as UF
    elif method == '3':
        # parameter is equals 2 - then use QUICK UNION OPTIMIZED
        print("Using QUICK UNION OPTIMIZED method - weighted tree & flatten")
        from quick_union import QUICK_UNION_OPTIMIZED_PATH_COMPRESSION as UF
    else:
        print("Using QUICK FIND method - simple array. DEFAULT METHOD")
        # Use QUICK FIND - DEFAULT
        from quick_find import QUICK_FIND as UF

    # Ask for the number of objects ti create
    my_objs = input("Enter how many objects exists: ")

    # Create unionFind object
    union_find_obj = UF(int(my_objs))

    # Ask for pair of objects to join their groups
    while True:
        pair = input('Type two numbers separatade by a comma: ')
        if pair:
            pair = pair.split(',')
            union_find_obj.union(int(pair[0]), int(pair[1]))
        else:
            break

    print(union_find_obj.get_connected_components())


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    args = sys.argv[1:]
    method = 0 if len(args) == 0 else args[0]
    main(method)
