# gischatbot

![gischatbot](gischatimage.jpg)

## A Twitter bot for the #gischat community

### gischatbot is a Twitter bot that:

* Retweet every tweet with the hashtag #gischat

* Follow all handles who tweet with #gischat

* Reminds a user when it's 30 minutes to #gischat

* Provide with the local time/timezone for #gischat to a user. 

## Usage

On the platform you can:

Tweet:

```
 #gischat
```

As a comment/tweet and it'll like and retweet the tweet and follow the user as well. 

Tweet:

```
when @gischatbot
```
As a comment or a tweet. It'll reply with the time for #gischat in your timezone(in development).

Tweet:

```
remind @gischatbot
```
As a comment/tweet and it will remind the user when its 30minutes to #gischat in his/her time zone(in development).


## Local Deployment

To use on computer, ensure that you have Python 3 installed.

Assign proper values to the environment variables in the .env file.

Run:

```
pip install -r requirements.txt
```

Run on terminal 1: 

```
python worker.py
```

Run on terminal 2:

```
python clock.py
```

## Running the tests

There are no tests yet.

## Contributing

Contributions are welcomed.


## Authors:

**Jolaiya Emmanuel** - [@jeafreezy](https://twitter.com/jeafreezy) <br>
**Kayode Adeniyi** - [@AdeniyiKayodee](https://twitter.com/AdeniyiKayodee) <br>
**Adigun Kehinde** - [@Adigun Kehinde](https://twitter.com/adiguntoba)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Thanks to:
* [Maptasti-Kate](https://twitter.com/pokateo_)
* [Dr. Michele M Tobias](https://twitter/MicheleTobias)

and everyone who provided ideas to help make this project better.


