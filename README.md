# docraptor-python-tutorial

This repository contains a sample project showcasing how you can use [Docraptor](https://docraptor.com/) via Python to convert HTML to PDF. I am using a simple HTML based invoice template from [sparksuite](https://github.com/sparksuite/simple-html-invoice-template/blob/master/invoice.html) as input.

You need to register for an account on [Docraptor](https://docraptor.com/) and get a free API key before you can use this code.

### Requirements

This code was tested in Python 3.10 but should work with all Python 3+ versions. You need to install the following dependencies as well:

- docraptor `pip install --upgrade docraptor`

### Run

You need to edit the `invoice.html` file to suit your needs. Next, you need to add your Docraptor API key in your environment. You can do so by opening up the terminal and running this command (replace `YOUR_API_KEY` with your key)

```
$ export DOCRAPTOR_KEY=YOUR_API_KEY
```

Now you can run the `app.py` file:

```
$ python app.py
```

### LICENSE

```
MIT License

Copyright (c) 2022 M.Yasoob Ullah Khalid ☺

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```