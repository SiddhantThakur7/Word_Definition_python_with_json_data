# Word_Definition_python_with_json_data
Takes input a word and returns its definition. uses similarity index to find the correct word even if misspelled and gives option for confirmation.

using the file data.json to use the parsed input and return the definition.

for word similarity and misspelled rectification facilities, difflib library is used.

the get_close_matches of difflib library gives the nearest neighbours to the misspelled word and the maximum similar is considered.
