import tkinter
from tkinter import *
from tkinter import font, messagebox, scrolledtext
import requests, webbrowser, pyperclip, sys, os

dir_path = os.path.join(os.environ['APPDATA'], 'TinyLS') #path AppData/Roaming/TinyLS
if not os.path.exists(dir_path):
	os.makedirs(dir_path)
file_path = os.path.join(dir_path, 'icon.ico') #path AppData/Roaming/TinyLS/icon.ico
if not os.path.exists(file_path):
	try:
		icon = requests.get("https://raw.githubusercontent.com/NicholasJohansan/TinyURL-LinkShortener-Program/master/icon.ico", allow_redirects=True).content
		open(file_path, 'wb').write(icon)
	except:
		pass

class Application:
	def __init__(self, app):
		self.app = app
		self.version = 0.2
		self.latest = 0.0
		self.downloadURL = "https://github.com/NicholasJohansan/TinyURL-LinkShortener-Program/raw/master/TinyLS.exe"
		self.font = font.Font(family="helvetica", size=12)

		app.title("TinyURL Link Shortener")
		app.geometry(f"+50+100")
		app.resizable(False, False)
		app['bg'] = "#fff"
		try:
			app.iconbitmap(file_path)
		except:
			pass

		self.lblTitle = Label(app, text="TinyLS - Link Shortener", bd=3, relief=GROOVE, fg="#192ecc", font=font.Font(family="fixedsys", size=20, weight="bold"), padx=20, pady=5, bg="#aaeeff")
		self.lblTitle.grid(row=0, column=0, columnspan=4, sticky="ew", ipadx=10, ipady=5)

		self.lblSubtitle = Label(app, text="somewhat more efficient than going to the website", bg="#fff", fg="#192ecc", font=font.Font(family="fixedsys", size=6), padx=10)
		self.lblSubtitle.grid(row=1, column=0, columnspan=4, pady=(5, 15))

		self.lblLink = Label(app, text="Enter your long URL below!", font=self.font, fg="#000080", bg="#fff")
		self.lblLink.grid(row=2, column=0, columnspan=4, pady=(10, 5))

		self.entryURL = scrolledtext.ScrolledText(app, font=self.font, width=50, height=5, bd=4, wrap='word', bg="#aaeeff", fg="#000080", highlightcolor="#000080", selectbackground="#aaeeff")
		self.entryURL.vbar.configure(width=12, troughcolor="#192ecc", bg="#aaeeff", activebackground="#aaeeff")
		self.entryURL.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

		self.frameAlias = Frame(app, bg="#73e2ff")
		self.frameAlias.grid(row=4, column=0, columnspan=4, sticky="ew")

		self.lblAlias = Label(self.frameAlias, text="Custom Alias", font=self.font, pady=10, justify="left", bg="#ffffff", fg="#000080")
		self.lblAlias.grid(row=0, column=0, sticky="e", ipadx=10, padx=(16, 5))

		self.entryAlias = Entry(self.frameAlias, font=self.font, bd=4, width=35, fg="#000080")
		self.entryAlias.grid(row=0, column=1, padx=(5, 16), sticky="we", ipady=2)

		self.btnSubmit = Button(app, text="Shorten Link", font=self.font, command=self.shortenLink, width=40, height=1, bd=5, fg="#000080", bg="#45d9ff", activebackground="#fff", borderwidth=5, activeforeground="#45d9ff", highlightcolor="#000000", relief=GROOVE)
		self.btnSubmit.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

		self.lblVersion = Label(app, text=f"TinyLS v{self.version}", font=("helvetica", 9, "bold"), bg="#aaeeff", fg="#000080")
		self.lblVersion.grid(row=6, column=0, columnspan=4, pady=(20, 5), sticky="ew")

		self.btnUpdate = Button(app, text="Update", font=self.font, command=self.update, activebackground="#fff", activeforeground="#45d9ff", width=20, height=1, state=DISABLED, relief=FLAT, bg="#45d9ff", fg="#000080")
		self.btnUpdate.grid(row=7, column=0, columnspan=2, sticky="ew")

		self.btnInfo = Button(app, text="Info/About", font=self.font, relief=FLAT, activebackground="#fff", activeforeground="#45d9ff", bg="#45d9ff", fg="#000080", command=lambda: messagebox.showinfo("Info/About", "This is a computer program designed to make link shortening more faster and easier.\n\nThis program utilises the TinyURL \"API\" by putting in parameters to the php url: https://tinyurl.com/create.php?alias=()&url=()\n\nThis program is made by @NJ889\nCopyright © 2020 Nicholas Johansan"), width=20, height=1)
		self.btnInfo.grid(row=7, column=2, columnspan=2, sticky="ew")

		self.checkVersion()
		
	def update(self):
		webbrowser.open_new(self.downloadURL)
		sys.exit()

	def checkVersion(self):
		try:
			self.latest = float(requests.get("https://raw.githubusercontent.com/NicholasJohansan/TinyURL-LinkShortener-Program/master/version.txt", timeout=5).content)
			if self.latest == self.version:
				self.lblVersion.config(text=f"TinyLS v{self.version} | you are up to date!")
			elif self.latest > self.version:
				self.lblVersion.config(text=f"TinyLS v{self.version} | v{self.latest} is available, you may update!")
				self.btnUpdate.config(state=NORMAL)
			else:
				self.lblVersion.config(text=f"TinyLS v{self.version} | you are on a developmental version!")
		except requests.ConnectionError as e:
			messagebox.showinfo("Connection Error", "Make sure that you are connected to the internet!\nThe program will now close as it requires internet connection in order to access TinyURL!")
			sys.exit()
		except requests.Timeout as e:
			messagebox.showinfo("Timeout Error", "The program have timed out while fetching the latest version!\nPlease restart the app as the program may not function as intended!")
			return
		except requests.RequestException as e:
			messagebox.showinfo("General Error", "An unexpected error have occured!\nThe error may or may not be fatal and will exit now to prevent further errors.\nPlease report this issue!")
			sys.exit()
		except requests.HTTPError as e:
			messagebox.showinfo("HTTP Error", "A request sent to fetch the latest version have failed!\nThis may be caused by the github servers being down which is unlikely!\nYou may proceed however the program might not work as intended, you can restart it if need be.")
			return

	def shortenLink(self):
		URL = self.entryURL.get("1.0", tkinter.END).strip().replace("\n", "")
		print(URL)
		Alias = self.entryAlias.get().rstrip("\n")
		if URL == "":
			messagebox.showinfo("Missing Fields", "Please fill in the URL first!")
			return
		elif Alias == "":
			messagebox.showinfo("Missing Fields", "Please fill in the Custom Alias!")
			return
		r = requests.get(f"https://tinyurl.com/create.php?alias={Alias}&url={URL}")
		if b'TinyURL can\'t be created, please try again below:' in r.content:
			err_msg = ""
			if b'Invalid URL' in r.content:
				err_msg = f"{URL} is an invalid URL!\nPlease enter a valid URL and try again!"
			elif b'Alias is not available' in r.content:
				err_msg = f"tinyurl.com/{Alias} is taken!\nPlease try again with another Alias!"
			elif b'The Alias must be at least 5 characters.' in r.content:
				err_msg = f'{Alias} is not at least 5 characters long!\nTry again with another Alias!'
			elif b'Too many custom aliases for this URL' in r.content:
				err_msg = f"{URL} is overused!\nTry again with another URL!"
			elif b'URL domain banned' in r.content:
				err_msg = f"The URL Domain of {URL} is banned!\nTry again with a different URL!"
			if err_msg != "":
				messagebox.showinfo("Link Shortening Failed", err_msg)
		else:
			pyperclip.copy(f"https://tinyurl.com/{Alias}")
			messagebox.showinfo("Success!", f"https://tinyurl.com/{Alias} have been successfully made!\nThe shortened link have been copied to your clipboard!")

app = Tk()
UI = Application(app)
app.mainloop()