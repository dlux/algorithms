import sys

from cliff import app
from cliff import commandmanager
import logging


class Main(app.App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(Main, self).__init__(
            description='Dlux CLI to run algorithm implementations',
            version='1.0.0',# sys.modules.items() module.__version__
            command_manager=commandmanager.CommandManager('dlux_alg.cm'),
            deferred_help=True,
            )

    def initialize_app(self, argv):
        self.log.debug('dlux_alg initialize_app')

    def prepare_to_run_command(self, cmd):
        self.log.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.log.debug('dlux_alg clean_up %s', cmd.__class__.__name__)
        if err:
            self.log.debug('dlux_alg got an error: %s', err)


def main(argv=sys.argv[1:]):
    the_app = Main()
    return the_app.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
