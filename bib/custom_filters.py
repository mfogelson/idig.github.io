def ieee_citation(entry):
    print(entry)
    # Example formatting for an article
    authors = ' and '.join(entry['author'].split(' and ')[:2]) + ', et al.' if ' and ' in entry['author'] else entry['author']
    title = entry['title']
    journal = entry['journal']
    volume = entry['volume']
    number = entry['number']
    pages = entry['pages']
    year = entry['year']
    
    return f"{authors}, \"{title},\" in {journal}, vol. {volume}, no. {number}, pp. {pages}, {year}."


from jinja2 import Environment
# from custom_filters import ieee_citation

# Assuming 'env' is your Jinja2 Environment
if __name__ == '__main__':
    env = Environment(...)
    env.filters['ieee_citation'] = ieee_citation
