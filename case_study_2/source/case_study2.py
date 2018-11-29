import random

def randomPhrase(buzz,adj,adv,verbs):
    
    r_buzz = random.sample(buzz,2)
    r_adj = random.sample(adj,1)
    r_adv = random.sample(adv,1)
    r_verbs = random.sample(verbs,1)
                    
    phrase = r_adj[0]+" "+r_buzz[0]+" and "+r_buzz[1]+" "+r_verbs[0]+" "+r_adv[0]

    return phrase


if __name__ == "__main__":

    buzz = ('continuous testing', 'continuous integration','continuous deployment','continuous improvement', 'devops')
    adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
    adverbs = ('remarkably', 'enormously', 'substantially', 'significantly','seriously')
    verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')

    gen_phrase = randomPhrase(buzz,adjectives,adverbs,verbs)
    print(gen_phrase)
    
    
