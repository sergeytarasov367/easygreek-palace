# EasyGreek Palace — «Дворец памяти»

3D-игра для изучения греческого языка (уровень A2). Ходишь по дому, двору и улице, нажимаешь на вещи — слышишь слово по-гречески, видишь перевод и род. Персонажи дают задания по-гречески: «принеси хлеб», «дай мне три помидора».

**Играть:** https://easygreek.app/greek/palace/

## Открытый код и коммерческое использование

- Код игры открыт под лицензией [MIT](LICENSE).
- **EasyGreek — коммерческий проект.** Мы используем эту игру, включая вклад участников, в своём продукте, в том числе в коммерческих целях.
- **Любой другой тоже может** использовать, менять, встраивать и продавать этот код на условиях MIT.
- Участие добровольное и не оплачивается. Это не работа, не стажировка по договору и не обещание трудоустройства.
- Тренажёр письма, курс и методика EasyGreek закрыты и в этот репозиторий не входят.

## Запуск

```
python3 -m http.server 8000
```
Откройте http://localhost:8000/. Озвучка в репозиторий не входит — игра берёт её с easygreek.app. Свои файлы (см. `tools/say.py`) — с адресом `http://localhost:8000/?localaudio=1`.

## Как устроено

- `index.html` — вся игра: three.js r160 и наш код без сборки. Комнаты — `ROOMS`, слова — `WORDS`, задания персонажей — `QUESTS`.
- `models/` — 3D-модели [Kenney](https://kenney.nl) (CC0), файлы лицензий рядом.
- `vendor/` — three.js (MIT).
- `*/texts.txt` — греческие реплики комнат.
- `tools/say.py` — озвучка слова или реплики (edge-tts, бесплатно).

Движок игры свой: другой (Unity, Godot и т. п.) не подключаем — развиваем этот.

## Чем можно помочь

- Новые места и сценарии: магазин, остановка, кафе, аптека, рынок.
- Задания и диалоги персонажей для экзамена A2.
- Удобство на телефоне и планшете, исправления ошибок.

Как участвовать — [CONTRIBUTING.md](CONTRIBUTING.md). Сторонние материалы — [THIRD_PARTY.md](THIRD_PARTY.md).

---

## English

A 3D game for learning Greek (A2): walk around a house, a yard and a street, tap things to hear the Greek word and see its translation; characters give you tasks in Greek. Play: https://easygreek.app/greek/palace/

**Open source and commercial use.** The game code is MIT-licensed. EasyGreek is a commercial project: we use this game, including contributions, in our product, also for commercial purposes. Anyone else may use, modify and sell it under the MIT terms too. Contributing is voluntary and unpaid — it is not a job, a contracted internship or a promise of employment. The EasyGreek handwriting trainer, course and methodology are closed and not part of this repository.

Run: `python3 -m http.server 8000`, open http://localhost:8000/. See [CONTRIBUTING.md](CONTRIBUTING.md).
