# beautifulsoup-scraping

Dummied down explanation for scraper.py

 ```import requests```

🧳 This brings in the **requests** library, which lets Python **ask websites for information**, like typing a URL in your browser and getting a web page.

---

 ```from bs4 import BeautifulSoup```

🍲 This brings in **BeautifulSoup**, a tool that helps **clean and organize messy web page code (HTML)** so you can easily find what you’re looking for.

---

 ```url = "https://en.wikipedia.org/wiki/Albert_Einstein"```

🌐 This sets the URL (web address) we want to scrape. In this case, the **Wikipedia page about Albert Einstein**.

---

 ```response = requests.get(url)```

📩 This tells Python to **go to that URL** and bring back the webpage contents. It stores the response (like HTML code) in a variable called `response`.

---

 ```if response.status_code == 200:```

✅ This checks if the request was **successful**. If the website says “200 OK”, it means everything went fine, and we can continue.

---

 ```soup = BeautifulSoup(response.text, 'html.parser')```

🧼 This line takes the messy web page code from `response.text` and gives it to **BeautifulSoup**, which then **organizes it** like a structured tree so you can search through it.

---

 ```print(f"Page Title: {soup.find('h1').text}\n")```

📝 This finds the big title at the top of the page (usually inside an `<h1>` tag) and prints it out. In this case, it would say "Albert Einstein".

---

 ```print("Section Titles:")```

🪧 This just prints a heading so you know the next thing coming is a list of section titles.

---

 ```for header in soup.find_all(['h2', 'h3']):```

🔍 This tells Python to **look through all `<h2>` and `<h3>` tags**, which are usually used for **section titles and sub-section titles** on Wikipedia pages.

We loop through (go one-by-one) each of these tags.

---

 ```span = header.find('span', class_='mw-headline')```

🔎 Inside each header (`<h2>` or `<h3>`), we look for a **`<span>` tag with a class called `mw-headline`**. Wikipedia uses this structure to mark section headings.

---

 ```if span:```

✔️ If we found that special span (not empty), we know it’s a **real section title**, so we print it.

---

 ```print(" -", span.text)```

🖨️ This prints the **text inside the span**, which is the name of the section (e.g., "Biography", "Death", etc.).

---

 ```else:```

❌ If we **didn’t find the special span**, maybe the page is structured a bit differently.

---

 ```header_text = header.get_text(strip=True)```

🧼 So as a backup, we just grab **all the text inside the header**, and use `.strip()` to **remove extra spaces**.

---

 ```if header_text and 'edit' not in header_text.lower():```

⚠️ Sometimes the text includes unwanted things like the word **"edit"** (from the little edit buttons on Wikipedia). We check to **skip those**.

---

 ```print(" -", header_text)```

✅ This prints the fallback section title if we didn’t get it from the span.

---

 ```else: print("Failed to fetch page:", response.status_code)```

❌ If the website didn’t return a success message (`200`), we print the error code (e.g., `404` means “page not found”).

---
🧪 Summary in Human Terms

> You’re telling Python:
> > "Go to the Albert Einstein Wikipedia page. If the page loads okay, look through the HTML code, find all the section headers like 'Biography' and 'Death', and print them out nicely."

