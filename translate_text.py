from google_trans_new import google_translator

#creating an object of google_translator class
translator=google_translator()

#opening two files .one in read mode and other in write mode
with open("input.txt",'r') as fin:
    with open("output.txt",'w', encoding="utf-8") as fout:
        for line in fin:
            translation=translator.translate(line,lang_tgt='hi')
            fout.write(translation)
            #print(translation)


print("Your input file is translated to your required language")





'''from googletrans import Translator
#import googletrans
#print(googletrans.LANGCODES)
translator=Translator()
try:

   translation=translator.translate("hello")
   print(translation)
except Exception as e:
    print(e)'''



'''from translate import Translator
translator=Translator(to_lang="hi")
with open("input.txt",'r') as fin:
    with open("output.txt", 'w', encoding="utf-8") as fout:
       for line in fin:
          translation=translator.translate(line)
          fout.write(translation)

print("Your Input file has been translated to your desired langauge" )'''


