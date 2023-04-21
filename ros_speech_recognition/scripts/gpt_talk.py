#!/usr/bin/env python

import rospy
import rospkg
from sound_play.libsoundplay import SoundClient
import openai
from speech_recognition_msgs.msg import SpeechRecognitionCandidates

package_path = rospkg.RosPack().get_path('tmp_openai')
with open(package_path + '/cfg/openai_api.txt') as f:
    openai.api_key = f.read().replace('\n','')



class GPTChatNode(object):
    def __init__(self):
        self.sub = rospy.Subscriber(
            '/speech_to_text',
            SpeechRecognitionCandidates,
            self._sub_cb,
            queue_size=1
        )
        tts_action_name = rospy.get_param(
            '~tts_action_name', 'sound_play')
        self.sound_client = SoundClient(
            blocking=True,
            sound_action=tts_action_name,
        )
        self.conf_thresh = rospy.get_param('~confidence_threshold',0.8)

    def _sub_cb(self, msg):
        if len(msg.confidence) > 0:
            speech_conf = msg.confidence[0]
            if speech_conf < self.conf_thresh:
                return

        speech_text = msg.transcript[0]
        print(speech_text)
        prompt = speech_text
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            )
        reply_text = response["choices"][0]["text"].replace('\n','')
        print(reply_text)
        self.sound_client.say(
            reply_text,
        )


if __name__ == '__main__':
    rospy.init_node('gptchat_node')
    node = GPTChatNode()
    rospy.spin()
