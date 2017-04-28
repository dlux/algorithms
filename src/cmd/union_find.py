import sys
from cliff import command
import logging

class UNIONFIND(command.Command):

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        import pdb;pdb.set_trace()
        method = 0 if len(parsed_args) == 0 else parsed_args[0]
        self.run(method)

    def get_parser(self, prog_name):
        parser = super(UNIONFIND, self).get_parser(prog_name)
        parser.add_argument('-a', '--algorithm',
                    choices=['quick_sort', 'quick_union',
                             'quick_union1', 'quick_union2'],
                    default='quick_sort',
                    help='Implemented algorithm.')
        return parser

    def get_description(self):
        return ("Implementation to solve union-find problem.")

    def run(self, method):
        if method == '1':
            # parameter is equals 1 - then use QUICK UNION
            self.log.info("Using QUICK UNION method - simple tree")
            from src.quick_union import QUICK_UNION as UF
        elif method == '2':
            # parameter is equals 2 - then use QUICK UNION OPTIMIZED
            self.log.info("Using QUICK UNION OPTIMIZED method - weighted tree")
            from src.quick_union import QUICK_UNION_OPTIMIZED as UF
        elif method == '3':
            # parameter is equals 2 - then use QUICK UNION OPTIMIZED
            self.log.info("Using QUICK UNION OPTIMIZED method - weighted tree & flatten")
            from src.quick_union import QUICK_UNION_OPTIMIZED_PATH_COMPRESSION as UF
        else:
            self.log.info("Using QUICK FIND method - simple array. DEFAULT METHOD")
            # Use QUICK FIND - DEFAULT
            from src.quick_find import QUICK_FIND as UF

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

        self.log.info(union_find_obj.get_connected_components())

if __name__ == "__main__":
    mm = UNIONFIND("","")
    mm.run(0)
