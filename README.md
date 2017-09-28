# Translator-API

<h1>Description</h1>
<p>To translate the given text into any language</p>

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
 <li>('es-co', 'Colombian Spanish')</li>
 <li>('es-mx', 'Mexican Spanish')</li>
 <li>('es-ni', 'Nicaraguan Spanish')</li>
 <li>('es-ve', 'Venezuelan Spanish')</li>
 <li>('et', 'Estonian')</li>
 <li>('eu', 'Basque')</li>
 <li>('fa', 'Persian')</li>
 <li>('fi', 'Finnish')</li>
 <li>('fr', 'French')</li>
 <li>('fy', 'Frisian')</li>
 <li>('ga', 'Irish')</li>
 <li>('gd', 'Scottish Galic')</li>
 <li>('gl', 'Galician')</li>
 <li>('he', 'Hebrew')</li>
 <li>('hi', 'Hindi')</li>
 <li>('hr', 'Croatian')</li>
 <li>('hsb', 'Upper Sorbian')</li>
 <li>('hu', 'Hungarian')</li>
 <li>('ia', 'Interlingua')</li>
 <li>('id', 'Indonesian')</li>
 <li>('io', 'Ido')</li>
 <li>('is', 'Icelandic')</li>
 <li>('it', 'Italian')</li>
 <li>('ja', 'Japanese')</li>
 <li>('ka', 'Georgian')</li>
 <li>('kk', 'Kazakh')</li>
 <li>('km', 'Khmer')</li>
 <li>('kn', 'Kannada')</li>
 <li>('ko', 'Korean')</li>
 <li>('lb', 'Luxembourgish')</li>
 <li>('lt', 'Lithuanian')</li>
 <li>('lv', 'Latvian')</li>
 <li>('mk', 'Macedonian')</li>
 <li>('ml', 'Malayalam')</li>
 <li>('mn', 'Mongolian')</li>
 <li>('mr', 'Marathi')</li>
 <li>('my', 'Burmese')</li>
 <li>('nb', 'Norwegian Bokmål')</li>
 <li>('ne', 'Nepali')</li>
 <li>('nl', 'Dutch')</li>
 <li>('nn', 'Norwegian Nynorsk')</li>
 <li>('os', 'Ossetic')</li>
 <li>('pa', 'Punjabi')</li>
 <li>('pl', 'Polish')</li>
 <li>('pt', 'Portuguese')</li>
 <li>('pt-br', 'Brazilian Portuguese')</li>
 <li>('ro', 'Romanian')</li>
 <li>('ru', 'Russian')</li>
 <li>('sk', 'Slovak')</li>
 <li>('sl', 'Slovenian')</li>
 <li>('sq', 'Albanian')</li>
 <li>('sr', 'Serbian')</li>
 <li>('sr-latn', 'Serbian Latin')</li>
 <li>('sv', 'Swedish')</li>
 <li>('sw', 'Swahili')</li>
 <li>('ta', 'Tamil')</li>
 <li>('te', 'Telugu')</li>
 <li>('th', 'Thai')</li>
 <li>('tr', 'Turkish')</li>
 <li>('tt', 'Tatar')</li>
 <li>('udm', 'Udmurt')</li>
 <li>('uk', 'Ukrainian')</li>
 <li>('ur', 'Urdu')</li>
 <li>('vi', 'Vietnamese')</li>
 <li>('zh-hans', 'Simplified Chinese')</li>
 <li>('zh-hant', 'Traditional Chinese')</li>

</ul>

