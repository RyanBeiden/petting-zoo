from models.llama import Llama

def create_llama():
    tina = Llama("Tina", "Fat Lard", "morning")
    return print(f'| {tina.name} the {tina.species} llama is available to pet during the {tina.shift} shift. |')
