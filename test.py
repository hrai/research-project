#!/usr/bin/env python2

import rospy
import magic_listen
import Levenshtein

rospy.init_node('demo')

index=0

file = open("questions.txt", "r")
for line in file:
    index=index+1
    question=line.lower().strip()
    print("Question " + str(index) + "- " + question)

    # call multilingual
    resp=magic_listen.multilingual_listen_raw('ne-NP')

    for translated_text_with_confidence in resp:
        translated_text=translated_text_with_confidence[0]
        print translated_text.lower() + ',' + str(Levenshtein.ratio(translated_text, question))
