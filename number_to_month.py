# Replace the "ANSWER HERE" for your answer
from google.genai.types import GenerationConfigRoutingConfig


def number_to_month(month):

    meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

    if month > 12 or month < 1:
        return "error"
    return meses[month -1]
