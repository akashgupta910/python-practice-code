# AKHBAR PADHKE SUNAAO

def speak(api_key, category):
    import requests, json
    from win32com.client import Dispatch

    url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={api_key}"
    speak = Dispatch("SAPI.Spvoice")
    json_data = requests.get(url).json()

    count = 1
    index = 0
    news_num = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

    while count < 11:
        news = json_data["articles"][count]["description"]
        speak.Speak(f"{news_num[index]} news is {news}")
        count = count + 1
        index = index + 1
        speak.Speak(news)

if __name__ == "__main__":
    print("\n <-- Aaj ki Top 10 Khabre janiye bina Padhe --> \n")
    api_key = str(input("--> Enter you API key from Newsapi.org: "))
    category = input("\nCategories: \n\t 1. business \n\t 2. entertainment \n\t 3. health \n\t 4. science \n\t 5. sports \n\t 6. technology \n\n --> Enter the same name of category which you want: ")
    speak(api_key, category)