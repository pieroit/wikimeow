
import wikipedia
import wikiquote
from langdetect import detect
from cat.mad_hatter.decorators import tool


@tool(return_direct=True)
def search_on_wikipedia(query, cat):
    """Search on wikipedia. Input is the search query."""

    # language detection
    language = detect(cat.working_memory.user_message_json.text)
    wikipedia.set_lang(language)
    
    # search page
    page = wikipedia.page(query)

    # compose a message for user
    return f"""

<h2>{page.title}</h2>

<blockquote>
    {page.summary}
</blockquote>

<img src="{page.images[0]}" width="500">

<a href="{page.url}">Read more</a>
"""


@tool(return_direct=True)
def search_on_wikiquote(query, cat):
    """Search quote on wikiquote. Input is the search query."""

    # language detection
    language = detect(cat.working_memory.user_message_json.text)
    
    # search quote
    quotes = wikiquote.quotes(query, lang=language)

    # compose a message for user
    reply = "\n"
    for q in quotes[:10]:
        reply += f"""\n - {q}"""
    reply += "\n"

    return reply

