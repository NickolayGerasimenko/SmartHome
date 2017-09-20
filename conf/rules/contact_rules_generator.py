template = '''rule "Switch state of LED{2} Changed"
when
    Item {0} received update
then
    if({0}.state == ON)
        {1}.sendCommand(OFF)
    else
        {1}.sendCommand(ON)
end'''

template2 = '''rule \"Contact state of LED{3} Changed\"
when
    Item {0} changed
then
    if({2}.state == ON)
        {1}.postUpdate(ON)
    else
        {1}.postUpdate(OFF)
end'''

for i in range(0,8):
    f = open('MCP23017ContactB{}.rules'.format(i), 'w')
    str = template.format('MCP23017VirtualSwitchB{}'.format(i),'MCP23017ContactB{}_LED'.format(i), i)
    f.write(str)
    f.write("\r\n \r\n")
    str = template2.format('MCP23017ContactB{}'.format(i),'MCP23017VirtualSwitchB{}'.format(i),'MCP23017ContactB{}_LED'.format(i), i)
    f.write(str)