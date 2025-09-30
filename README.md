# InstaDL

InstaDL is a Python script that allows you to download Instagram Reels using the `instaloader` library. You can provide a list of Reel URLs in the `main.py` file, and the script will download them into separate folders named after the Reel's shortcode.

---

## How to Use

1. **Add your Reel links**  
   Open the `main.py` file and add the Instagram Reel URLs you want to download to the `reel_links` list:

```python
   reel_links = [
       "https://www.instagram.com/reel/Cxyz123...",
       "https://www.instagram.com/reel/Abcde456..."
   ]
```

2. **Run the script**

```bash
   python main.py
```

3. **Find your downloads**
   The script will create a new folder for each Reel, named with its unique shortcode. The video and other post details will be inside these folders.

---

## Login (Optional)

If you need to download from a private account or encounter issues with rate limiting, you can log in to your Instagram account:

```python
# try:
#     loader.load_session_from_file("your_username")
# except FileNotFoundError:
#     username = "your_username"
#     password = "your_password"
#     loader.login(username, password)
#     print(f"Logged in as {username}")
```

Replace `"your_username"` and `"your_password"` with your Instagram credentials.

---

## Requirements
<p>
  <img src="https://skillicons.dev/icons?i=python" />  
</p>

* Python 3.x
* `instaloader`

Install the dependency:

```bash
pip install instaloader
```

---

## Disclaimer

This script is for personal use only. Please respect the privacy and copyright of the content you download. The developers of this script are not responsible for any misuse.

---

## License

This project is licensed under the MIT License.

---

## Author

**flowstxte** 
[GitHub](https://github.com/flowstxte)
