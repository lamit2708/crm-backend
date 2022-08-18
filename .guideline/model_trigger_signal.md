# Trigger vs Signal

## Compare 1

Triggers monitor database row changes, thus they operate on raw tabular data. Trigger code is run by DBMS.

In contrast to triggers signals monitor domain object changes. In a generic case Django's model consists of data from several table rows (consider model inheritance and related object subsets). Signal code is run by Django.

## Compare 2

Main advantages of Triggers over Signals:

    independent of the application: makes the migration to a new frameworks/languages easier (since triggers and, in some cases, stored procedure are dump with your DB)

    safety: depending on the situation, you could restrict the UPDATE rights on some tables and still be able to run your app (think of critical history or transaction tables, who knows which exploits might be discovered in the next 10 years)

    reduce the number of requests your app have to address to the DBMS (especially useful in the context of a distributed architecture).

Here are the main advantages. The main cons is that you have to deal with the old school SQL syntax.

## Django Signal

[REF](https://docs.djangoproject.com/en/dev/topics/signals/)

## Using Simple Database Triggers to Solve Complex Django Problems

[REF](https://www.youtube.com/watch?v=6Mtd6O_DVSo)

## Django Trigger

[REF](https://pypi.org/project/django-triggers/)
