from scholarly import scholarly


def save_csv():
    _file = open("output.csv", "w+")
    search_query = scholarly.search_author("Mayken Espinoza-Andaluz")
    author = scholarly.fill(next(search_query))
    _file.write("title|authors|year|abstract\n")
    for pub in author["publications"]:

        title = pub["bib"]["title"]
        year = pub["bib"]["pub_year"]
        abstract = pub["bib"]["title"]
        _file.write(f"{title}|{authors}|{year}|{abstract}\n")
    _file.close()


save_csv()
