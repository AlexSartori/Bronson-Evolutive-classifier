# Bronson, the evolutive classifier #
Humans are not perfect, and neither are machines.

---

## Intro ##
A classifier is a program that learns to label inputs based on their features. These features are pre-defined by a human, and therefore they cannot be perfect.

###### Here's an example: ######
Say we have a list of male and female names, and we want a computer to learn to give them the correct label ('male' or 'female'). We first define a so-called featureset, a group of properties used to predict an input's label. As an example we could use a name's last letter:

    featureset(name):
        name.lastletter

We then create a classifier and train it so that it will create its statistical data such as:

    classifier.train(train_names)

    last-letter = 'a'      female : male    =  37.8 : 1.0
    last-letter = 'k'        male : female  =  31.6 : 1.0
    last-letter = 'f'        male : female  =  21.0 : 1.0
    last-letter = 'i'      female : male    =   4.1 : 1.0

Meaning that if a name ends with letter 'a' it is 37.8 times more probable that it will be a female one. However, its accuracy is not satisfying, around 75%. (In 100 names, 75 are correctly guessed).

Next step is to think of a better featureset, to include more data for the classifier to work on.

## A better classifier ##
There is an infinte set of possible featuresets, combinations of basic properties: last-letter, last-3-letters, first-3-letters, length of the name, number of vowels and so on.

As you'll see, none of them will be perfect:

    features['last-letter'] = name[-1]
    features['first-letter'] = name[0]
    features['v_count'] = sum(name.lower().count(l) for l in 'aeiou')   # Vowels count

    Accuracy: 78.4%
&nbsp;

    features['last-3'] = name[-3:]
    features['first-3'] = name[:3]
    features['length'] = len(name)
    features['v_count'] = sum(name.lower().count(l) for l in 'aeiou')

    Accuracy: 81.6%
&nbsp;


    for l in "abcdefghjklmnopqrstuvwxyz":
        features['count %s' % l] = name.lower().count(l)    # How many of each letter in the name

    Accuracy: 69.8%

As you can see they can get better, but none of the human thinkable featuresets will ever be able to reach the perfection. So what's the solution when a human brain is not enough?

## When humans need help ##
Solution is: computers. Stupid ones when it's about only processing data, intelligent ones when the thing is about learning and evolution.

###### The idea I got ######
A possible solution could have been to try out every combination in the word, but it did not seem a smart solution. What it was is instead an algorithm that creates a group of classifiers with random featuresets and keeps mixing the good ones.

The concept is, 100 random classifiers get created and once they've all been tested, the 50 most accurate are kept. For each one of them a second classifier is chosen and a new one is generated with a combination of these two's genes (features) with possible mutations. This will generate other 50 classifiers, made up with the best pieces of the previous generation!

Now the process is repeated, and again the worst half is replaced with combinations of the best ones. This will, in the end, create the perfect combination, capable of getting 100% of names right!

## Too easy, Alex ##

    Average accuracy for generation #1:  69.4%
    Average accuracy for generation #2:  73.7%
    ...
    Average accuracy for generation #18: 83.0%

Great! It's evolving! Will it reach 100%?

Nope:

![Figure_3](http://codiceloco.altervista.org/services/usercontent/chart_1.png)

It has done an amazing job for the first 10-15 generations but then... There was no feature combination that could do best than the previous, even if features where selected by "Natural Selection".

## Conclusion ##
As everything related to humans, this poor irrational thinking thing, names do not have a set of specific rules to define their gender.

If humans used rules like "Female names must end with `A` and male ones with `K`" a program to label such strings would be no more complex than a "Hello World".

Unfortunately, Natural Language is intrinsically ambiguous, and to make computers capable of processing such data there's a whole Artificial Intelligence branch dedicated to its research, called Natural Language Processing.

Perfection is never reached because no matter how extensive a feature set is, **there will always be an exception to that rule**: resuming the previous example where K-ending names are supposed to be male, Brook is not.

If you're interested on the code, here's another file explaining it in detail: [CODE_DOC.md](#)

*Alex Sartori*
