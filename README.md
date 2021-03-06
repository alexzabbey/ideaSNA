# ideaSNA
<img src="https://raw.githubusercontent.com/alexzabbey/ideaSNA/master/Images/all1.png" alt="האנציקלופדיה של הרעיונות" />
<blockquote dir="rtl">“האנציקלופדיה של הרעיונות” הינה חיבור אנציקלופדי מקורי וביקורתי על תרבות, מחשבה ותקשורת בנות זמננו; מדריך תיאורטי ושימושי למסע בין תחומי דעת מרכזיים של חיי הרוח והיומיום, הכולל מאות ערכים על הרעיונות המעצבים את חיינו. האנציקלופדיה שנכתבה בידי ד"ר דוד גורביץ וד"ר דן ערב, יצאה לאור כספר בשנת 2012 בהוצאת בבל.</blockquote>
<p dir="rtl">כדי להתאמן בפייתון, SQL ו-SNA, חשבתי שיהיה מגניב לנסות לנתח את הקישורים הפנימיים ב"אנציקלופדיה של הרעיונות" (http://haraayonot.com/). בדרך גיליתי מה הרעיונות המרכזיים והחשובים בעולם היום, ניתחתי קבוצות של רעיונות, ולמדתי כמה שיעורים.</p>


<p dir="rtl"></p>
<p dir="rtl"></p>
<p dir="rtl"></p>
<p dir="rtl"></p>



<h2 dir="rtl">התהליך</h2>
<p dir="rtl">התחלתי בלבנות סקרייפר. השתמשתי בספריית requests כדי לנהל את ה-http sessions ובספריית beautifulsoup בשביל הparsing. בשלב הראשון חילצתי את רשימת כל הערכים (http://haraayonot.com/alphabetic-ideas/), והסקרייפר עבר על כל ערך, מצא את שם הערך בעברית ובאנגלית, את ה-URL של הדף ונתן לכל דף מספר סידורי. את כל המידע הזה שמתי בטבלת nodes ב-sqlite. לאחר מכן הסקרייפר עבר ערך ערך והוציא את כל הלינקים מכל ערך, בדק את המס"ד שמקושר ללינק בטבלת ה-nodes, והכניס הכל לטבלת edges.</p>
<p dir="rtl">בסוף התהליך, ואחרי שניקיתי קצת את המידע (והסתבכתי קשות עם ה-encoding), יצאו 540 nodes, ו-12,125 edges. מרשים. פתחתי את הטבלאות ב-Gephi.</p>
<h2 dir="rtl">הממצאים</h2>
<p dir="rtl">כדי להכין את הסקרייפר הייתי צריך לשוטט קצת באתר ולהבין איך הוא בנוי. הנחתי, שכיוון לחיבור קוראים "האנציקלופדיה של הרעיונות" כשאסיים לנתח אותו אדע מה הרעיונות החשובים ביותר בעולם. מה שהבנתי בדיעבד, זה שלפני הכל, צריך להבין את המידע שעובדים איתו. כלומר התברר לי כשעברתי על הערכים ובייחוד כשהערך עם הכי הרבה centrality היה פוסט-מודרניזם, שהאינציקלופדיה של הרעיונות זו כותרת מעט יומרנית למה שהוא בפועל "האנציקלופדיה של הרעיונות המערביים הפרוגרסיביים של מאה ה-21". לא תמצאו בו ערך על האידיאות של אפלטון או אפילו על הומניזם, אבל בהחלט ניתן למצוא בו ערכים כמו <a href="http://haraayonot.com/idea/intertextuality/">אינטרטקסטואליות</a> ו<a href="http://haraayonot.com/idea/technogothic/">טכנוגותיקה</a>.</p>
<p dir="rtl">אם כך, על פי הממצאים, ניתן לראות בבירור שעולם המחשבה שמציגה האנציקלופדיה מבוססת ברובה על החשיבה הפוסטמודרנית, ואכן זה הערך שקיבל את ה-degree, ה-centrality וה-betweenness הגבוהים ביותר (בעודו מפוצל למספר ערכים שונים(!)- פוסטמודרניזם באומנות, בפילוסופיה וכו'). ואיתו מושגים בהקשר דומה: אני/אחר, ייצוג, אובייקט/סובייקט, ועוד.</p>
<h3 dir="rtl">מסקנה ראשונה: הדרך היעילה ביותר להבין את העולם של ימינו היא לקרוא פוקו ודרידה. ולראות טלוויזיה</h3>
<p dir="rtl">הנחת היסוד: כדי להבין כמה שיותר מושגים שקשורים לעולם המחשבה של ימינו, כדאי שנמצא את הערכים עם ה-betweenness הגבוה ביותר, כלומר אלה שהכי יעיל לעבור דרכם כשאנחנו עוברים בין ערכים שונים ברשת. </p>
<p dir="rtl">בראש הדירוג הזה עומד כמובן ה<a href="http://haraayonot.com/idea/postmodernism-in-philosophy/">פוסטמודרניזם</a>, אחריו <a href="http://haraayonot.com/idea/television/">טלוויזיה</a>, ואז <a href="http://haraayonot.com/idea/modernity/">מודרניזם</a> (כנראה שצריך להבין רעיונות מודרניסטיים כדי להבין מה זה פוסטמודרניזם).</p>
<h3 dir="rtl">מסקנה שנייה: כדי להבין את העולם של ימינו, הכי חשוב לקרוא אדם סמית'</h3>
<p dir="rtl">הנחת היסוד: כדי להבין את מושג כלשהו, צריך להבין את כל הערכים שמוזכרים בו. דמיינו שאתם קוראים ערך ופתאום מופיע מושג שאתם לא מכירים- הדבר ההגיוני לעשות הוא לקרוא את הערך שמסביר את המושג. כלומר, הערכים עם ה-In-Degree הגבוה ביותר הם הערכים שנדרש להבין אותם כדי להבין הכי הרבה רעיונות אחרים באינציקלופדיה. ה-TOP-5 בדירוג הזה הם <a href=” http://haraayonot.com/idea/capitalism/”>קפיטליזם</a> (171), <a href="http://haraayonot.com/idea/postmodernism-in-philosophy/">פוסטמודרניזם</a> (155), <a href="http://haraayonot.com/idea/meaning/">משמעות</a> (148), <a href="http://haraayonot.com/idea/selfother/">אני/אחר</a> (147), ו<a href="http://haraayonot.com/idea/objectsubject/">אובייקט/סובייקט </a> (142).</p>
<h3 dir="rtl">מסקנה שלישית: על שישה דברים העולם עומד</h3>
<p dir="rtl">הופתעתי לגלות עד כמה הקהילות שנתן לי אלגוריתם Louvain היו מובהקות מבחינה נושאית. אחרי סריקה איכותנית של כל אחת מהקהילות, גיליתי שהמדד שהכי התאים לכותרות האיכותניות שנתתי לכל קהילה היה הdegree, כשהערכים עם ה-degree הגבוה ביותר בדרך כלל היו בעלי הדימיון הרב ביותר לכותרת האיכותנית שאני נתתי. להלן הקהילות ע"פ גודלן, בסדר יורד:</p>

<img src="https://raw.githubusercontent.com/alexzabbey/ideaSNA/master/Images/community4nodeslabels.png" alt="פילוסופיה פוסטמודרנית"/>
<p dir="rtl">הקהילה הגדולה ביותר, פילוסופיה פוסטמודרנית ורעיונות נוספים</p>
<br />
<img src="https://raw.githubusercontent.com/alexzabbey/ideaSNA/master/Images/community3nodeslabels.png" alt="תרבות וטכנולוגיה" />
<p dir="rtl">תרבות וטכנולוגיה</p>
<br />
<img src="https://raw.githubusercontent.com/alexzabbey/ideaSNA/master/Images/community1nodeslabels.png" alt="קפיטליזם" />
<p dir="rtl">החיים בתרבות קפיטליסטית. תת הקהילה הירוקה עוסקת באורבניות ועיר, הכתומה בתנוכות נגד לקפיטליזם, הכחולה בקפיטליזם, גלובליזציה ונגזרותיהן המעשיות, והסגולה בתרבות הצריכה</p>
<br />
<img src="https://raw.githubusercontent.com/alexzabbey/ideaSNA/master/Images/community2nodeslabels.png" alt="אומנות מודרנית" />
<p dir="rtl">אומנות מודרנית: תתי קהילות ירוקה וסגולה מורכבות מתנועות באומנות מודרנית ורעיונות בהקשר הזה, הכחולה בתרבות חזותית, והירוקה והמובהקת מכולם במוזיקה</p>
<br />
<img src="https://raw.githubusercontent.com/alexzabbey/ideaSNA/master/Images/community5nodeslabels.png" alt="האני, זהות" />
<p dir="rtl">ה"אני", זהות</p>
<br />
<img src="https://raw.githubusercontent.com/alexzabbey/ideaSNA/master/Images/community0nodeslabels.png" alt="אידיאולוגיה" />
<p dir="rtl">הערך "אידיאולוגיה" הוא בעל הdegree והbetweenness הגבוהים ביותר, והוא המגדיר המובהק של הקהילה הזו. תתי קהילות התחלקו די יפה. תת הקהילה הסגולה מורכבת בבירור מאידיאולוגיות שקשורות למיעוטים, הדרתם מהחברה והרעיונות שעומדים מאחורי ההדרה או באים כביקורת עליה. הקהילה הירוקה נראית קשורה יותר לזהות ולהגדרה עצמית. הכחולה עוסקת בפילוסופיה מרקסיסטית על שלל רכיביה?, והקבוצה הכתומה היא יותר מטא-,בערכים בה עוסקים בפרקטיקות מטא-רעיוניות- כמו ביקורת, שיח ועוד.</p>
<h2 dir="rtl">מה הלאה?</h2>
<p dir="rtl">לא החלטתי עדיין, אבל חשבתי שאפשר:</p>
<ul dir="rtl">
<li>לכרות את כל ההוגים המוזכרים בערכים השונים, ולנסות לאמוד את השפעתם, את תחומי החיים שעסקו בהם וכו'</li>
<li>להפוך את המידע לגרף אינטראקטיבי עם D3, כך שתתאפשר אקספלורציה נוחה יותר של המידע</li>
<li>לקחת את הערכים במקבילים בויקיפדיה ולעשות להם בדיקה דומה</li>
</ul>
<img src="https://raw.githubusercontent.com/alexzabbey/ideaSNA/master/Images/network.png" alt="רשת" />
<p dir="rtl">תודה שקראתם! אשמח לשמוע הערות וללמוד מאנשים שמבינים בתחום באמת :)</p>
