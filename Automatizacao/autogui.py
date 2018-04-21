import pyautogui

#Tamanho da tela
##print(pyautogui.size())

#Posição do mouse
##print(pyautogui.position())


#Move o ponteiro para uma coordenada
##pyautogui.moveTo(10,10,duration=1)#(x,y,duration = )
##pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)#move de acordo com a localização do mouse atual
##pyautogui.dragTo(10,10, button='right')#clica na posição atual e arrasta até o local dado
                                    ##>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
                                    ##>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
                                    ##>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
                                    ##>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
                                    ##>>> pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end

#clicks
##pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')#click completo
##pyautogui.rightClick(563,696)#Click
##pyautogui.doubleClick(563,696)#Duplo click
##pyautogui.click(1163,8)#Click direito

#teclas
##pyautogui.hotkey('win'+'d')#infinitas teclas ao mesmo tempo
##pyautogui.press('esc')#preciona uma tecla ou uma [lista de teclas]
##pyautogui.KEYBOARD_KEYS#todas as teclas disponiveis
##pyautogui.typewrite("Bhishan", interval=0.1)#escreve um texto com uma velocidade de 0.1 por tecla

#MENSAGENS
##pyautogui.alert(text='', title='', button='OK')#Alerta
##pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])
##pyautogui.prompt(text='', title='' , default='')
##pyautogui.password(text='', title='', default='', mask="*")

##pyautogui.screenshot()#print screen

##pyautogui.keyDown('ctrl')#preciona
##pyautogui.keyUp('esc')#solta



