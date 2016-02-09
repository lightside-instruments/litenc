from optparse import OptionParser
usage="usage: %prog [options]"
parser = OptionParser(usage)
parser.add_option("-s", "--server", dest="server",
                      help="servername to use in the netconf session")
parser.add_option("-u", "--user", dest="user",
                      help="username to use in the netconf session")
parser.add_option("-p", "--password", dest="password",
                      help="password to use in the netconf session")
parser.add_option("-x", "--xpath", dest="xpath",
                      help="xpath pointing to the value of the leaf")

(options, args) = parser.parse_args()

import netconf
from netconf import netconf_xget_leaf_value

#host="123.456.789.123"
#user="root"
#password="blabla"
#xpath="/system/uptime"

my_netconf = netconf.netconf()
my_netconf.connect("server="+options.server+" port=830 user="+options.user+" password="+options.password)
(ret, reply_xml) = my_netconf.rpc("<hello>\
 <capabilities>\
   <capability>urn:ietf:params:netconf:base:1.0</capability>\
 </capabilities>\
</hello>")

(ret, value) = netconf_xget_leaf_value(my_netconf,options.xpath)
print value

my_netconf.terminate()

