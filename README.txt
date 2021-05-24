------------------------------Languagage Translator App(automation script)---------------------------------------------------

A)Purpose of this app:
-This idea popped up in my mind when i saw my aunt finding difficulty to understand any message she received on  whatsapp because they were in English.
-She had to open google chrome and copy paste the content and get it translated by any website.
-At that time,I thought of how translation works and what if I can provide a  an input file containing the content
 which can be translated to Hindi in an output txt file.
-Storing in a file was needed because the user can refer to the translated content as and when needed.


B)Python Module used in this:

-I have used 'google_trans_new'  module for this automation.
-Although there are many translator api's availabe in the market egIBM Watson Language Translator API,MyMemory Translation API
-Googletrans is a free and unlimited python library that implemented Google Translate API.
-google_translator  class is the class which is used here.
-Features of this API-
 1)Fast and reliable - it uses the same servers that translate.google.com uses
 2)Auto language detection
 3)Bulk translations
 4)Customizable service URL/Http2 support


C)Working/internal implementation of this application:
-The 'google_trans_new' module is first installed in the project using Settings/Interpreter/pip option or
 pip install google_trans_new

-After installing the module,we need to import 'google_translator' class which is used for the translating the text.

-Then we need two files here
  1)input.txt -which is an input file containg the text to be translated
  2)output.txt -which has the translated text in hindi or whichever language is specified by the user

-input file is opened in read mode and output file is opened in write mode

-translate() of the class is used to translate the content


C)translate() method:

-translate() method has few parameters:
 1)text - input to be translated
 2)lang_tgt/dest -langauge to which input has to be converted
     lang_tgt = 'hi' i.e hi is the language code for hindi**
 2)lang_src/src

**langauge codes can be obtained from google_trans_new/google_trans.LANGCODES--you can print using this


D)Issue faced while developing this mini project:

-Issue 1
  memory finished while using translate api of python
  number of word translated were 1000 per day.
  So had to figure out alternative of that.Used google_trans

-Issue 2:
 While using googletrans ,it was not working
 showing atrribute error
 'NoneType' object has no attribute 'group'
  नमस्ते

Therfore hunted for the solution and found that this google_trans repo version has some errors
so people were suggesting to use google_trans_new


E)Exception where it would fail:

-The maximum character limit on a single text is 15k.
-so very large files could not translated

Note-For more details:
    https://pypi.org/project/googletrans/
    https://py-googletrans.readthedocs.io/en/latest/
    https://pypi.org/project/translate-api/


