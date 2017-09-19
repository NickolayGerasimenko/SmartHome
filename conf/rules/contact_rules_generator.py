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

for i in range(0,8):
    f = open('MCP23017Contact_B{}.rules'.format(i), 'w')
    str = template.format('Light_MCP23017Contact_B{}'.format(i),'MCP23017Contact_B{}_LED'.format(i),'MCP23017Contact_B{}'.format(i), i)
    f.write(str)
