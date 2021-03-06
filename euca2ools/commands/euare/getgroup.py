# Software License Agreement (BSD License)
#
# Copyright (c) 2009-2011, Eucalyptus Systems, Inc.
# All rights reserved.
#
# Redistribution and use of this software in source and binary forms, with or
# without modification, are permitted provided that the following conditions
# are met:
#
#   Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the
#   following disclaimer.
#
#   Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the
#   following disclaimer in the documentation and/or other
#   materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Neil Soman neil@eucalyptus.com
#         Mitch Garnaat mgarnaat@eucalyptus.com

from boto.roboto.awsqueryrequest import AWSQueryRequest
from boto.roboto.param import Param
import euca2ools.commands.euare


class GetGroup(AWSQueryRequest):

    ServiceClass = euca2ools.commands.euare.Euare

    Description = """GetGroup"""
    Params = [Param(
        name='GroupName',
        short_name='g',
        long_name='group-name',
        ptype='string',
        optional=False,
        doc=""" Name of the group. """,
        ), Param(
        name='Marker',
        short_name='m',
        long_name='marker',
        ptype='string',
        optional=True,
        doc=""" Use this only when paginating results, and only in a subsequent request after you've received a response where the results are truncated. Set it to the value of the Marker element in the response you just received. """,
        ), Param(
        name='MaxItems',
        short_name=None,
        long_name='max-items',
        ptype='integer',
        optional=True,
        doc=""" Use this only when paginating results to indicate the maximum number of User names you want in the response. If there are additional User names beyond the maximum you specify, the IsTruncated response element is true. """ ,
        ), Param(
        name='DelegateAccount',
        short_name=None,
        long_name='delegate',
        ptype='string',
        optional=True,
        doc=""" [Eucalyptus extension] Use the parameter only as the system admin to act as the account admin of the specified account without changing to account admin's role. """,
        )]


    def cli_formatter(self, data):
        print data.Group['Arn']
        print '\tusers'
        for user in data.Users:
            print '\t%s' % user['Arn']
            
    def main(self, **args):
        self.list_markers.append('Users')
        self.item_markers.append('member')
        return self.send(**args)

    def main_cli(self):
        self.do_cli()
