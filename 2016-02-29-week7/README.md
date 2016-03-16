# Week 7 (Feb. 29, 2016)

This week we're going to start talking about web scraping -- though without (yet) diving into the Python code. As we start going over some of the basics, these resources might come in handy:

  - [The request/response cycle](https://en.wikipedia.org/wiki/Request%E2%80%93response) (Wikipedia)
  - [More about the request/response cycle](http://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177) (Written for humans)
  - [Codecademy HTML/CSS basics](https://www.codecademy.com/en/tracks/htmlcss)

Also, following up on some of the git questions from the last couple weeks, these guides covering git basics might be helpful as well:

  - [Git -- the simple guide](http://rogerdudler.github.io/git-guide/)
  - [Learn Git in 20 Minutes](https://www.youtube.com/watch?v=0fKg7e37bQE)

And here are a few examples of how to do the things we've been discussing with Github, starting with cloning, which copies a repository from Github onto your machine (using this repo as an example):

```
git clone https://github.com/cjdd3b/advanced-data-journalism.git
```

You can also fork the repository into your own account, then clone it from there. Forking takes place through the Github website. [This guide](https://guides.github.com/activities/forking/) provides pretty good instructions.

Subsequent updates to a cloned repository is done via a pull:

```
cd location-of-your-repository
git pull
```

That covers getting code from Github onto your machine. Obviously, you can also push code from your machine to Github -- as long as you control the repo. Here's how you might create a repository called "adj-assignments".

First, log into your Github account and [create a repository](https://help.github.com/articles/creating-a-new-repository/) using the website.

Next, clone that repository on to your machine (in this case, we'll put it on the desktop):

```
cd Desktop
git clone https://github.com/your-user-name/adj-assignments.git
```

Go ahead an add a file to that repository once it's been cloned. Once that's done, you can check add it and check it back into Github.

```
git add .
git commit -m 'New file'
git push
```