import json
import jieba
import matplotlib.pyplot as plt
from tinydb import TinyDB

from config import topics
from config import wordbank_topics

wordbank = dict()
topic_results = dict()
user_results = dict()

def get_keywords():
    global wordbank
    for wordbank_topic in wordbank_topics:
        with open(".\\Keywords\\" + wordbank_topic + ".json", "r", encoding="utf-8") as f:
            data = json.load(f)
        data = data["Keywords"]
        wordbank[wordbank_topic] = [x[1] for x in data.items()]

def judge(topic, text):
    words = jieba.lcut(text)
    for word in words:
        if word in wordbank[topic]:
            return True
    return False

def analysis_topic(topic):
    db = TinyDB(".\\Topics\\" + f"{topic}.json", ensure_ascii=False, encoding='utf-8')
    texts = dict()
    for wordbank_topic in wordbank_topics:
        texts[wordbank_topic] = list()
    total_length = len(db.all())
    for item in db.all():
        text = ""
        text += item["data"]["content"]
        text += "".join(x for x in item["data"]["comments"])

        for wordbank_topic in wordbank_topics:
            if judge(wordbank_topic, text):
                texts[wordbank_topic].append(item)

    print(f"topic: {topic}\nlen: {total_length}")
    topic_results[topic] = list()
    for wordbank_topic in wordbank_topics:
        # print(f"{wordbank_topic}: {len(texts[wordbank_topic])/total_length*100:.1f}%")
        topic_results[topic].append({wordbank_topic: round(len(texts[wordbank_topic])/total_length*100, 1)})

def analysis_user():
    db = TinyDB(".\\User\\" + 'user.json', ensure_ascii=False, encoding='utf-8')
    texts = dict()
    for wordbank_topic in wordbank_topics:
        texts[wordbank_topic] = list()
    total_length = len(db.all())
    for item in db.all():
        text = ""
        text += item["data"]["content"]
        for comment in item["data"]["comment"]:
            text += comment["comment"]
            for response in comment["responses_to_comment"]:
                text += response

        for wordbank_topic in wordbank_topics:
            if judge(wordbank_topic, text):
                texts[wordbank_topic].append(item)

    print(f"user_len: {total_length}")
    for wordbank_topic in wordbank_topics:
        user_results[wordbank_topic] = round(len(texts[wordbank_topic])/total_length*100, 1)

def plot(ax, x_data, y_data, title, xlabel, ylabel):
    ax.bar(x_data, y_data)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0,100)

if __name__ == "__main__":
    plt.rcParams['font.family'] = 'SimHei'
    get_keywords()
    for topic in topics:
        analysis_topic(topic)
    analysis_user()
    fig, axes = plt.subplots(3, len(topics) // 3 + 1, figsize = (len(topics) // 3 * 5 + 5, 15))
    axes = axes.ravel()
    axes_iter = iter(axes)
    for topic in topics:
        x, y = list(), list()
        for i, item in enumerate(topic_results[topic]):
            x.append(f"{wordbank_topics[i]}\n{item[wordbank_topics[i]]}%")
            y.append(item[wordbank_topics[i]])
        plot(next(axes_iter), x, y, topic, "", "比例")
    plt.tight_layout()
    plt.show()

    x, y = list(), list()
    for k, v in user_results.items():
        x.append(f"{k}\n{v}%")
        y.append(v)
    plt.clf()
    plt.title("用户")
    plt.ylabel("比例")
    plt.ylim(0, 100)
    plt.bar(x, y)
    plt.show()