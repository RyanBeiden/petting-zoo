from models.spider import Spider

def create_spider():
    satan = Spider("Satan", "Scary & Gross")
    return print(f'| {satan.name} the {satan.species} spider is slithering on {satan.date_added} |')
