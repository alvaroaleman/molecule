#  Copyright (c) 2015-2016 Cisco Systems, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import click

from molecule import util
from molecule.command.v2 import base


class Converge(base.Base):
    def execute(self):
        """
        Execute the actions necessary to perform a `molecule converge` and
        return a tuple.

        :return: Return a tuple of (`exit status`, `command output`), otherwise
         exit on command failure.
        """
        print self.args
        print self.command_args
        return (0, None)


@click.command()
@click.option('--driver', default=None, help='Specificy a driver.')
@click.pass_context
def converge(ctx, driver):  # pragma: no cover
    """ Provisions all instances defined in molecule.yml. """
    command_args = {'driver': driver, }

    c = Converge(ctx.obj.get('args'), command_args)
    exit_code, command_output = c.execute()
    util.sysexit(exit_code)
