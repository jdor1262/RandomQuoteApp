import requests
from tkinter import *
# TODO! 
# make necessary installations/imports

def get_quote():
   
    # TODO!
    #Write your code here.
    #Make an API call to get a random quote (including exception handling)
    # Requirements of the API call:
        # Make the call to 'http://api.quotable.io'
        # Get 1 random quote at a time
        # Specify a category (check out the documentation to learn more about categories and how to use them)
        # Customize your endpoint and parameters according to the requirements above.  
    #Parse the response object and store the quote and the author in variables called 'quote' and 'author'


    response = requests.get("http://api.quotable.io/random")


    if response.status_code == 200:

        data = response.json()
        quote = data['content']
        author = data['author']
        print("Quote:", quote)
        print("Author:", author)
        #Pass the quote variable into the canvas via the 'quote' variable.
        canvas.itemconfig(quote_text, text=quote)
        #Pass the author variable into the canvas via the 'author' variable.
        canvas.itemconfig(author_text, text=author)
    else:
        # If the request was not successful, print the status code
        print("Failed to retrieve quote. Status code:", response.status_code)


window = Tk()
window.title("Random Quote App")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

quote_text = canvas.create_text(
    150,
    180,
    text="Click on the button below to load a random quote.",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

author_text = canvas.create_text(
    150, 320, text="", width=250, font=("Arial", 20, "italic"), fill="white"
)
canvas.grid(row=0, column=0)

button = Button(highlightthickness=0, command=get_quote, text="Get a new quote")
button.grid(row=1, column=0)

window.mainloop()