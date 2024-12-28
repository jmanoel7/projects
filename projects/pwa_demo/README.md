# Django PWA Installation Demo

This repository contains the code for the Django Progressive Web App (PWA) installation demo featured in my YouTube tutorial. Follow the steps below to set up and run the demo.

## Setup Instructions

### Step 1: Install Dependencies

Ensure you have Python installed on your system. Use the following command to install all required dependencies:

```sh
pip install -r requirements.txt
```

### Step 2: Apply Migrations

Although this demo doesn't use any database models, applying migrations will suppress warnings related to migrations:

```sh
python manage.py migrate
```

### Step 3: Collect Static Files

Prepare and collect static files for the PWA demo:

```sh
python manage.py collectstatic
```

### Step 4: Run the Demo

Start the Django development server to launch the PWA demo:

```sh
python manage.py runserver
```

## Contribute

If you'd like to improve this demo or suggest changes:

1. Fork the repository.
2. Create a branch for your updates.
3. Submit a pull request.

## Watch the Tutorial

For a detailed walkthrough of setting up a Django PWA, check out the [YouTube video:](https://youtu.be/lteaqUZWk3E).
