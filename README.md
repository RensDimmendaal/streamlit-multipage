# streamlit-multipage


## Inspiration

There's multiple ways to create a multipage streamlit app.

I tried out the approach from Prakhar Rathi in this [article](https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030).
They also made an elaborate example with their [data storyteller app](https://github.com/prakharrathi25/data-storyteller).

## Motivation

I decided to make this repo to address two things:

### 1. I wanted to fix the autoreload functionality

Streamlit allows you to reload changes in the app without restarting it. That's super useful when developing apps iteratively. Sadly, with the multipage approach this functionality breaks. With a small change I could get it to work again.

### 2. I wanted to make the demo as simple as possible

The datastoryteller app is is really nice. But it's also *a lot*. I wanted to create a minimal example so it's easier to share with other people who want to make a multipage app.

## Demo

*todo*

## Usage instructions

### To run the demo:

```
pip install streamlit
streamlit run app/main.py
```

Edit `app/pages/home.py` or `app/pages/another.py` and see that reload still works.

### Usage in your own projects

For your own usage copy the code in `app/` as a template.

Don't forget to add streamlit to your dependencies.