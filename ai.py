from flask import Flask, render_template
import requests

app = Flask(__name__)

# کلید API و URL برای دریافت اخبار
API_KEY = "fa5ecc572a4c444e9f320d7b1b75edb5"
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

# تابعی برای دریافت اخبار برتر امروز
def get_top_news():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        if "articles" in data:
            articles = data["articles"]
            # فیلتر کردن اخبار دارای توضیح (خلاصه)
            articles_with_description = [article for article in articles if article.get("description")]
            # فیلتر اخبار با تصویر و بدون تصویر
            articles_with_image = [article for article in articles_with_description if article.get("urlToImage")]
            articles_without_image = [article for article in articles_with_description if not article.get("urlToImage")]
            
            # جایگزینی اخبار بدون تصویر با اخبار تصویردار
            while len(articles_without_image) > 0 and len(articles_with_image) > 0:
                no_image_article = articles_without_image.pop(0)
                image_article = articles_with_image.pop(0)
                no_image_article["urlToImage"] = image_article["urlToImage"]
                articles_with_image.append(no_image_article)
            # بازگشت ۱۲ خبر
            return articles_with_image[:20]
    return []

# روت اصلی برای نمایش صفحه
@app.route('/')
def home():
    news = get_top_news()
    return render_template('index.html', news=news)

if __name__ == '__main__':
    app.run(debug=True)
