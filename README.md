# Translator-API

<h1>Description</h1>
<p>To translate the given text into any language</p>

<h2>Languages and Modules</h2>
<ul>
  <li>Django</li>
  <li>Django REST framework : http://www.django-rest-framework.org/</li>
  <li>googletrans : https://pypi.python.org/pypi/googletrans</li>
</ul>

<h2>How To Test</h2>
<p>send the HTTP 'POST' message to the following url pattern </p>
<p>http://[address:port]/api/translator</p>

<h2>POST message format</h2>
<p>{"text":"How are you", "dest":"de"}</p>
<p>You can place any text you want in the place of "How are you"</p>
<p>You can choose any language code that you want to translated</p>

<h3>The simple way to test</h3>
<ol>
  <li>Go to the directory which has 'manage.py' then type in "python3 manage.py runserver [portno]"</li>
  <li>Go to the following url in browser "http://127.0.0.1:[portno]/translator/"</li>
  <li>Type in POST json format - {"text":"How are you", "dest":"de"} in the content</li>
  <li>Click on the "POST</li>
  <li>OR</li>
  <li>curl -H "Content-Type: application/json" -X POST -d '{"text":"How are you", "dest":"de"}' http://localhost:[portNo]/translator/</li>
</ol>

<h2>Language Codes</h2>
<ul>
  <li>af for Afrikaans</li>
  <li>ar for Arabic</li>
  <li>ast for Asturian</li>
  <li>az for Azerbaijani</li>
  <li>bg for Bulgarian</li>
  <li>be for Belarusian</li>
  <li>bn for Bengali</li>
  <li>br for Breton</li>
  <li>bs for Bosnian</li>
  <li>ca for Catalan</li>
  <li>cs for Czech</li>
  <li>cy for Welsh</li>
  <li>da for Danish</li>
  <li>de for German</li>
  <li>dsb for Lower Sorbian</li>
  <li>el for Greek</li>
  <li>en for English</li>
  <li>en-au for Australian English</li>
  <li>en-gb for British English</li>
  <li>eo for Esperanto</li>
  <li>es for Spanish</li>
  <li>es-ar for Argentinian Spanish</li>
 <li>es-co for Colombian Spanish</li>
 <li>es-mx for Mexican Spanish</li>
 <li>es-ni for Nicaraguan Spanish</li>
 <li>es-ve for Venezuelan Spanish</li>  
 <li>et for Estonian</li>
 <li>eu for Basque</li>
 <li>fa for Persian</li>
 <li>fi for Finnish</li>
 <li>fr for French</li>
 <li>fy for Frisian</li>
 <li>ga for Irish</li>
 <li>gd for Scottish Galic</li>
 <li>gl for Galician</li>
 <li>he for Hebrew</li>
 <li>hi for Hindi</li>
 <li>hr for Croatian</li>
 <li>hsb for Upper Sorbian</li>
 <li>hu for Hungarian</li>
 <li>ia for Interlingua</li>
 <li>id for Indonesian</li>
 <li>io for Ido</li>
 <li>is for Icelandic</li>
 <li>it for Italian</li>
 <li>ja for Japanese</li>
 <li>ka for Georgian</li>
 <li>kk for Kazakh</li>
 <li>km for Khmer</li>
 <li>kn for Kannada</li>
 <li>ko for Korean</li>
 <li>lb for Luxembourgish</li>
 <li>lt for Lithuanian</li>
 <li>lv for Latvian</li>
 <li>mk for Macedonian</li>
 <li>ml for Malayalam</li>
 <li>mn for Mongolian</li> for 
 <li>mr for Marathi</li>
 <li>my for Burmese</li>
 <li>nb for Norwegian Bokmål</li>
 <li>ne for Nepali</li>
 <li>nl for Dutch</li>
 <li>nn for Norwegian Nynorsk</li>
 <li>os for Ossetic</li>
 <li>pa for Punjabi</li>
 <li>pl for Polish</li>
 <li>pt for Portuguese</li>
 <li>pt-br for Brazilian Portuguese</li>
 <li>ro for Romanian</li>
 <li>ru for Russian</li>
 <li>sk for Slovak</li>
 <li>sl for Slovenian</li>
 <li>sq for Albanian</li>
 <li>sr for Serbian</li>
 <li>sr-latn for Serbian Latin</li>
 <li>sv for Swedish</li>
 <li>sw for Swahili</li>
 <li>ta for Tamil</li>
 <li>te for Telugu</li>
 <li>th for Thai</li>
 <li>tr for Turkish</li>
 <li>tt for Tatar</li>
 <li>udm for Udmurt</li>
 <li>uk for Ukrainian</li>
 <li>ur for Urdu</li>
 <li>vi for Vietnamese</li>
 <li>zh-hans for Simplified Chinese</li>
 <li>zh-hant for Traditional Chinese</li>
</ul>

