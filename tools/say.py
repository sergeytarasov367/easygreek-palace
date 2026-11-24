#!/usr/bin/env python3
"""Озвучить слово или реплику для игры (бесплатно, через edge-tts).
  pip install edge-tts
  python3 tools/say.py kitchen/q/thanks "Ευχαριστώ!" --voice nestoras
Файл ляжет в kitchen/q/thanks.mp3. Чтобы игра взяла свои файлы, откройте её с ?localaudio=1.
Голоса: athina (женский, слова), nestoras (мужской). Скорость -15 % — как на сайте."""
import argparse, asyncio, pathlib
import edge_tts, edge_tts.communicate as _cm
from edge_tts.constants import TRUSTED_CLIENT_TOKEN

# старый адрес speech.platform.bing.com отдаёт 403 из Европы (rany2/edge-tts#490) — новый хост, тот же открытый ключ библиотеки
_cm.WSS_URL = f"wss://api.msedgeservices.com/tts/cognitiveservices/websocket/v1?Ocp-Apim-Subscription-Key={TRUSTED_CLIENT_TOKEN}"
VOICES = {'athina': 'el-GR-AthinaNeural', 'nestoras': 'el-GR-NestorasNeural'}
ap = argparse.ArgumentParser()
ap.add_argument('path', help='путь без .mp3, например audio/kanapes или kitchen/q/thanks')
ap.add_argument('text', help='греческий текст')
ap.add_argument('--voice', default='athina', choices=sorted(VOICES))
a = ap.parse_args()
out = pathlib.Path(a.path + '.mp3'); out.parent.mkdir(parents=True, exist_ok=True)
text = a.text.replace(';', '?').replace('\u037e', '?')   # греческий «;» — вопрос: иначе синтез читает его как точку
asyncio.run(edge_tts.Communicate(text, VOICES[a.voice], rate='-15%').save(str(out)))
print('ok', out)
