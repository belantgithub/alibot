# -*- coding: utf8 -*-

import json
import logging
import re

import telepot
from django.template.loader import render_to_string
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings

TelegramBot = telepot.Bot(settings.TELEGRAM_BOT_TOKEN)

logger = logging.getLogger('telegram.bot')


def _display_help():
    return render_to_string('help.md')


def _start_bot():
    return render_to_string('start.md')


def _add_razbor_message():
    return render_to_string('add.md')


# def _display_planetpy_feed():
#     return render_to_string('feed.md', {'items': parse_planetpy_rss()})


class CommandReceiveView(View):
    def post(self, request, bot_token):
        if bot_token != settings.TELEGRAM_BOT_TOKEN:
            return HttpResponseForbidden('Invalid token')

        commands = {
            '/start': _display_help,
            '/add': _add_razbor_message,
            '/help': _display_help,
        }

        raw = request.body.decode('utf-8')
        logger.info(raw)

        try:
            payload = json.loads(raw)
        except ValueError:
            return HttpResponseBadRequest('invalid request body')
        else:
            chat_id = payload['message']['chat']['id']
            message = payload['message'].get('text')
            if type(message) is unicode:
                func = commands.get(message.split()[0].lower(), 'no_command')
                print(func)
                if func != 'no_command':
                    TelegramBot.sendMessage(chat_id, func(), parse_mode='Markdown')
                else:
                    if message.find(u'#разбор') != -1:
                        func = commands.get('/add')
                        TelegramBot.sendMessage(chat_id, func(), parse_mode='Markdown')
                    else:
                        TelegramBot.sendMessage(chat_id, 'I do not understand you, Sir!')
            else:
                TelegramBot.sendMessage(chat_id, 'It is not a text message')

        return JsonResponse({}, status=200)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CommandReceiveView, self).dispatch(request, *args, **kwargs)