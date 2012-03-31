#!/usr/bin/env python
''' Collection of parrot_primary, secondary and tertiary emotions
'''
__author__ = 'Edmon Begoli'

parrot_primary = {}
secondary = {}

from nltk.corpus import wordnet as wn


#For love
secondary['affection'] = ('adoration', 'affection', 'love', 'fondness', 'liking'
                          , 'attraction', 'caring', 'tenderness', 
                          'compassion', 'sentimentality')
secondary['lust'] = ('arousal', 'desire', 'lust', 'passion', 'infatuation')
secondary['longing'] = ('longing')

parrot_primary['love'] = dict( (i,secondary[i]) for i in ('affection', 'lust',
                                                           'longing') )

#For joy
secondary['cheerfulness'] = ('amusement', 'bliss', 'cheerfulness', 'gaiety', 
                             'glee', 'jolliness', 'joviality', 'joy', 'delight', 
                             'enjoyment', 'gladness', 'happiness', 'jubilation', 
                             'elation', 'satisfaction', 'ecstasy', 'euphoria')
secondary['zest'] = ('enthusiasm', 'zeal', 'zest', 'excitement', 'thrill', 
                     'exhilaration')
secondary['contentment'] = ( 'contentment', 'pleasure' )
secondary['pride'] = ('pride', 'triumph')
secondary['optimism'] = ('eagerness', 'hope', 'optimism')
secondary['enthrallment'] = ('enthrallment', 'rapture')
secondary['relief'] = ('relief')

parrot_primary['joy'] = dict( (i,secondary[i]) for i in ('cheerfulness',
                                                         'zest', 'contentment', 
                   'pride','optimism','enthrallment','relief') )


#For surprise
secondary['surprise'] = ('amazement', 'surprise', 'astonishment' )

parrot_primary['surprise'] = {'surprise':secondary['surprise'] } 

#For anger
secondary['irritation'] = ('aggravation', 'irritation', 'agitation', 
                           'annoyance', 'grouchiness', 'grumpiness')
secondary['exasperation'] = ( 'exasperation', 'frustration')
secondary['rage'] = ( 'anger', 'rage', 'outrage', 'fury', 'wrath', 'hostility', 
                      'ferocity', 'bitterness', 'hate', 'loathing', 'scorn', 
                      'spite', 'vengefulness', 'dislike', 'resentment' )
secondary['disgust'] = ( 'disgust', 'revulsion', 'contempt' )
secondary['envy'] = ( 'envy', 'jealousy' )
secondary['torment'] = ('torment')

parrot_primary['anger'] = dict( (i,secondary[i]) for i in ('irritation',
                               'exasperation', 'rage',
                               'disgust','envy','torment') )

#For sadness
secondary['suffering'] = ( 'agony', 'suffering', 'hurt', 'anguish' )
secondary['sadness'] = ( 'depression', 'despair', 'hopelessness', 'gloom', 
                         'glumness', 'sadness', 'unhappiness', 'grief', 'sorrow'
                         , 'woe', 'misery', 'melancholy')
secondary['disappointment'] = ( 'dismay', 'disappointment', 'displeasure' )
secondary['shame'] = ( 'guilt', 'shame', 'regret', 'remorse' )
secondary['neglect'] = ( 'alienation', 'isolation', 'neglect', 'loneliness', 
                         'rejection', 'homesickness', 'defeat', 'dejection', 
                         'insecurity', 'embarrassment', 'humiliation', 'insult')
secondary['sympathy'] = ( 'pity', 'sympathy' )

parrot_primary['sadness'] = dict( (i,secondary[i]) for i in ('suffering', 'sadness', 
                       'disappointment', 'shame','neglect','sympathy') )

#For fear
secondary['fear'] = ( 'horror', 'alarm', 'shock', 'fear', 'fright', 'horror', 
                      'terror', 'panic', 'hysteria', 'mortification' )
secondary['nervousness'] = ( 'anxiety', 'nervousness', 'tenseness', 'uneasiness', 
                             'apprehension', 'worry', 'distress', 'dread' )

parrot_primary['fear'] = dict( (i,secondary[i]) for i in ('fear', 'nervousness') )

def pretty(d, indent=0):
    for key, value in d.iteritems():
        print '\t' + key
        #print '\t' + str(value)
        for k, val in value.iteritems():
            print '\t\t' + k
            for em in val:
                print '\t\t\t' + em
def main():
    pretty( parrot_primary)
    
if __name__ == "__main__":
    main()    
    
    