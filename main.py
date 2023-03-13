import asyncio
import edge_tts

from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/get_mp3', methods=['POST'])
def getmp3():
    data = request.get_json()
    text = data['text']
    voice = data['voice']
    model = voiceToModel(voice)
    file = data['file']
    asyncio.run(generate_mp3(text, model, file))
    return Response("success", status=200)


async def generate_mp3(text, voice, input_file) -> None:
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(input_file)


def voiceToModel(voice):
    if voice == "1":
        return "zh-CN-XiaoxiaoNeural"
    elif voice == "2":
        return "zh-CN-XiaoyiNeural"
    elif voice == "3":
        return "zh-CN-YunjianNeural"
    elif voice == "4":
        return "zh-CN-YunxiNeural"
    elif voice == "5":
        return "zh-CN-YunxiaNeural"
    elif voice == "6":
        return "zh-CN-YunyangNeural"
    elif voice == "7":
        return "zh-CN-liaoning-XiaobeiNeural"
    elif voice == "8":
        return "zh-CN-shaanxi-XiaoniNeural"
    elif voice == "9":
        return "zh-HK-HiuGaaiNeural"
    elif voice == "10":
        return "zh-HK-HiuMaanNeural"
    elif voice == "11":
        return "zh-HK-WanLungNeural"
    elif voice == "12":
        return "zh-TW-HsiaoChenNeural"
    elif voice == "13":
        return "zh-TW-HsiaoYuNeural"
    elif voice == "14":
        return "zh-TW-YunJheNeural"
    elif voice == "15":
        return "zu-ZA-ThandoNeural"
    elif voice == "16":
        return "zu-ZA-ThembaNeural"
    else:
        return "Invalid voice option"


if __name__ == '__main__':
    app.run(port=8023)
