# maverickmoore.com_02

## About this Project

**Purpose**
This website is my online presence. Ideally, it can help with job hunting, professional growth, and networking opportunities.

As a web developer, this website needs to look great, be easy to use, and rank on Google.

As a user, this website needs to answer your questions about what Maverick does and the website itself can serve as the proof that I am a qualified web developer.


## Important Topics

**SEO**
- Increase organic web presence
- Useful for recruiters and developers
- Publish web content
- Accessible
- Fast


**Maverick**
- Software engineer
- Web developer
- Entrepreneur
- Python / Django Specialist


**Career Hunting**
- Resource for recruiters
- Resource for networking


## Running website locally

**First time**
Clone the repo when working with the repo for the first time.

```bash
git clone git@github.com:mcm66103/maverickmoore.com_02.git

or

git clone https://github.com/mcm66103/maverickmoore.com_02.git
```

Then create a virtual environment with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

```bash
mkvirtualenv maverickmoore
```

Configure your environment variables. look for `mysite/.env.template`.

Reach out to me (maverick) to get the values for the `.env`. Or fiddle around with Twilio and generate yer own credentials.

Copy and paste the contents of `.env.template` to a new file called `.env`

Next step, run you migrations.

```bash
python manage.py migrate
```


**Each time you pull**
activate your virtual environment

```bash
workon maverickmoore
```

Install new requirements.

```bash
pip install -r requirements.txt
```

If there have been new migrations then run them.

```bash
python manage.py migrate
```

**Turning on the webserver**

run this bash command from the project root to kick off the webserver.

```bash
python manage.py runserver
```

Now visit the site from your browser with the url `127.0.0.1:8000`.
