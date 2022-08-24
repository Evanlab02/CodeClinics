<h1>CodeClinics</h1>
<strong>NOTE: CodeClinics is intended to run on Linux (Works best on Ubuntu)</strong>
<h2>1. Installing CodeClinics</h2>
<p>There are 2 ways to get CodeClinics on your computer, the first method is suggested if you do not intend to change the program at all, the second method being if you want edit the source code to suit your needs better.</p>
<h3>1.1 Download</h3>
<h4>1.1.1 Download the binary</h4>

Head to the releases tab and download the latest binary (code_clinic)

![download_bin](https://user-images.githubusercontent.com/36800222/186501488-47816f7c-101e-47a3-8d13-d590f513d78e.gif)

<h4>1.1.2 Download source files</h4>

Fork and clone this repo to your device!

<h2>1.2 Installation for Non-Binary Users</h2>

To install dependencies you can run

```bash
$ make setup
```

Or you can use pipenv - Suggested if you are planning to work with this codebase

```bash
$ pipenv shell
$ pipenv sync
```

You can now follow along with the binary users (You will just instead be using python and code_clinic.py)

<h3>1.3 Installation For Binary Users</h3>

Open your terminal, your file should be in your downloads so head over to that directory and do the following(this might vary on devices)

```bash
$ cd ~/Downloads/
$ chmod +X code_clinic
$ sudo cp code_clinic /usr/local/bin/
```

You should now be able to run code_clinics, by doing the following

```bash
$ code_clinic --help
```

The output should be similiar to the following

![help_command](https://user-images.githubusercontent.com/36800222/186504176-22c978e5-82b8-4058-bec8-415f18640b1c.png)

You can then proceed to do the following

```bash
$ code_clinic install
```

You will then see this:

![credentials](https://user-images.githubusercontent.com/36800222/186505269-e967f874-c2c5-45ad-96d4-513a4635cf43.png)

Paste your credentials file (Refer to 2. Google Calendar API) into the storage directory, and press enter (Remember to enable show hidden files)

If you did this step correctly, you will see this:

![welcome](https://user-images.githubusercontent.com/36800222/186505953-9ef8a64c-7a07-4d71-9b15-a579ebb0e9b4.png)

One of the parts of the installation will also require your google calendar ID (Refer to 2. Google Calendar API if you are unsure what this means)

<h2>2. Google Calendar API</h2>

This program uses the google calendar API and this unfortunately means for any user using this program, they have to familiarize themself with the API to get this prorgram running. This means you need to create a project on the Google Calendar API. 

When you have created this project you also need to create an client secret and download the client secret - rename it to 'credentials.json' - and store it in the storage directory. 

You can then proceed to create a central calendar that will be used to store all the events in a middle point and go to its settings and find the calendar ID, copy this ID and keep it somewhere for when you install code_clinics. This step I will not include screenshots for and this will be up to you to solve.

<h2>3. Use the help command</h2>

Use the help command to find out more about how to use this program and have fun. 

<h2>4. Command Examples</h2>

<h3>4.1 Login</h3>

![login](https://user-images.githubusercontent.com/36800222/186509069-6bf8891f-f939-40a4-a39b-32f8a32131e5.png)

<h3>4.2 Volunteer</h3>

![volunteer](https://user-images.githubusercontent.com/36800222/186509551-5639ca6f-aff3-4e32-b1a7-464face44fb4.png)

<h3>4.3 Book</h3>

![book](https://user-images.githubusercontent.com/36800222/186510159-b2b9779a-7978-4eae-aba5-8b6194e965a7.png)

<h3>4.4 Calendar</h3>

![calendar](https://user-images.githubusercontent.com/36800222/186510285-09b5ce23-6032-4a9f-96bb-45c7b9b4fc6c.png)

<h3>4.5.1 Cancel Volunteer</h3>

![deleted](https://user-images.githubusercontent.com/36800222/186510572-5d7a1748-0195-428d-80d2-57ab35c4ed70.png)

<h3>4.5.2 Cancel Student</h3>

[No Image] - You can run this command using

```bash
$ code_clinic cancel --member-type student
```

