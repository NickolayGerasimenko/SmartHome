import os
import os.path

template_active_low = '''rule "Switch state of {0} Changed"
when
    Item {0} received update
then
    if({0}.state == ON)
        {1}.sendCommand(OFF)
    else
        {1}.sendCommand(ON)
end'''

template_active_high = '''rule "Switch state of {0} Changed"
when
    Item {0} received update
then
    if({0}.state == ON)
        {1}.sendCommand(ON)
    else
        {1}.sendCommand(OFF)
end'''

template2 = '''rule \"Contact state of {0} Changed\"
when
    Item {0} changed
then
    if({2}.state == ON)
        {1}.postUpdate(ON)
    else
        {1}.postUpdate(OFF)
end'''

#       I2C I/O Board addresses
#       
#       A2:A1:A0  Addr
#       --------------
#       
#       0 0 0       $20
#       0 0 1       $24
#       0 1 0       $22
#       1 0 0       $21
#       0 1 1       $26
#       1 1 0       $23
#       1 0 1       $25
#       1 1 1       $27



# k:v -> <I2C addr> : ( <relay active level>, <is_enabled> )
IO_Board_addresses = { '20' : ( 'ACTIVE_HIGH', True  ),
                       '24' : ( 'ACTIVE_HIGH', False ),
                       '22' : ( 'ACTIVE_HIGH', False ),
                       '21' : ( 'ACTIVE_LOW' , True  ),
                       '26' : ( 'ACTIVE_HIGH', False ),
                       '23' : ( 'ACTIVE_HIGH', False ),
                       '25' : ( 'ACTIVE_HIGH', False ),
                       '27' : ( 'ACTIVE_HIGH', False )
                     }

#MCP_Switch_20_A0
#MCP_Contact_20_B0
#MCP_VirtualSwitch_20_B0

items_template0 = '''
Switch MCP_VirtualSwitch_{0}_B{1} "Light {0}:{1}" (FF_Corridor, gLights)'''
items_template1 = '''
Switch MCP_Switch_{0}_A{1} "MCP_SW_{0}_A{1}" (FF_Corridor, gLights) {{ mcp23017="{{ address:{0}, pin:'A{1}', mode:'DIGITAL_OUTPUT', defaultState:'HIGH'}}" }}'''
items_template2 = '''
Contact MCP_Contact_{0}_B{1} "MCP_Cont_{0}_B{1}" (FF_Corridor, gWallButtons) {{ mcp23017="{{ address:{0}, pin:'B{1}', mode:'DIGITAL_INPUT'}}" }}'''

# generate item file
for k,v in IO_Board_addresses.items():
    board = k
    is_enabled = v[1]
    if is_enabled is True:
            items_filepath = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), 'items','MCP_Switch_{}.items'.format(board))
            print items_filepath
            with open(items_filepath, 'w') as f:
                for i in range(0,8):
                    f.write(items_template0.format(board,i))
                for i in range(0,8):
                    f.write(items_template1.format(board,i))
                for i in range(0,8):
                    f.write(items_template2.format(board,i))
                
for k,v in IO_Board_addresses.items():
    board = k
    is_enabled = v[1]
    if is_enabled is True:
        for i in range(0,8):
            filename = 'MCP_Switch_{}_A{}_{}.rules'.format(board,i,v[0])
            f = open(filename, 'w')
            template = template_active_high if v[0] == 'ACTIVE_HIGH' else template_active_low
            f.write(template.format('MCP_VirtualSwitch_{}_B{}'.format(board,i),'MCP_Switch_{}_A{}'.format(board,i), i))
            f.write("\r\n \r\n")
            f.write(template2.format('MCP_Contact_{}_B{}'.format(board,i),'MCP_VirtualSwitch_{}_B{}'.format(board,i),'MCP_Switch_{}_A{}'.format(board,i), i))