from models.llama import Llama

def create_llama():
    tina = Llama("Tina", "Fat Lard")
    return print(f'| {tina.name} the {tina.species} llama is walking on {tina.date_added} |')
