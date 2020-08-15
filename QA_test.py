import os
from pocketsphinx import LiveSpeech
from module import module_pico
from module import module_beep

qa_dict = {}
with open('dictionary/QandA/QandA.txt', 'r') as f:
    qa_list = f.readlines()
    print("----------question list-----------")
    for qa in qa_list:
        qa = qa.rstrip().split(',')
        qa_dict[str.lower(qa[0])] = qa[1]
        print(str.lower(qa[0]))
    print("----------question list-----------\n")
# Define path
file_path = os.path.abspath(__file__)
test_dic_path = file_path.replace(
    '/QA_test.py', '/dictionary/QA_sample.dict')
test_gram_path = file_path.replace(
    '/QA_test.py', '/dictionary/QA_sample.gram')

def QandA():
    while True:
        question = recognition()
        print("----------------------------------\n", question, "?")
        module_pico.speak(qa_dict[question])
        print("----------------------------------\n")

def recognition():

    ###############
    #
    # test pocketsphinx with dictionary
    #
    # param >> None
    #
    # return >> None
    #
    ###############

    global live_speech
    print('[*] START RECOGNITION')
    setup_live_speech(False, test_dic_path, test_gram_path, 1e-20)

    module_beep.beep("start")
    for phrase in live_speech:
        noise_words = read_noise_word(test_gram_path)
        if str(phrase) == "":
            pass
        elif str(phrase) not in noise_words:
            module_beep.beep("stop")
            return str(phrase)

        # noise
        else:
            #print(".*._noise_.*.")
            pass


# setup livespeech
def setup_live_speech(TF, dict_path, jsgf_path, kws_threshold):

    ###############
    #
    # use this module to set live espeech parameter
    #
    # param >> lm: False >> means useing own dict and gram
    # param >> dict_path: ~.dict file's path
    # param >> jsgf_path: ~.gram file's path
    # param >> kws_threshold: mean's confidence (1e-○)
    #
    # return >> None
    #
    ###############

    global live_speech
    live_speech = LiveSpeech(lm=TF,
                             dic=dict_path,
                             jsgf=jsgf_path,
                             kws_threshold=kws_threshold
                             )

def read_noise_word(gram_path):

    ###############
    #
    # use this module to put noise to list
    #
    # param >> gram_path: grammer's path which you want to read noises
    #
    # return >> words: list in noises
    #
    ###############

    words = []
    with open(gram_path) as f:
        for line in f.readlines():
            if "<noise>" not in line:
                continue
            if "<rule>" in line:
                continue
            line = line.replace("<noise>", "").replace(
                    " = ", "").replace("\n", "").replace(";", "")
            words = line.split(" | ")
    return words

if __name__ == '__main__':
    QandA()