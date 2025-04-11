import spacy

class Chatbot:
    def __init__(self):
        """
        Inicializa el Chatbot con respuestas predefinidas para preguntas relacionadas con contabilidad y las NIF.
        """
        self.responses = {
            "Enumere los elementos que integran el marco conceptual de la información financiera.": "Los elementos que integran el marco conceptual de la información financiera son: objetivos de la información financiera, características cualitativas de la información financiera, postulados básicos, elementos de los estados financieros y reconocimiento y valuación de los elementos de los estados financieros.",
            "enumere los elementos que integran el marco conceptual de la información financiera": "Los elementos que integran el marco conceptual de la información financiera son: objetivos de la información financiera, características cualitativas de la información financiera, postulados básicos, elementos de los estados financieros y reconocimiento y valuación de los elementos de los estados financieros.",
            "Mencione y explique brevemente las características básicas de la información financiera.": "Las características básicas de la información financiera son: confiabilidad (la información debe ser veraz y verificable), relevancia (debe ser útil para la toma de decisiones), comprensibilidad (debe ser clara y fácil de entender) y comparabilidad (debe permitir comparar información entre periodos y entidades).",
            "Explique qué función tienen los postulados básicos de la información financiera.": "Los postulados básicos de la información financiera son fundamentos que rigen el ambiente bajo el cual debe operar el sistema de información contable, asegurando que la información sea consistente y útil para la toma de decisiones.",
            "Indique cuáles son los postulados básicos de la información financiera.": "Los postulados básicos de la información financiera son: entidad económica, negocio en marcha, devengación contable, asociación de costos y gastos con ingresos, valuación, dualidad económica y consistencia.",
            "¿A qué se refiere el postulado de entidad económica?": "El postulado de entidad económica establece que las operaciones de una entidad son independientes de las de sus accionistas, propietarios o cualquier otra entidad.",
            "¿Qué establece el postulado de asociación de costos y gastos con ingresos?": "El postulado de asociación de costos y gastos con ingresos establece que los costos y gastos deben identificarse con el ingreso que generaron en el mismo periodo contable.",
            "¿Qué se entiende por devengación contable?": "La devengación contable establece que los efectos de las transacciones y eventos económicos deben reconocerse en el momento en que ocurren, independientemente de la fecha en que se realicen los cobros o pagos.",
            "¿Cuáles son los conceptos básicos de la información financiera?": "Los conceptos básicos de la información financiera incluyen: activo, pasivo, capital contable, ingresos, gastos, utilidad y pérdida.",
            "Explique los conceptos de activo, pasivo y capital.": "Un activo es un recurso controlado por una entidad del que se esperan beneficios económicos futuros. Un pasivo es una obligación presente de la entidad que resultará en una salida de recursos. El capital contable es el valor residual de los activos de la entidad después de deducir todos sus pasivos.",
            "Describa brevemente los conceptos de ingreso, gasto, utilidad y pérdida.": "Los ingresos son recursos que incrementan los beneficios económicos. Los gastos son decrementos en los beneficios económicos. La utilidad ocurre cuando los ingresos superan a los gastos, mientras que la pérdida ocurre cuando los gastos superan a los ingresos.",
            "¿Cuál es la ecuación contable básica?": "La ecuación contable básica es: Activo = Pasivo + Capital.",
            "¿Cuáles son los elementos que integran el capital contable?": "Los elementos que integran el capital contable son: capital social, utilidades retenidas y reservas.",
            "¿Cómo se determinan las utilidades retenidas?": "Las utilidades retenidas se determinan sumando la utilidad neta del periodo a las utilidades acumuladas de periodos anteriores, menos los dividendos distribuidos.",
            "¿Cómo se calcula la utilidad neta del periodo?": "La utilidad neta del periodo se calcula restando los gastos totales (incluyendo costos operativos, impuestos y otros gastos) de los ingresos totales. La fórmula es: Utilidad Neta = Ingresos Totales - Gastos Totales.",
            "Liste los estados financieros básicos y especifique el objetivo de cada uno.": "Los estados financieros básicos son: 1) Balance General: muestra la situación financiera de la entidad en un momento determinado. 2) Estado de Resultados: muestra los ingresos, costos y gastos para determinar la utilidad o pérdida del periodo. 3) Estado de Cambios en el Capital Contable: muestra los movimientos en el capital contable durante el periodo. 4) Estado de Flujo de Efectivo: muestra las entradas y salidas de efectivo clasificadas en actividades operativas, de inversión y de financiamiento."
        }
        self.greetings = {
            "hola": "¡Hola! ¿En qué puedo ayudarte hoy?",
            "buenos días": "¡Buenos días! ¿Cómo puedo asistirte?",
            "buenas tardes": "¡Buenas tardes! ¿En qué puedo ayudarte?",
            "buenas noches": "¡Buenas noches! ¿Cómo puedo asistirte?"
        }

        self.intent_questions = {
            "quiero hacer una pregunta": "¡Claro! Dime tu pregunta y trataré de responderla lo mejor posible."
        }

        self.thank_you_responses = {
            "gracias": "¡De nada! Si tienes más preguntas, no dudes en decírmelo.",
            "muchas gracias": "¡Con gusto! Estoy aquí para ayudarte."
        }

        self.generic_response = "Entendido. Si tienes una pregunta específica, no dudes en decírmelo."

    def chat(self, user_input):
        """
        Maneja la interacción del chat continuo con el usuario.
        """
        if not user_input.strip():
            return "Por favor, escribe algo para continuar."

        normalized_input = user_input.lower().strip()

        # Priorizar saludos
        if normalized_input in self.greetings:
            return self.greetings[normalized_input]

        # Manejar intención de hacer una pregunta y esperar una pregunta predefinida
        if normalized_input in self.intent_questions:
            self.awaiting_question = True
            return self.intent_questions[normalized_input]

        # Responder a una pregunta predefinida si se está esperando una
        if getattr(self, 'awaiting_question', False):
            self.awaiting_question = False
            if normalized_input in self.responses:
                return self.responses[normalized_input]
            else:
                return "No tengo una respuesta exacta para eso, pero puedo ayudarte a buscar más información si lo necesitas."

        # Normalizar las claves de las respuestas predefinidas
        normalized_responses = {key.lower().strip(): value for key, value in self.responses.items()}

        # Manejar agradecimientos
        if normalized_input in self.thank_you_responses:
            return self.thank_you_responses[normalized_input]

        # Verificar si la entrada coincide con una pregunta predefinida normalizada
        if normalized_input in normalized_responses:
            return normalized_responses[normalized_input]

        # Respuesta genérica para entradas no reconocidas
        return self.generic_response

    def ask_question(self, question):
        """
        Responde a la pregunta proporcionada si está predefinida, o indica que no tiene una respuesta.
        """
        if not question.strip():
            return "Por favor, haz una pregunta válida."

        # Buscar respuesta predefinida
        response = self.responses.get(question)
        if response:
            return response

        # Respuesta alternativa si no se encuentra una respuesta predefinida
        return "No tengo una respuesta exacta para eso, pero puedo ayudarte a buscar más información si lo necesitas."