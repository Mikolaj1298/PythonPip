
def save_bibtex(bibtexes):
    with open("bibtex.bib", "a") as myfile:
        for item in bibtexes:
            myfile.write(
                getBibtex(item) + '\n')

def getBibtex(item):
    bib = f'@author{{{self.pk},\n  author =\t"{self.authors}", \
        \n  title =\t"{self.title}",\n'
    bib = bib[0:len(bib)-1]+'\n}\n'
    return bib

