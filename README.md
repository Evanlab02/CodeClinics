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

<h3>1.2 Installation For binary users</h3>

Open your terminal, your file should be in your downloads so head over to that directory and do the following(this might vary on devices)

```bash
$ cd ~/Downloads/
$ chmod +X code_clinic
$ sudo cp code_clinic /usr/local/bin/
```

You should now be able to run code_clinics, by doing the following

```bash
code_clinic --help
```

The output should be similiar to the following
