import operator
import speech_recognition as sr
print("Your speech_recognition version is: "+sr.__version__)
r = sr.Recognizer()
my_mic_device = sr.Microphone(device_index=1)
with my_mic_device as source:
    print("Say what you want to calculate, example: 3 plus 3")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
my_string=(r.recognize_google(audio))
print(my_string)
def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'into' : operator.mul,
        'Into' : operator.mul,
        'divide by' :operator.__truediv__,
        'BY' :operator.__truediv__,
        'by' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        'power':operator.__pow__,
       
    }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

print(eval_binary_expr(*(my_string.split())))