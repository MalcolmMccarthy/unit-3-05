#By: Malcolm
#Calculates factorial
import ui

def factortial_button(sender):
	# calculates factorial
 input = int(view['input_textfield'].text)
 counter = 1
 answer = 1
 while(counter <= input):
        if counter <= input: 
            answer = answer * counter
            counter = counter + 1
            view['answer_label'].text = "{}".format(answer)
    



view = ui.load_view()
view.present('sheet')
