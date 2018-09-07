#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import argparse

urlcodificar = 'https://www.tulipantranslate.com/api/v1/message'
urldecodificar = 'https://www.tulipantranslate.com/api/v1/translate'


def codificar(mensaje, apodo):
    return json.loads(requests.post(urlcodificar, data={'from': apodo,
                      'message': mensaje}).text)['translation']


def decodificar(mensaje, apodo):
    return json.loads(requests.post(urldecodificar,
                      data={'from': apodo,
                      'translation': mensaje}).text)['content']


parser = argparse.ArgumentParser(description='CLI de Tulipan Translate')
parser.add_argument('--codificar', type=str, help='mensaje a codificar')
parser.add_argument('--decodificar', type=str,
                    help='mensaje a decodificar')

parser.add_argument('--apodo', type=str, help='apodo a utilizar')

args = parser.parse_args()
if args.apodo != None:
    if args.codificar != None:
        print ('Mensaje Traducido: ' + codificar(args.codificar,
                args.apodo))
    if args.decodificar != None:
        print ('Mensaje Original: ' + decodificar(args.decodificar,
                args.apodo))
