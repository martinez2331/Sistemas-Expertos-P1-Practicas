

class BaseConocimiento:
    def __init__(self):
        self.conocimiento = {
            "Hola": "¡Hola! ¿En qué puedo ayudarte?",
            "Como estas?": "Estoy bien, gracias por preguntar. ¿Y tú?",
            "De que te gustaría hablar?": "Puedo hablar sobre una amplia variedad de temas. ¿Qué te interesa?"
        }

    def agregar_conocimiento(self, pregunta, respuesta):
        self.conocimiento[pregunta] = respuesta

    def buscar_respuesta(self, pregunta):
        if pregunta in self.conocimiento:
            return self.conocimiento[pregunta]
        else:
            return "Lo siento, no entiendo esa pregunta. ¿Podrías proporcionar más información para que pueda aprender?"

class ChatBot:
    def __init__(self):
        self.base_conocimiento = BaseConocimiento()

    def iniciar_conversacion(self):
        print("¡Hola! Soy un chatbot. ¿En qué puedo ayudarte?")
        while True:
            entrada_usuario = input("Usuario: ")
            respuesta = self.base_conocimiento.buscar_respuesta(entrada_usuario)
            print("ChatBot:", respuesta)
            if respuesta == "Lo siento, no entiendo esa pregunta. ¿Podrías proporcionar más información para que pueda aprender?":
                self.agregar_conocimiento_nuevo()
                continue  # Continuar la conversación después de agregar conocimiento nuevo

    def agregar_conocimiento_nuevo(self):
        pregunta_nueva = input("ChatBot: Por favor, ingresa la pregunta que deseas agregar a mi base de conocimiento: ")
        respuesta_nueva = input("ChatBot: Ahora, ingresa la respuesta a esa pregunta: ")
        self.base_conocimiento.agregar_conocimiento(pregunta_nueva, respuesta_nueva)
        print("¡Gracias por enseñarme algo nuevo!")

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.iniciar_conversacion()