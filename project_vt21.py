
# Importing tools to open .gz-files and to work over directories,
# also importing regular expressions to try to remove unwanted strings.
import gzip
import os
import re

# The function returns which checks which Swedish words
# can have both neuters.                                                                      
def find_neuter():
    directory = 'home/example_dir/example_county.tag.gz'
    # Creating two lists to later compare.
    counties = {}

    # Inner function to create keys and count occurences.
    def create():
        # Looping over the sub-directories.
        for filename in os.listdir(directory):
            # This line might be unnecessary.
            county = filename.strip('.tag.gz')
            # Creating empty dicts to fill with sub-dicts and 
            # key-value pairs.
            county = {}
            neutrum = {}
            utrum = {}
            # Opening each file to access the texts.
            # 'File' is the coresponding county folder.
            with gzip.open(filename, 'rt') as file:
                for txt in file: 
                    # Formating the text, all lower makes most sense.
                    # Removing new rows and removing blank spaces.
                    name = filename.strip(' .tag.gz')
                    list = txt.strip('\n').lower().split(' ')
                    for item in list:
                        # Words and tags are seperated with '/'.
                        tupp = item.split('/')
                        # This is to avoid index error.
                        if len(tupp) < 2:      
                            continue
                        # This is handling the actual text, breaking it down to 
                        # tuples of two with the word and the part-of-speach tag.    
                        ord = tupp[0]
                        tag = tupp[1]
                        # Starting to handle the actual words.
                        # First checking if the word is a noun,
                        if 'nn' in tag:
                            # Trying to remove strings with non-alfanumericals
                            if ord == re.search('^\W*?', ord):
                                continue
                            else:
                                # only singular forms are wanted, so plural
                                # is skipped by continuing,
                                if 'pl' in tag:
                                        continue
                                else:
                                    # then checking if the word is in definate form,
                                    # where both neuters can occur. 
                                    if 'def' in tag:
                                        # Then checking neuter.
                                        if 'neu' in tag:
                                            # Removing the definite part of the word.
                                            neu = ord[:-2]
                                            # Matching with the wanted search word.
                                            if neu == srch:
                                                # Incrementing the value if the word exists as a key,
                                                # else, adding it as a key with '1' as value.
                                                if neu in neutrum:
                                                    neutrum[neu] = neutrum.get(neu) + 1
                                                else:
                                                    neutrum[neu] = 1
                                                    county['neutrum'] = neutrum
                                            else:
                                                continue
                                        elif 'utr' in tag:
                                            utr = ord[:-2]
                                            if utr == srch:
                                                if utr in utrum:
                                                    utrum[utr] = utrum.get(utr) + 1
                                                else:
                                                    utrum[utr] = 1
                                                county['utrum'] = utrum
                                            else:
                                                continue
                                        else:
                                            continue
                                    # Continuing to avoid other word-classes, like verbs.
                                    else:
                                        continue
                        else:
                            continue
                # Adding each county with the county name as a key,
                # and a sub-dict as value.
                counties[name] = county
            # Closing each folder, otherwise fails the for-loop. 
            file.close()
        return counties
    
    # Changing working directory.
    # The reason that I change the directory instead of concatenating
    # is that changing the working directory avoids FileNotFoundError.
    os.chdir(directory)
    # Promting user for word to find.
    srch = input('what word would you like to search for? ')
    # Calling the create function defined in lines 16-97.
    create()
    # Printing the dict of counties and results
    for k, v in counties.items():
        print(k, ':\t\t', v)
    # Closing the code.
    return
