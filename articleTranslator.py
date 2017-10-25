"""
Replaces words in a string with dictionary words
"""
def main():
    sub = {}
    words = ''
    paragraph = []
    print("This program translates articles into more legible English.\nEnter the \"best\" word and its list of synonyms. Type \"quit\" to end input.")

    words = str(input(""))
    while words != 'quit':
        synonyms = words.split()
        x = synonyms[0]
        del synonyms[0]
        sub.update({synonyms[i]:x for i in range(0,len(synonyms))})
        words = str(input(""))

    print("\nEnter the article one line at a time. Type \"quit\" to end input.")
    articleLine = str(input(""))
    while articleLine != 'quit':
        article = articleLine.split()
        for i in range(0, len(article)):
            if str(article[i]) in sub:
                    article[i] = sub[article[i]]
        modified = ' '.join(str(e) for e in article)
        paragraph.append(modified)
        articleLine = str(input(""))
    
    print("\nThe modified article is as follows:")
    for i in paragraph:
        print(i)
main()
