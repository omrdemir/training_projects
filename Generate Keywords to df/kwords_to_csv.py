import pandas as pd

words = ['buy', 'prices', 'sale', 'cheap']


products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

keywords_list = []


for product in products:
    for word in words:
    
        keywords_list.append([product, product.upper() + ' ' + word.upper()])
        keywords_list.append([product, word.upper() + ' ' + product.upper()])
        
#print(keywords_list)


keywords = pd.DataFrame(keywords_list, columns=['Products', 'Keyword'])

print(keywords)


keywords['Campaign'] = 'SEM_Sofas'


keywords['Criterion Type'] = 'Exact'


keywords.to_csv('keywords.csv', index=False)