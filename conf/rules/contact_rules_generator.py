template = '''rule "Switch Light LED{3} State Update"
when
    Item {0} received update

then
    if({0}.state == ON) {
        {1}.state = OFF
        {2}.postUpdate(OPEN)
    } else {
        {1}.state = ON
        {2}.postUpdate(CLOSED)
    }
end'''

str = template.format('Light_MCP23017Contact_B0','MCP23017Contact_B0_LED','MCP23017Contact_B0', 0)
print(str)

