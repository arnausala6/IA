# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    # The reward of reaching the goal state (+10) is so little compared to
    # the reward of negative terminal states (-100). Therefore, the risk of ending
    # up in a negative state must be very low for crossing the bridge to be 
    # worth it. This is obtained by lowering the noise value and ensuring that the agent
    # always takes the desired action (left or right).
    answer_discount = 0.9
    answer_noise = 0
    return answer_discount, answer_noise
    #This answer was given in the notebook. Additionally, we want to add that by
    #lowering the noise, we can make sure that the actions that we take end up
    #where we want, so we are now sure that there is no risk of falling over

def question3a():
    answer_discount = 0.3           #preferes immediate reward
    answer_noise = 0                #there is no risk near the cliff  
    answer_living_reward = 0        #preferes taking less steps
    return answer_discount, answer_noise, answer_living_reward

def question3b():
    answer_discount = 0.3           #preferes immediate reward
    answer_noise = 0.2              #there is risk near the cliff    
    answer_living_reward = 0.1      #preferes taking more steps
    return answer_discount, answer_noise, answer_living_reward

def question3c():
    answer_discount = 0.9           #preferes long-term reward
    answer_noise = 0                #there is no risk near the cliff 
    answer_living_reward = 0        #preferes taking less steps
    return answer_discount, answer_noise, answer_living_reward

def question3d():
    answer_discount = 0.9           #preferes long-term reward
    answer_noise = 0.2              #there is risk near the cliff 
    answer_living_reward = 0        #preferes taking less steps
    return answer_discount, answer_noise, answer_living_reward

def question3e():
    answer_discount = 1             #preferes long-term reward
    answer_noise = 0                #there is no risk near the cliff 
    answer_living_reward = 1        #will try to stay alive forever
    return answer_discount, answer_noise, answer_living_reward

def question8():
    
    #Even if the environment has no noise, the agent only learns about the high reward if it actually goes over the bridge. 
    #With just 50 episodes, there's still a decent chance it never really explores that path or it sticks to the safer one early on. 
    # Because of that, we can’t guarantee something like a 99% success rate just by picking some epsilon and learning rate, no matter how tie-breaking works.
    
    return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
