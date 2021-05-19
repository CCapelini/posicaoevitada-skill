from mycroft import MycroftSkill, intent_file_handler


class Posicaoevitada(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('posicaoevitada.intent')
    def handle_posicaoevitada(self, message):
        self.speak_dialog('posicaoevitada')


def create_skill():
    return Posicaoevitada()

