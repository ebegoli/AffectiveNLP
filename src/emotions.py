#!/usr/bin/env python
''' Collection of parrot_primary, secondary and tertiary emotions
'''
__author__ = 'Edmon Begoli'

parrot_primary = {}
secondary = {}

from nltk.corpus import wordnet as wn
from io import FileIO
from nltk import SnowballStemmer
from conceptnet import lookup_token



#For love
secondary['affection'] = ('adoration', 'affection', 'love', 'fondness', 'liking'
                          , 'attraction', 'caring', 'tenderness', 
                          'compassion', 'sentimentality')
secondary['lust'] = ('arousal', 'desire', 'lust', 'passion', 'infatuation')
secondary['longing'] = ('longing',)

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
secondary['relief'] = ('relief',)

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
secondary['torment'] = ('torment',)

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

def write_synsets(d, indent=0):
    ''' Function queries the 
    '''
    with open("parrot_synsets.txt", "w") as f:
      f.write( "total #primary:" + str(len(d)))      
      for prim, value in d.iteritems():
          prim_syns = wn.synsets( prim )
          prim_syns.sort()
          f.write( '\nprimary: ' + prim )
          f.write( '(# of secondary:' + str(len(value)) )
          f.write( ' # of synsets: ' + str(len(prim_syns)) + ')\n\t ')
          for syn in prim_syns:
            f.write(  str(syn) + "-" + syn.definition + "\n\t " )
          for sec, val in value.iteritems():
              sec_syns = wn.synsets( sec )
              sec_syns.sort()
              f.write( "\n\t\tsecondary:"  + sec ) 
              f.write( " (# of tertiary:" + str(len(val)) )
              f.write( " # of synsets:" + str(len(sec_syns)) + ")\n\t\t " )

              par_cycles = set(prim_syns) & set(sec_syns) 
              if (len(par_cycles)) > 0:
                f.write( ">>> cycles to parent " + str(par_cycles))

              for syn in sec_syns:
                f.write( str(syn) + "-" + syn.definition + "\n\t\t " )
              for ter in val: 
                ter_syns = wn.synsets( ter )
                ter_syns.sort()           
                par_cycles = set(ter_syns) & set(sec_syns) 
                gpar_cycles = set(ter_syns) & set(prim_syns) 

                if (len(par_cycles)) > 0:
                  f.write( ">>> cycles to parent " + str(par_cycles))
                if (len(gpar_cycles)) > 0:
                  f.write( ">>> cycles to grandparent " + str(gpar_cycles))

                f.write( '\n\t\t\ttertiary: ')
                f.write( ter + "(# of synsets: " +  str(len(ter_syns)) + ")\n\t\t\t " )
                for syn in ter_syns:
                    f.write( str(syn) + "-" + syn.definition + "\n\t\t\t ")




def get_emotions_list( indent=0 ):
    ''' Provides a unique, flattened list of parrot emotions
    '''  
    emotions = []
    for key, value in parrot_primary.iteritems():
        if key not in emotions:
           emotions.append( str(key) )
        for k, val in value.iteritems():
          if k not in emotions:
             emotions.append( str(k) )
          for em in val:   
             if em not in emotions:
                 emotions.append( str(em) )
    return emotions

def pretty_print( d, indent=0 ):
    '''
    '''
    for key, value in d.iteritems():
        print '\t' + key
        #print '\t' + str(value)
        for k, val in value.iteritems():
            print '\t\t' + k
            for em in val:
                print '\t\t\t' + em


def is_emotion( word, casesensitive=False ):
    ''' Looks up a word in the lists of emotions '''

    print lookup_token( "affection" )
    if casesensitive == False:
      word = word.lower()

    print word  

    if parrot_primary.has_key( word ):
      return True
    for prim, value in parrot_primary.iteritems():
          if value.has_key( word ):
             return True
          for sec, val in value.iteritems():
            if word in val:
              return True
              
    return False 




def main():
    #get_synsets( parrot_primary)
    stemmer = SnowballStemmer('english')
    print stemmer.stem( "affectionate" )

    print is_emotion( "affection" )
    print is_emotion( "Affection" ) 
    print is_emotion( "haha" )


if __name__ == "__main__":
    main()    
    
    