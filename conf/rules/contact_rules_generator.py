template = '''rule \"Switch Light LED{3} State Update\"
when
    Item {0} received update

then
    if({0}.state == ON) {{
        {1}.state = OFF
        {2}.postUpdate(OPEN)
    }} else {{
        {1}.state = ON
        {2}.postUpdate(CLOSED)
    }}
end'''

template2 = '''rule \"Contact state of LED{2} Changed\"
when
    Item {0} changed

then
    if({0}.state == OPEN) {{
        {1}.sendCommand(ON)
    }} else {{
        {1}.sendCommand(OFF)
    }}
end'''

for i in range(0,8):
    f = open('MCP23017ContactB{}.rules'.format(i), 'w')
    str = template2.format('MCP23017ContactB{}'.format(i),'MCP23017ContactB{}_LED'.format(i), i)
    f.write(str)
