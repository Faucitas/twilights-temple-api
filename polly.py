import os
import sys
import subprocess
import boto3


# AWS Polly client setup
polly = boto3.Session().client('polly')


def polly_request(text):
    response = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Amy',
                                       Engine='neural')
    return response['AudioStream'].read()

# TODO use pydub to pitch shift audio
# https://batulaiko.medium.com/how-to-pitch-shift-in-python-c59b53a84b6d
